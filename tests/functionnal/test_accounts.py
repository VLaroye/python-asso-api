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

