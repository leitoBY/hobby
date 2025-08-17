from flask import request, Blueprint, render_template
from backend.api.blog.blog_post_service import BlogPostService
from backend.decorators.user_decorators import login_required, get_current_user

main = Blueprint('main', __name__)

@main.route('/')
def get_main():
    current_user = get_current_user()
    render_data = {
      'info': 'some_info',
      'blog_posts': BlogPostService.get_all_blog_posts()

    }
    return render_template('main.html', render_data=render_data, user=current_user)

add_post = Blueprint('add_post', __name__)

@add_post.route('/post/add')
@login_required
def add_new_post(current_user):
    return render_template('edit_post.html', user=current_user)


contacts = Blueprint('contacts', __name__)

@contacts.route('/contacts')
def contact_us():
    current_user = get_current_user()
    return render_template('contacts.html', user=current_user)

donate = Blueprint('donate', __name__)

@donate.route('/donate')
def donate_money():
    current_user = get_current_user()
    return render_template('donate.html', user=current_user)
