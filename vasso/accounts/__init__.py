from flask import Blueprint
from .models import Account

accounts = Blueprint(
    'accounts',
    __name__,
    url_prefix='/accounts'
)

from .views import list_accounts,\
    create_account,\
    get_account,\
    update_account,\
    delete_account
