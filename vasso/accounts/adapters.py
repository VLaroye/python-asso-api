from marshmallow import ValidationError
from vasso import db
from vasso.accounts.models import Account, AccountSchema
from vasso.auth.models import User, UserSchema

account_schema = AccountSchema()
user_schema = UserSchema()


class AccountAdapter:
    @staticmethod
    def get_by_id(account_id):
        return Account.query.get(account_id)

    @staticmethod
    def get_list():
        return Account.query.all()

    @staticmethod
    def delete(account):
        db.session.delete(account)
        db.session.commit()

    @staticmethod
    def validate(account):
        owner_id = account.get('owner_id')

        if owner_id is None:
            raise ValidationError({'owner_id': ['Field may not be null.']})

        try:
            owner_id = int(owner_id)
        except ValueError:
            raise ValidationError({'owner_id': ['Must be an int.']})

        owner = User.query.get(owner_id)

        if owner is None:
            raise ValidationError({'owner': ["Can't find this user."]})

        account_dict = {
            'name': account.get('name'),
            'owner': user_schema.dump(owner)
        }

        # Converts data dictionary to Account object + Validates fields
        account = account_schema.load(account_dict, session=db.session)

        return account
