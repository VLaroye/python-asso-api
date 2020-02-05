from marshmallow import fields
from vasso import db, ma
from vasso.base_model import Base


class User(Base):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    accounts = db.relationship('Account', backref='owner', lazy=True)

    def __repr__(self):
        return f'<User {self.username}>'


class UserSchema(ma.ModelSchema):
    class Meta:
        fields = ('id', 'username', 'email')

