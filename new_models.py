from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Geos(db.Model):
    __tablename__ = "geos"
    id = db.Column(db.Integer, primary_key=True)
    lat = db.Column(db.String(20))
    lng = db.Column(db.String(20))

    address = db.Column(db.Integer, db.ForeignKey('addresses.id'), unique=True)
    

class Addresses(db.Model):
    __tablename__ = 'addresses'
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(20))
    suite = db.Column(db.String(20))
    city = db.Column(db.String(20))
    zipcode = db.Column(db.String(20))

    geo = db.relationship('Geos', backref='geo', uselist = False)
    user = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True)


class Companies(db.Model):
    __tablename__ = 'companies'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    catchPhrase = db.Column(db.String(20))
    bs = db.Column(db.String(20))

    user = db.Column(db.Integer, db.ForeignKey('users.id'),unique=True)

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    username = db.Column(db.String(30),unique=True) 
    email = db.Column(db.String(30),unique=True)
    phone = db.Column(db.String(30), unique=True)
    website = db.Column(db.String(30))


    address = db.relationship('Addresses', backref='address', uselist = False)
    company = db.relationship('Companies', backref='company', uselist = False)


