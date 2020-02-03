from flask import jsonify, request, abort, current_app
from http import HTTPStatus
from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError
from vasso import db
from vasso.accounts import accounts
from vasso.accounts.models import Account, AccountSchema

account_schema = AccountSchema()


@accounts.route('', methods=['GET'])
def list_accounts():
    accounts_list = Account.query.all()

    return jsonify({'status': True, 'data': account_schema.dump(accounts_list, many=True)})


@accounts.route('', methods=['POST'])
def create_account():
    print(request.json)
    data = request.json
    try:
        account = account_schema.load(data, session=db.session)

        db.session.add(account)
        db.session.commit()

        return jsonify({'status': True})
    except ValidationError as err:
        abort(HTTPStatus.BAD_REQUEST, 'Invalid account')
    except IntegrityError as err:
        current_app.logger.error(err)
        db.session.rollback()
        return jsonify({'status': False, 'data': 'Account with this name already exists'})


@accounts.route('/<account_id>', methods=['GET'])
def get_account(account_id):
    account = Account.query.get_or_404(account_id)

    return jsonify({'status': True, 'data': account_schema.dump(account)})


@accounts.route('/<account_id>', methods=['POST', 'PUT'])
def update_account(account_id):
    return 'Get account'


@accounts.route('/<account_id>', methods=['DELETE'])
def delete_account(account_id):
    account = Account.query.filter_by(id=account_id).first_or_404()

    db.session.delete(account)
    db.session.commit()

    return jsonify({'status': True})
