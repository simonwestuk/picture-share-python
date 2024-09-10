def test_config(test_client):
    response = test_client.get('/home')
    assert response.status_code == 200