from app import create_app, db
from app.models import User
from flask_bcrypt import generate_password_hash

app = create_app()

with app.app_context():
    # Create the database and tables
    db.create_all()
    
    # Check if the admin user already exists
    admin = User.query.filter_by(email='admin@example.com').first()
    
    if admin is None:
        # Create an admin user
        admin = User(
            username='admin',
            email='admin@admin.com',
            password=generate_password_hash('password').decode('utf-8'),
            is_admin=True
        )
        db.session.add(admin)
        db.session.commit()
        print('Admin user created.')
    else:
        print('Admin user already exists.')
