from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    date_created = db.Column(db.DateTime(timezone=True), default=func.now())
    
class Articles(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(50))
    order_type= db.Column(db.String(50))
    dp_date = db.Column(db.String(50))
    arr_date = db.Column(db.String(50))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default=datetime.datetime.now)
    deliver_date=db.Column(db.DateTime, default=(datetime.datetime.now()+datetime.timedelta(days=1)))
    cxl_date=db.Column(db.DateTime)
    status=db.Column(db.String(30))
    op_code=db.Column(db.Text())