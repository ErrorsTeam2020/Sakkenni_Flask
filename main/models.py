from main import db,login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    phone = db.Column(db.Integer, nullable=False)
    nat_id = db.Column(db.Integer, unique=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    address = db.Column(db.String(150), nullable=False)
    governorate = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    user_class = db.Column(db.String(100), nullable=False)
    gender = db.Column(db.String(100), nullable=False)
    flats = db.relationship('Flat', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.fullname}','{self.username}','{self.address}'" \
               f",'{self.governorate}','{self.email}','{self.password}','{self.user_class}','{self.gender}'" \
               f",{self.phone},{self.nat_id})"


class Flat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(150), nullable=False)
    description = db.Column(db.String(600), nullable=False)
    governorate = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    student_num = db.Column(db.Integer, nullable=False)
    room_num = db.Column(db.Integer, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Flat('{self.title}','{self.address}','{self.description}','{self.governorate}'," \
               f"{self.price},{self.student_num},{self.room_num})"
