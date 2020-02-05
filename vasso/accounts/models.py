from marshmallow import fields
from vasso import db, ma
from vasso.base_model import Base
from vasso.auth.models import UserSchema


class Account(Base):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'<Post {self.name}>'


class AccountSchema(ma.ModelSchema):
    class Meta:
        model = Account
        owner = fields.Nested(UserSchema, required=True)
