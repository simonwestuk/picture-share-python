def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    assert response.status_code == 200
    assert b"Welcome" in response.data
    
def test_register_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/register' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/register')
    assert response.status_code == 200
    assert b"Register" in response.data
