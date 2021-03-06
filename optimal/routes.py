from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse
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
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!', 'danger')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('posts')
        return redirect(next_page)
    return render_template('login.html', title="Login", form=form)

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    logout_user()
    flash('Logout successful!', 'success')
    return redirect(url_for('home'))


@app.route('/posts', methods=['GET'])
@login_required
def posts():
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
    return render_template("posts.html", title="Posts", posts=blogPosts)
