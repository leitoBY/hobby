from flask import jsonify, Blueprint, render_template
from api.blog.blog_post_service import BlogPostService


main = Blueprint('main', __name__)

@main.route('/')
def get_main():

    render_data = {
      'info': 'some_info',
      'blog_posts': BlogPostService.get_all_blog_posts()

    }
    return render_template('main.html', render_data=render_data)
