from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# Set up the SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define the blog post model (database table structure)
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Post({self.title}, {self.author})"
    

# Create the database and tables (run only once initially)
@app.before_request
def create_tables():
    db.create_all()


# Index route to display all blog posts
@app.route('/')
def index():
    posts = BlogPost.query.all()  # Fetch all posts from the database
    return render_template('index.html', posts=posts)


# Route to add a new post
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_post = BlogPost(
            author=request.form['author'],
            title=request.form['title'],
            content=request.form['content']
        )
        db.session.add(new_post)
        db.session.commit()  # Save to the database
        return redirect(url_for('index'))  # Redirect to the homepage
    return render_template('add.html')


# Route to delete a post
@app.route('/delete/<int:id>')
def delete_post(id):
    post = BlogPost.query.get_or_404(id)  # Get the post by ID or return 404
    db.session.delete(post)
    db.session.commit()  # Delete from the database
    return redirect(url_for('index'))


# Route to update a post
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_post(id):
    post = BlogPost.query.get_or_404(id)  # Fetch the blog post by ID
    if request.method == 'POST':
        # Update the post in the database
        post.author = request.form['author']
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()  # Save changes to the database
        return redirect(url_for('index'))  # Redirect to the homepage
    return render_template('update.html', post=post)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)
