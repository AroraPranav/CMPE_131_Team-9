from ctypes import addressof
from market import db, login_manager
from market import bcrypt
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)
    items = db.relationship('Item', backref='owned_user', lazy=True)

    firstName = db.Column(db.String(length=30), nullable=False)
    lastName = db.Column(db.String(length=30), nullable=False)
    rating = db.Column(db.Integer())

    @property
    def prettier_budget(self):
        if len(str(self.budget)) >= 4:
            return f'{str(self.budget)[:-3]},{str(self.budget)[-3:]}$'
        else:
            return f"{self.budget}$"

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def can_purchase(self, item_obj):
        return self.budget >= item_obj.price

    def can_sell(self, item_obj):
        return item_obj in self.items


class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    price = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(length=1024))
    owner = db.Column(db.Integer(), db.ForeignKey('user.id'))
    address = db.Column(db.String(length=50), nullable=False)
    city = db.Column(db.String(length=30), nullable=False)
    zip = db.Column(db.String(length=30), nullable=False)
    bed = db.Column(db.Integer(), nullable=False)
    bath = db.Column(db.Integer(), nullable=False)
    rural = db.Column(db.Boolean(), default = False)
    suburban = db.Column(db.Boolean(), default = False)
    urban = db.Column(db.Boolean(), default = False)
    apartment = db.Column(db.Boolean(), default = False)
    house = db.Column(db.Boolean(), default = False)
    condo = db.Column(db.Boolean(), default = False)
    picdata = db.Column(db.LargeBinary) #Actual data, needed for Download
    rendered_picdata = db.Column(db.Text)#Data to render the pic in browser

    def __repr__(self):
        return f'[PROPERTY {self.id}]: Price:{self.price}, Description:{self.description}, Owner:{self.owner}, Address:{self.address}, City:{self.city}, Zipcode:{self.zip}, Bed:{self.bed}, Bath:{self.bath}'

    def buy(self, user):
        self.owner = user.id
        user.budget -= self.price
        db.session.commit()

    def sell(self, user):
        self.owner = None
        user.budget += self.price
        db.session.commit()