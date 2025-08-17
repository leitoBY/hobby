from backend.repository import Repository
from backend.api.blog.blog_post_model import BlogPost


class BlogPostRepository(Repository):
    model = BlogPost
