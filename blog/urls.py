from django.urls import path, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap

from blog.sitemaps import PostSitemap

from . import views

app_name = 'blog'

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    # post views
    path('', views.PostListView.as_view(), name='post_list'),
    path('tag/<slug:tag_slug>', views.PostListView.as_view(), name='post_list_by_tag'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
    path('<int:post_id>/share/', views.share_post, name='share_post'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap')
]