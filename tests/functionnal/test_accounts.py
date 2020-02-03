def test_list_accounts(client, db):
    """
    GIVEN a Flask application
    WHEN the '/accounts' is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/accounts/')

    print(response)
    assert response.status_code == 200

