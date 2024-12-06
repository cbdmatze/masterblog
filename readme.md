
---

# BlogPost Application

Welcome to the **BlogPost Application**! This web app allows users to create, update, delete, and "like" blog posts. The app is built using Flask and provides a simple yet effective interface for managing blog content.

## Features

- **Create Blog Posts**: Users can easily add new blog posts by providing an author name, a title, and the content of the post.
- **Update Existing Posts**: Users can update the content of any existing blog post.
- **Delete Blog Posts**: Users can delete blog posts they no longer want to keep.
- **Like Blog Posts**: Each post can be liked, with the like count displayed next to the post.
- **Flash Messaging**: Success and error messages are shown dynamically using Flask’s built-in flash message functionality.
- **Mobile-Responsive Design**: The app is fully responsive and adjusts well on mobile devices.
- **SQLite Database**: The app uses an SQLite database to store blog posts and manage them efficiently.
- **CSRF Protection**: Flask-WTF extension provides CSRF protection to ensure secure form submissions.
- **Flask-Migrate for Database Migrations**: Database schema changes are managed with Flask-Migrate to handle upgrades and downgrades.

## Project Structure

```
BlogPost/
│
├── app.py               # Main Flask application
├── models.py            # Defines the BlogPost model for the SQLite database
├── templates/
│   ├── index.html       # Home page to display all blog posts
│   ├── add.html         # Form to create a new blog post
│   ├── update.html      # Form to update an existing blog post
│
├── migrations/          # Folder for Flask-Migrate database migration scripts
├── static/
│   └── style.css        # CSS file for styling the web pages
│
├── instance/
│   └── app.db           # SQLite database
│
├── config.py            # Configuration settings (including for the database)
└── README.md            # Project documentation (this file)
```

## Getting Started

### Prerequisites

- Python 3.x installed on your system.
- Basic knowledge of Flask, SQLAlchemy, and Jinja2 templating.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/BlogPost.git
   cd BlogPost
   ```

2. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the SQLite database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

### Running the Application

1. Set the Flask app environment variable:

   ```bash
   export FLASK_APP=app.py   # On Windows, use `set FLASK_APP=app.py`
   ```

2. Run the Flask development server:

   ```bash
   flask run
   ```

3. Open your browser and visit `http://127.0.0.1:5000/` to view the app.

### SQLite Database

The **SQLite database** is used to store all the blog posts in the app. The database file (`app.db`) is stored in the `instance/` folder. The database schema is defined in `models.py` using **SQLAlchemy ORM**. Here’s how it works behind the scenes:

- Each blog post is represented as an instance of the `BlogPost` class, which maps directly to a table in the SQLite database.
- SQLAlchemy handles all interactions with the database, such as inserting, querying, updating, and deleting blog posts.
  
When the app runs for the first time, the database is created, and the structure is updated using **Flask-Migrate**.

### Flask-Migrate (Database Migrations)

The project uses **Flask-Migrate** to handle database migrations. Flask-Migrate is an extension that handles **Alembic** integration with SQLAlchemy. Here's how it works:

- When you make changes to the database schema (e.g., adding new fields), you'll run:

  ```bash
  flask db migrate -m "Description of change"
  flask db upgrade
  ```

- This will generate a migration script and apply the schema changes to the database without losing the existing data.
  
Migrations are stored in the `migrations/` folder.

### CSRF Protection

The project uses **Flask-WTF** to handle forms and provide **CSRF (Cross-Site Request Forgery) protection**. CSRF protection ensures that forms submitted in the app are validated and protected from external attacks.

- Every form includes a hidden CSRF token, automatically generated for each session.
- If a form submission lacks a valid CSRF token, the request is rejected, ensuring that only legitimate form submissions are processed.

## Directory Overview

- **`app.py`**: The main Flask application that defines the routes, handles requests, and renders templates.
- **`models.py`**: Defines the `BlogPost` class (model) for interacting with the SQLite database.
- **`migrations/`**: Contains the Alembic scripts for database migrations.
- **`templates/`**: Contains the HTML files rendered by Flask (for creating, updating, and viewing blog posts).
- **`static/`**: Holds static files, such as the `style.css` file for styling the app.
- **`instance/`**: Contains the SQLite database file (`app.db`) that stores the blog posts.

### App Functionality

#### Home Page (Index)
- Displays a list of all blog posts.
- Each post shows the title, author, content, and the number of likes.
- Users can perform the following actions:
  - **Like** a post (via a green "Like" button).
  - **Update** a post.
  - **Delete** a post.

#### Create New Post
- Accessible via a "Create New Post" button on the home page.
- Users are prompted to enter the author name, title, and content for the new post.

#### Update Post
- Users can update the title, author, or content of a post through the "Update" button on each post.

#### Delete Post
- Clicking the "Delete" button will remove a post from the list.

## Styling

The project uses a simple and clean CSS design (`style.css`). Some key styles:
- **General Styling**: Uses a light-grey background for the body and a centered, white container for content.
- **Button Styles**: Buttons use different colors for actions like submitting (blue), deleting (red), and liking (green). Hover effects provide interactive feedback to users.
- **Mobile Responsiveness**: The layout adapts to mobile screens, ensuring the content looks good on all devices.

## Contributing

Feel free to submit issues or pull requests if you have any suggestions or improvements. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Enjoy building and managing your blog content with the BlogPost application! 🎉

---

### Additional Notes

- **Flask-Migrate**: If you add new fields to your model (like a new attribute to the blog post), don't forget to generate and apply a new migration using `flask db migrate` and `flask db upgrade`.
- **CSRF Protection**: CSRF protection ensures that only authorized forms are processed, improving the security of your app.

---

