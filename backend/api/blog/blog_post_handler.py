from flask import jsonify, Blueprint, render_template, request
from backend.api.blog.blog_post_service import BlogPostService

blog_post_api = Blueprint('blog_post_api', __name__)


@blog_post_api.route('/api/blog_post/create', methods=['POST'])
def add_post():
    if request.method == 'POST':
        body = request.get_json()
        BlogPostService.create_blog_post(user=None, data=body)
        return jsonify({"message": "Blog post was successfully added"})

    return jsonify(message="Something went wrong")
