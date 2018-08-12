from flask import jsonify, request, Blueprint, render_template
from api.blog.blog_post_service import BlogPostService
from decorators.user_decorators import login_required

main = Blueprint('main', __name__)

@main.route('/')
def get_main():

    render_data = {
      'info': 'some_info',
      'blog_posts': BlogPostService.get_all_blog_posts()

    }
    return render_template('main.html', render_data=render_data)

add_post = Blueprint('add_post', __name__)

@add_post.route('/post/add')
@login_required
def add_new_post(current_user):
    print('here we are')
    print(request)
    print(request.headers)
    return render_template('edit_post.html', user=current_user)


contacts = Blueprint('contacts', __name__)

@contacts.route('/contacts')
def contact_us():
    return render_template('contacts.html')

donate = Blueprint('donate', __name__)

@donate.route('/donate')
def donate_money():
    return render_template('donate.html')
