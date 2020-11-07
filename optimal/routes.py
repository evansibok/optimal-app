from flask import render_template, flash, redirect, url_for
from optimal import app
from optimal.forms import RegForm, LoginForm


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegForm()
    if form.validate_on_submit():
        flash(f'Account creation success for {form.username.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for {form.email.data}, {form.remember_me.data}!', 'success')
        return redirect(url_for('posts'))
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
