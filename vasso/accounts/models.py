from vasso import db
from vasso.base_model import Base


class Account(Base):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship('User', backref=db.backref('accounts', lazy=True))

    def __repr__(self):
        return f'<Post {self.name}>'