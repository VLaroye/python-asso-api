from flask import jsonify
from vasso.accounts import accounts
from vasso.accounts.models import Account


@accounts.route('/', methods=['GET'])
def list_accounts():
    accounts_list = Account.query.all()

    return jsonify({'status': True, 'data': accounts_list})


@accounts.route('/', methods=['POST'])
def create_account():
    return 'Create account'


@accounts.route('/<account_name>', methods=['GET'])
def get_account(account_name):
    return 'Get account'


@accounts.route('/<account_name>', methods=['POST', 'PUT'])
def update_account(account_name):
    return 'Get account'


@accounts.route('/<account_name>', methods=['DELETE'])
def delete_account(account_name):
    return 'Delete account'
