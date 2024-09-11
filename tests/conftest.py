import pytest
from app import create_app, db

# Create the Flask app fixture
@pytest.fixture(scope='module')
def app():
    # Create an instance of the Flask app
    flask_app = create_app()

    # Set the app to testing mode
    flask_app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:",  # In-memory database for testing
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    yield flask_app  # Yield the app for the test

# Create the test client fixture that depends on the app fixture
@pytest.fixture(scope='module')
def test_client(app):
    # Create a test client using the Flask app instance
    testing_client = app.test_client()

    # Establish an application context before running the tests
    with app.app_context():
        yield testing_client  # This is where the testing happens!

# Create the init_database fixture that also depends on the app fixture
@pytest.fixture(scope='module')
def init_database(app):
    # Create the database and the tables
    with app.app_context():
        db.create_all()

        yield db  # This is where the testing happens!

        # Drop the database and the tables
        db.drop_all()
