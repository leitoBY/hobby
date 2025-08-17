from datetime import datetime
from backend.api.users.user_model import User
from backend.api.blog.blog_post_model import BlogPost
from backend.api.blog.blog_post_repository import BlogPostRepository


class BlogPostService(object):

    @classmethod
    def get_all_blog_posts(cls) -> list:
        blog_posts = []
        posts =  BlogPostRepository.get_all()
        for post in posts:
            blog_posts.append({
                'id': post.id,
                'created_at': post.created_at.strftime("%d.%m.%Y"),
                'title': post.title,
                'author': post.author,
                'content': post.content,
                'comments': post.comments
            })
        return blog_posts

    @classmethod
    def create_blog_post(cls, user: User, data: dict) -> BlogPost:
        new_blog_post = BlogPost(
            created_at = datetime.utcnow(),
            title=data.get('title'),
            content=data.get('content'),
            author=data.get('email'),
            user_id=user.id if user else None  # TODO get info from token if user authenticated
        )
        BlogPostRepository.add(new_blog_post)
        BlogPostRepository.commit()
        return new_blog_post
