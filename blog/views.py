# Django import
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.db.models import Count
from django.views.generic import ListView

# Model import
from .models import Post, Comment
from .forms import EmailPostForm, CommentForm

# 3rd party model import 
from taggit.models import Tag

# List View
class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_slug = self.kwargs.get('tag_slug')
        print(tag_slug)
        if tag_slug:
            tag = get_object_or_404(Tag, slug=tag_slug)
            queryset = queryset.filter(tags__in=[tag])
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag_slug = self.kwargs.get('tag_slug')
        if tag_slug:
            tag = get_object_or_404(Tag, slug=self.kwargs['tag_slug'])
            context['tag'] = tag
        return context
    
# Detail view
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='published', publish__year=year, publish__month=month, publish__day=day)

    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    # Retrieve all tags for the current post
    post_tags_ids = post.tags.values_list('id', flat=True)

    # Get all posts with related tags exclude current post
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)

    # Count tags for similar_posts and order in desc by same_tags and by time published
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:4]

    return render(request,
                   'blog/post/detail.html', {
        'post': post, 
        'comments': comments, 
        'new_comment': new_comment, 
        'comment_form': comment_form,
        'similar_posts': similar_posts,
        }
            )


# Post sharing view
def share_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, status='published')
    sent = False

    if request.method == 'POST':
        # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            #  Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(
                post.get_absolute_url()
            )
            subject = f"{cd['name']} recommends you read {post.title}"
            message = f"Read {post.title} at {post_url}\n\n{cd['name']}\'s comments: {cd['comments']}"
            send_mail(subject, message, 'amosehiguese@gmail.com', [cd['to']])
            send = True
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {
        'post': post,
        'form': form,
        'sent': sent,
    })