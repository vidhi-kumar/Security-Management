from datetime import datetime
from security import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), nullable=False) #  unique=True this was removed
    password = db.Column(db.String(60), nullable=False)  
    type_force = db.Column(db.String(20), nullable=False)
    units =  db.Column(db.String(20), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
   

    def __repr__(self): # to display data
        return f"User('{ self.username }', '{ self.email }', '{ self.type_force }', '{ self.units }',{ self.password })"
                       
                
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    typ = db.Column(db.String(100), nullable=False) 
    required_units = db.Column(db.Integer, nullable=False)
    # date_requested = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    def __repr__(self): # to display data
       return f"Post('{ self.typ }','{ self.required_units }', '{ self.date_requested }')"
        # return f"User('{ self.username }','{ self.email }')"

