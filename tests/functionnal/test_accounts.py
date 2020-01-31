from tests.configure_test import test_client, init_database


def test_list_accounts(test_client, init_database):
    """
    GIVEN a Flask application
    WHEN the '/accounts' is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/accounts/')

    assert response.status_code == 200
