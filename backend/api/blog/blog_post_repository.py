from repository import Repository
from api.blog.blog_post_model import BlogPost


class BlogPostRepository(Repository):
    model = BlogPost
