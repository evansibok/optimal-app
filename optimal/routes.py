from flask import render_template, flash, redirect, url_for
from flask_login import current_user, login_user
from optimal import app, db
from optimal.forms import RegForm, LoginForm
from optimal.models import User


u = User()


@app.route('/')
@app.route('/home')
def home():
    return render_template("home.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    form = RegForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password_hash = u.set_password(form.password.data)
        user = User(username=username, email=email, password_hash=password_hash)
        db.session.add(user)
        db.session.commit()
        # flash success message
        flash(f'Account creation success for {form.username.data}! Please login to continue!', 'success')
        # redirect to login
        return redirect(url_for('login'))
    return render_template('register.html', title="Register", form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('posts'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
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
