from flask import make_response, jsonify
from http import HTTPStatus


def make_json_response(data=None, status=True, errors=None):
    body = {
        'status': status
    }

    if data is not None:
        body['data'] = data

    if errors is not None:
        body['errors'] = errors

    response = make_response(jsonify(body), HTTPStatus.OK)

    response.headers['Content-Type'] = 'application/json'

    return response
