import json


def test_list_accounts(client, db):
    """
    GIVEN a Flask application
    WHEN the '/accounts' is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/accounts/')

    data = json.loads(response.data.decode())

    account = data['data'][0]
    status = data['status']

    assert response.status_code == 200
    assert status
    assert account['name'] == 'Account 1'
    assert account['id'] == 1
    assert account['creator'] == 1


def test_get_account(client, db):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<account_id>' is request (GET)
    THEN check the response is valid
    """
    response = client.get('/accounts/1')

    data = json.loads(response.data.decode())

    account = data['data']
    status = data['status']

    assert response.status_code == 200
    assert status
    assert account['name'] == 'Account 1'
    assert account['id'] == 1
    assert account['creator'] == 1

    # Check response when accounts doesn't exists
    response = client.get('/accounts/4')

    assert response.status_code == 404


def test_delete_account(client, db):
    """
    GIVEN a Flask application
    WHEN the '/accounts/<account_id>' is requested (DELETE)
    THEN check the response is valid
    """
    response = client.delete('/accounts/1')

    data = json.loads(response.data.decode())

    status = data['status']

    assert status

    # Check response when doesn't exists
    response = client.delete('/accounts/4')

    assert response.status_code == 404
