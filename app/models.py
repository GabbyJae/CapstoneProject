from . import db
from werkzeug.security import generate_password_hash





class Users(db.Model):
    # You can use this to change the table name. The default convention is to use
    # the class name. In this case a class name of UserProfile would create a
    # user_profile (singular) table, but if we specify __tablename__ we can change it
    # to `user_profiles` or some other name.
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender=db.Column(db.String(80))
    email=db.Column(db.String(150))
    password = db.Column(db.String(255))

    def __init__(self, firstname, lastname,gender,email, password):
        self.firstname = firstname
        self.lastname = lastname
        self.gender=gender
        self.email=email
        self.password = generate_password_hash(password, method='pbkdf2:sha256')

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' %  self.email


class Reservations(db.Model):
    __tablename__ = 'Reservations'
    id = db.Column(db.Integer,primary_key = True)
    start_date = db.Column(db.String(255))
    start_time = db.Column(db.String(255))
    end_date = db.Column(db.String(255))
    end_time = db.Column(db.String(255))
    licenseplateno = db.Column(db.String(255))
    typeofparking = db.Column(db.String(255))

    def __init__(self,start_date, start_time, end_date, end_time, licenseplateno, typeofparking):
        self.start_date = start_date
        self.start_time = start_time
        self.end_date = end_date
        self.end_time = end_time
        self.typeofparking = typeofparking
        self.licenseplateno = licenseplateno

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)
        
    

class ParkingLots(db.Model):
    __tablename__ = 'Parking Lots'
    id = db.Column(db.Integer,primary_key = True)
    parkinglots = db.Column(db.String(255))
    numberofspaces = db.Column(db.Integer,)


    def __init__(self,parkinglots, numberofspaces):
        self.parkinglots = parkinglots
        self.numberofspaces = numberofspaces

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)
    
