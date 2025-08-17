from flask import jsonify, Blueprint, render_template, request
from backend.api.comment.comment_service import CommentService

comment_api = Blueprint('comment_api', __name__)


@comment_api.route('/api/blog_post/<post_id>/add', methods=['POST'])
def add_comment(post_id):
    if request.method == 'POST':
        body = request.get_json()
        CommentService.add_comment(user=None, post_id=post_id, data=body)
        return jsonify({"message": "Blog post was successfully added"})

    return jsonify(message="Something went wrong")
