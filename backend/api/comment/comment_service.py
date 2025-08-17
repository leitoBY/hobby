from datetime import datetime
from backend.api.users.user_model import User
from backend.api.comment.comment_model import Comment


class CommentService(object):

    @classmethod
    def add_comment(cls, user: User, post_id: int, data: dict) -> Comment:

        new_comment = Comment(
            created_at=datetime.utcnow(),
            title=data.get('title'),
            message=data.get('message'),
            post_id=post_id,
            user_id=user.id if user else None
        )
        return new_comment
