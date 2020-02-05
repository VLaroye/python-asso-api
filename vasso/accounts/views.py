from flask import jsonify, request, current_app, abort
from psycopg2.errors import UniqueViolation, NotNullViolation
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from vasso.utils.make_json_response import make_json_response
from vasso import db
from vasso.accounts.adapters import AccountAdapter
from vasso.accounts import accounts
from vasso.accounts.models import AccountSchema
from vasso.auth.models import User, UserSchema

account_schema = AccountSchema()
user_schema = UserSchema()

AccountAdapter()


@accounts.route('', methods=['GET'])
def list_accounts():
    accounts_list = AccountAdapter.get_list()

    data = account_schema.dump(accounts_list, many=True)

    return make_json_response(data)


@accounts.route('', methods=['POST'])
def create_account():
    data = request.json

    try:
        account = AccountAdapter.validate(data)

        db.session.add(account)
        db.session.commit()

        return make_json_response(data=account_schema.dump(account))
    except ValidationError as err:
        return make_json_response(status=False, errors=err.messages)
    except IntegrityError as err:
        current_app.logger.error(err)
        db.session.rollback()

        if isinstance(err.orig, UniqueViolation):
            return make_json_response(status=False, errors={'name': 'Account with this name already exists'})

        return make_json_response(status=False, errors={'error': 'Error adding new account to database'})


@accounts.route('/<account_id>', methods=['GET'])
def get_account(account_id):
    account = AccountAdapter.get_by_id(account_id)

    if account is None:
        return make_json_response(status=False, errors={'Not found': 'Account not found'})

    return make_json_response(data=account_schema.dump(account))


@accounts.route('/<account_id>', methods=['POST', 'PUT'])
def update_account(account_id):
    return 'Get account'


@accounts.route('/<account_id>', methods=['DELETE'])
def delete_account(account_id):
    account = AccountAdapter.get_by_id(account_id)

    if account is None:
        return make_json_response(status=False, errors={'Not found': 'Account not found'})

    AccountAdapter.delete(account)

    return make_json_response()
