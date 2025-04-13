import os
import click
from app import create_app, db
from app.models import User # We'll create models.py next

# Determine the configuration based on FLASK_CONFIG environment variable or default
config_name = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(config_name)

@app.shell_context_processor
def make_shell_context():
    """Creates a shell context that adds the database instance and models."""
    return dict(db=db, User=User)

@app.cli.command()
@click.option('--drop', is_flag=True, help='Create after drop.')
def init_db(drop):
    """Initialize the database."""
    if drop:
        click.confirm('This will delete the database tables. Do you want to continue?', abort=True)
        db.drop_all()
        click.echo('Dropped tables.')
    db.create_all()
    click.echo('Initialized the database.')
    # Optionally, create a default admin user here if needed
    # if User.query.filter_by(username='admin').first() is None:
    #     admin_user = User(username='admin', email='admin@example.com')
    #     admin_user.set_password('defaultpassword') # Change this!
    #     db.session.add(admin_user)
    #     db.session.commit()
    #     click.echo('Created admin user.')

if __name__ == '__main__':
    app.run()
