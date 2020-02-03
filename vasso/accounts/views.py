from flask import jsonify
from vasso import db
from vasso.accounts import accounts
from vasso.accounts.models import Account, AccountSchema

account_schema = AccountSchema()


@accounts.route('/', methods=['GET'])
def list_accounts():
    accounts_list = Account.query.all()

    return jsonify({'status': True, 'data': account_schema.dump(accounts_list, many=True)})


@accounts.route('/', methods=['POST'])
def create_account():
    return 'Create account'


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
