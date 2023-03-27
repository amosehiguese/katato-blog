# Katato Blog With Django

This is a Django-based blog app that allows users to view, and comment on blog posts. In addition to standard blog features, this app includes the following features:

- Pagination: The blog posts are paginated to make navigation easier for the user.
- Share via Email: Users can share blog posts via email.
- Tagging: Users can tag their blog posts with relevant tags using the `Taggit` library.
- Custom Template Tags and Filters: The app includes custom template tags and filters to enhance the appearance and functionality of the app.
- Custom Sitemap and RSS Feed: The app includes a custom sitemap and RSS feed for blog posts to help with search engine optimization and feed readers.
- Full Text Search: The app includes full-text search functionality to allow users to search for blog posts based on keywords.

## Installation

To install and run this app, follow these steps:

- lone the repository: `git clone https://github.com/amosehiguese/katato-blog.git`
- Install the required packages: pip install -r requirements.txt
- Set up the database: python manage.py migrate
- Create a superuser: python manage.py createsuperuser
- Run the app: python manage.py runserver

## Usage

Once the app is installed and running, users can do the following:

1. Create a new blog post: Click on "New Post" and fill in the details using the admin site.
2. View a blog post: Click on a blog post title to view the post.
3. Comment on a blog post: Click on "Comment" and enter your comment.
4. Share a blog post via email: Click on "Share" and enter the recipient's email address.
5. Tag a blog post: Enter relevant tags when creating a new post.

## Other Features

- This blog makes use of custom template tags and filters using `simple_tag` and `inclusion_tag` helper functions.

- It uses Django sitemap framework to generate sitemaps for the blog site dynamically

- It uses Django built-in syndication feed framework to dynamically generate RSS or Atom feeds.

- It uses a search functionality built on top of PostgreSQL to provide full-text search features
