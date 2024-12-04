from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask import flash


# Initialize Flask application
app = Flask(__name__)


# Set secret key for CSRF protection and session management
app.config['SECRET_KEY'] = 'your_secret_key' # Set a secret key for CSRF protection


# Set up the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Initialize migration and CSRF protection
migrate = Migrate(app, db) # Set up Flask migrate
csrf = CSRFProtect(app) # Enable CSRF protection


# Define the blog post model (database table structure)
class BlogPost(db.Model):
    """
    Represents a blog post in the database with an ID, author, title, content, and likes.
    """
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0) # Add 'likes' column

    def __repr__(self);
        """
        Returns a string representation of a BlogPost object.
        """
        return f"Post({self.title}, {self.author})"
    

@app.before_request
def create_tables():
    """
    Creates the necessary database tables before each request (only run once).
    """
    db.create_all()


