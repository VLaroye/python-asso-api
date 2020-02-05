from flask import Blueprint, json
from werkzeug.exceptions import HTTPException

errors = Blueprint(
    'errors',
    __name__
)


@errors.app_errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP Errors"""
    response = e.get_response()

    response.data = json.dumps({
        'code': e.code,
        'name': e.name,
        'message': e.description,
        'status': False,
    })

    response.content_type = 'application/json'

    return response
