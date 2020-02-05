import json
from http import HTTPStatus


def test_list_accounts(client, db):
    """
    GIVEN a Flask application
    WHEN the '/accounts' is requested (GET)
    THEN check the response is valid
    """
    response = client.get('/accounts')

    data = json.loads(response.data.decode())

    account = data['data'][0]
    status = data['status']

    assert response.status_code == HTTPStatus.OK
    assert status
    assert account['name'] == 'Account 1'
    assert account['id'] == 1
    assert account['owner'] == 1


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

    assert response.status_code == HTTPStatus.OK
    assert status
    assert account['name'] == 'Account 1'
    assert account['id'] == 1
    assert account['owner'] == 1

    # Check response when accounts doesn't exists
    response = client.get('/accounts/4')

    data = json.loads(response.data.decode())

    errors = data['errors']
    status = data['status']

    assert response.status_code == HTTPStatus.OK
    assert not status
    assert len(errors) == 1
    assert errors['Not found'] == 'Account not found'


def test_create_account(client, db):
    """
    GIVEN a Flask application
    WHEN the '/accounts' is required (POST)
    THEN check the response is valid
    """
    response = client.post('/accounts', json={'name': 'Account 5', 'owner': 1})

    data = json.loads(response.data.decode())

    status = data['status']
    account = data['data']

    assert response.status_code == HTTPStatus.OK
    assert status
    assert account['id'] == 2
    assert account['name'] == 'Account 5'
    assert account['owner'] == 1

    """Check response when trying to create an account which name is already taken"""
    response = client.post('/accounts', json={'name': 'Account 1', 'owner': 1})

    data = json.loads(response.data.decode())

    status = data['status']
    errors = data['errors']

    assert response.status_code == HTTPStatus.OK
    assert not status
    assert errors.get('name')

    """Check response when trying to create an account without a 'name' field"""
    response = client.post('/accounts', json={'owner': 1})

    data = json.loads(response.data.decode())

    status = data['status']
    errors = data['errors']

    assert response.status_code == HTTPStatus.OK
    assert not status
    assert errors['name']

    """Check response when trying to create an account without a 'owner' field"""
    response = client.post('/accounts', json={'name': 'Account 3'})

    data = json.loads(response.data.decode())

    status = data['status']
    errors = data['errors']

    assert response.status_code == HTTPStatus.OK
    assert not status
    assert errors['owner']


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

    assert response.status_code == HTTPStatus.NOT_FOUND
