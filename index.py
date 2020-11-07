from optimal import app, db
from optimal.models import User, Post

@app.shell_context_processor
def make_shell_context():
    """
    Attaches the User, Post to the Flask App Shell Instance
    """
    return {'db': db, 'User': User, 'Post': Post}