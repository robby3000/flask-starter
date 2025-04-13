# Flask Starter Project

This is a starter template for building modern web applications using Flask. It comes pre-configured with a robust set of tools and features to accelerate development.

## Features

*   **Flask Core**: Uses the Flask microframework with an Application Factory pattern.
*   **Blueprints**: Organized structure with `main` and `auth` blueprints.
*   **Database**: SQLAlchemy ORM for database interactions.
*   **Authentication**:
    *   User registration and login functionality.
    *   Password hashing with Bcrypt (via Flask-Bcrypt).
    *   Session management with Flask-Login.
*   **Forms**: Secure forms using WTForms (via Flask-WTF) with CSRF protection. Includes email validation (`email-validator`).
*   **Frontend Stack**:
    *   **Tailwind CSS**: Utility-first CSS framework for rapid UI development.
    *   **Alpine.js**: Minimal JavaScript framework for adding behavior to your markup.
    *   **HTMX**: Enables modern browser features directly from HTML.
*   **Asset Pipeline**: Webpack configured for bundling and processing CSS (with PostCSS/Tailwind) and JavaScript assets.
*   **Configuration**: Environment-based configuration using `.env` files (via `python-dotenv`).
*   **Database Management**: Custom Flask CLI command (`flask init-db`) to initialize the database schema.
*   **Extensions**: Includes Flask-SQLAlchemy, Flask-Migrate (though migrations aren't fully set up yet), Flask-WTF, Flask-Login, Flask-Bcrypt, Flask-HTMX.

## Getting Started

Follow these steps to set up a new project based on this template:

### Prerequisites

*   Python 3 (tested with 3.13)
*   Node.js and npm (or yarn)

### Setup Instructions

1.  **Clone or Copy the Project:**
    ```bash
    # Either clone the repository if it's hosted on Git
    # git clone <repository_url> new-project-name
    # cd new-project-name

    # Or copy the flask-starter directory
    cp -r /path/to/flask-starter /path/to/new-project-name
    cd /path/to/new-project-name
    ```

2.  **Create and Activate a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3.  **Install Python Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure Environment Variables:**
    *   Copy the example environment file:
        ```bash
        cp .env.example .env
        ```
    *   **Edit the `.env` file:**
        *   Generate a strong, unique `SECRET_KEY`. You can use `python -c 'import secrets; print(secrets.token_hex(16))'` to generate one.
        *   Update `DATABASE_URL` with your actual database connection string (e.g., for PostgreSQL, SQLite, etc.). Example format for Supabase Postgres is provided in the file.

5.  **Rename Project Placeholders:**
    *   Edit `package.json`: Change the `"name"` value from `"flask-starter"` to your new project's slug (e.g., `"ThenextInsta"`).
    *   Edit `app/templates/base.html`: Replace all instances of "Flask Starter" with your new project's display name (e.g., "ThenextInsta").
    *   Edit `app/templates/index.html`: Replace "Welcome to Flask Starter!" with your new project's welcome message (e.g., "Welcome to ThenextInsta!").

6.  **Install Node.js Dependencies:**
    *   Remove the old lock file and node_modules directory (essential after changing package name):
        ```bash
        rm -f package-lock.json
        rm -rf node_modules
        ```
    *   Install dependencies:
        ```bash
        npm install
        ```

7.  **Build Frontend Assets:**
    *   For development (unminified):
        ```bash
        npm run dev
        ```
    *   For production (minified):
        ```bash
        npm run build
        ```

8.  **Initialize the Database:**
    *   Ensure your `DATABASE_URL` in `.env` is correctly configured and the database server is running.
    *   Run the initialization command:
        ```bash
        flask init-db
        ```
    *   This command will create the necessary tables (e.g., the `users` table) based on the models defined in `app/models.py`.

9.  **Run the Development Server:**
    ```bash
    flask run
    ```
    The application should now be running at `http://127.0.0.1:5000`.

### Development Workflow

*   **Frontend Changes**: To automatically rebuild frontend assets (CSS, JS) as you make changes, run the Webpack watch command in a separate terminal:
    ```bash
    npm run watch
    ```
*   **Backend Changes**: The Flask development server (`flask run` with `FLASK_ENV=development`) will automatically reload when Python files change.
*   **Database Migrations**: Flask-Migrate is included but not fully initialized. To manage database schema changes, you would typically initialize it (`flask db init`), create migration scripts (`flask db migrate -m "Description"`), and apply them (`flask db upgrade`). This setup is left for the user to implement as needed.

## Project Structure

```
.
├── app/                    # Main application package
│   ├── __init__.py         # Application factory
│   ├── extensions.py       # Flask extension initializations
│   ├── models.py           # SQLAlchemy database models
│   ├── auth/               # Authentication blueprint
│   │   ├── __init__.py
│   │   ├── forms.py        # Login/Registration WTForms
│   │   └── routes.py       # Authentication routes (/login, /register, /logout)
│   ├── main/               # Main application blueprint
│   │   ├── __init__.py
│   │   └── routes.py       # Core application routes (e.g., home page)
│   ├── static/
│   │   ├── dist/           # Compiled CSS/JS assets (output from Webpack)
│   │   └── src/            # Source CSS/JS files
│   │       ├── css/
│   │       │   └── main.css # Main CSS entrypoint (includes Tailwind)
│   │       └── js/
│   │           └── main.js  # Main JS entrypoint (includes Alpine, HTMX)
│   └── templates/          # Jinja2 templates
│       ├── auth/           # Auth blueprint templates
│       │   ├── login.html
│       │   └── register.html
│       ├── base.html       # Base template with common structure
│       ├── index.html      # Home page template
│       └── _formhelpers.html # Template macro for rendering forms
├── migrations/             # Flask-Migrate migration scripts (if initialized)
├── tests/                  # Placeholder for tests
├── venv/                   # Python virtual environment (ignored by Git)
├── .env                    # Environment variables (DO NOT COMMIT)
├── .env.example            # Example environment variables
├── .flaskenv               # Defines FLASK_APP, FLASK_ENV
├── .gitignore              # Files/directories ignored by Git
├── config.py               # Configuration classes
├── package.json            # Node.js dependencies and scripts
├── package-lock.json       # Locked Node.js dependency versions
├── postcss.config.js       # PostCSS configuration (for Tailwind)
├── requirements.txt        # Python dependencies
├── run.py                  # Flask app entry point and CLI commands
├── tailwind.config.js      # Tailwind CSS configuration
└── webpack.config.js       # Webpack configuration
