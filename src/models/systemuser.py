from db import db


class SystemUserModel(db.Model):
    __tablename__ = 'systemusers'

    id = db.Column(db.String(80), primary_key=True)
    account_locked = db.Column(db.String(80))
    activated = db.Column(db.String(80))
    email = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    suspended = db.Column(db.String(80))
    username = db.Column(db.String(80))

    def __init__(self, user):
        self.id = user.get("_id")
        self.account_locked = user.get("account_locked")
        self.activated = user.get("activated")
        self.email = user.get("email")
        self.firstname = user.get("firstname")
        self.lastname = user.get("lastname")
        self.suspended = user.get("suspended")
        self.username = user.get("username")

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'account_locked': self.account_locked,
            'activated': self.activated,
            'email': self.email,
            'firstname': self.firstname,
            'lastname': self.lastname,
            'suspended': self.suspended,
            'username': self.username,
        }

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
