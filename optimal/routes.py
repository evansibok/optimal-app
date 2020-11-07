from flask import render_template
from optimal import app
from optimal.forms import RegForm, LoginForm

@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegForm()
    # if request.method == 'POST' and form.validate_on_submit():
    # flash(
    #     f'Account creation success for {form.username.data}!', 'success')
    #     return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    # if request.method == 'POST' and form.validate_on_submit():
    # flash(
    #     f'Account creation success for {form.email.data}!', 'success')
    #     return redirect(url_for('posts'))
    return render_template('login.html', title="Login", form=form)

@app.route('/posts', methods=['GET'])
def posts():
    user = {'username': 'EVANSIBOK'}
    blogPosts = [
        {
            'id': 1,
            'author': 'evansibok',
            'title': 'First Blog Post',
            'content': 'This is the first blog post!',
            'date_posted': 'Nov 6, 2020',
        },
        {
            'id': 2,
            'author': 'jonwen',
            'title': 'Second Blog Post',
            'content': 'This is the second blog post!',
            'date_posted': 'Nov 6, 2020',
        },
    ]
    return render_template("posts.html", title="Posts", posts=blogPosts, user=user)
