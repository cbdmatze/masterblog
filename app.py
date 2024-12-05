from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)

# Set secret key for CSRF protection and session management using the value from .env
app.config['SECRET_KEY'] = os.getenv('FLASK_SECRET_KEY', 'fallback_secret_key')  # Use a fallback key if env var is missing

# Set up the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Initialize migration and CSRF protection
migrate = Migrate(app, db)
csrf = CSRFProtect(app)


# Define the blog post model (database table structure)
class BlogPost(db.Model):
    """
    Represents a blog post in the database with an ID, author, title, content, and likes.
    """
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    likes = db.Column(db.Integer, default=0)  # Add 'likes' column

    def __repr__(self):
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


@app.route('/')
def index():
    """
    Displays all the blog posts from the database.
    
    Returns:
        Rendered HTML template with a list of all posts.
    """
    posts = BlogPost.query.all()  # Fetch all posts from the database
    return render_template('index.html', posts=posts)


@app.route('/add', methods=['GET', 'POST'])
def add():
    """
    Displays a form to add a new blog post or adds the new post to the database if the form is submitted.
    
    Returns:
        Rendered HTML template for adding a post, or redirects to the homepage after adding a post.
    """
    if request.method == 'POST':
        new_post = BlogPost(
            author=request.form['author'],
            title=request.form['title'],
            content=request.form['content']
        )
        db.session.add(new_post)
        db.session.commit()  # Save to the database
        
        # Flash success message and redirect
        flash('Post created successfully!', 'success')
        return redirect(url_for('index'))  # Redirect to the homepage
    
    return render_template('add.html')


@app.route('/delete/<int:id>')
def delete_post(id):
    """
    Deletes a blog post by its ID and removes it from the database.
    
    Args:
        id (int): The ID of the blog post to delete.
    
    Returns:
        Redirects to the homepage after deleting the post.
    """
    post = BlogPost.query.get_or_404(id)  # Get the post by ID or return 404
    db.session.delete(post)
    db.session.commit()  # Delete from the database
    
    # Flash success message and redirect
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_post(id):
    """
    Displays a form to update an existing blog post or updates the post in the database if the form is submitted.
    
    Args:
        id (int): The ID of the blog post to update.
    
    Returns:
        Rendered HTML template for updating a post, or redirects to the homepage after updating the post.
    """
    post = BlogPost.query.get_or_404(id)  # Fetch the blog post by ID
    if request.method == 'POST':
        # Update the post in the database
        post.author = request.form['author']
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()  # Save changes to the database
        
        # Flash success message and redirect
        flash('Post updated successfully!', 'success')
        return redirect(url_for('index'))  # Redirect to the homepage
    
    return render_template('update.html', post=post)


@app.route('/like/<int:id>')
def like_post(id):
    """
    Increments the like count of a blog post and saves the updated data to the database.
    
    Args:
        id (int): The ID of the blog post to like.
    
    Returns:
        Redirects to the homepage after liking the post.
    """
    post = BlogPost.query.get_or_404(id)  # Fetch the blog post by ID
    post.likes += 1  # Increment the like count
    db.session.commit()  # Save the change to the database
    
    # Flash success message and redirect
    flash('Post liked!', 'success')
    return redirect(url_for('index'))  # Redirect to the homepage


if __name__ == "__main__":
    """
    Starts the Flask application on the specified host and port.
    """
    app.run(host='0.0.0.0', port=5003, debug=True)
