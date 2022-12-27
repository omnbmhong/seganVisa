from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask import jsonify
from . import db
from .models import User, Articles
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_marshmallow import Marshmallow

auth = Blueprint("auth", __name__)

ma = Marshmallow(auth)
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'email', 'username', 'password','date_created')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class ArticleSchema(ma.Schema):
    class Meta:
        fields = ('id', 'country', 'order_type','dp_date','arr_date','body', 'date')
        
article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


@auth.route("/login", methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")
        
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Password is incorrect.', category='error')
        else:
            flash('Email does not exist.', category='error')
            
    return render_template("login.html")
#  login design for Vue frontend
@auth.route("/vuelogin", methods=['GET','POST'])
def veu_login():
    if request.method == 'POST':
        phone = request.json['phone']
        password = request.json['password']
        user = User.query.filter_by(username=phone).first()
        match_user = User(email='null', username='null', password='null')
        flag={'id':'9','status':"Failure",'username':"None"}

        if user:
            if check_password_hash(user.password, password):
                match_user = User(email='OK', username=phone, password=generate_password_hash(password, method='sha256'))
                flash("Logged in!", category='success')
                login_user(user, remember=True)
                name=user.username
                flag={'id':'8','status':"Success",'username':name}
                print('Login Success',"by User ",name)
                return jsonify(flag)
            else:
                flash('Password is incorrect.', category='error')
                print('Password is incorrect.')
        else:
            flash('Email does not exist.', category='error')
            print('Phone Number does not exist.')
            
    return jsonify(flag)


@auth.route("/sign-up", methods=['GET','POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get("email")
        username = request.form.get("username")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        email_exists = User.query.filter_by(email=email).first()
        username_exists = User.query.filter_by(username=username).first()

        if email_exists:
            flash('Email is already in use.', category='error')
        elif username_exists:
            flash('Username is already in use.', category='error')
        elif password1 != password2:
            flash('Password don\'t match!', category='error')
        elif len(username) < 2:
            flash('Username is too short.', category='error')
        elif len(password1) < 5:
            flash('Password is too short.', category='error')
        elif len(email) < 4:
            flash("Email is too short invalid.", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('User created!')
            return redirect(url_for('views.home'))
        
    return render_template("signup.html")


@auth.route("/logout")
def logout():
    return redirect(url_for("views.home"))

@auth.route("/vuelogout")
def vue_logout():
    return redirect(url_for("views.home"))

@auth.route('/register', methods=['POST','GET'])
def register_user():
    if request.method == 'POST':
        email = request.json['email']
        username = request.json['first_name']+request.json['last_name']
        password1 = request.json['password']
        password2 = request.json['password_confirm']
        new_user = User(email=email, username=username, password=generate_password_hash(
                password1, method='sha256'))
        print("register info=",new_user)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user, remember=True)
        flash('User created!')
        return user_schema.jsonify(new_user)
    
@auth.route('/get', methods=['GET'])
def get_articles():
    all_articles = Articles.query.all()
    results = articles_schema.dump(all_articles)
    return jsonify(results)

@auth.route('/add', methods=['POST'])
def add_article():
    country = request.json['country']
    dp_date = request.json['dp_date']
    arr_date = request.json['arr_date']
    order_type = request.json['order_type']
    body = request.json['body']
    articles = Articles(country=country,order_type=order_type,dp_date=dp_date,arr_date=arr_date,body=body)
    db.session.add(articles)
    db.session.commit()
    return article_schema.jsonify(articles)

@auth.route('/get/<id>/', methods=['GET'])
def post_details(id):
    article = Articles.query.get(id)
    return article_schema.jsonify(article)

@auth.route('/update/<id>/', methods=['PUT'])
def update_article(id):
    article = Articles.query.get(id)
    country = request.json['country']
    body = request.json['body']
    article.country = country
    article.body = body
    db.session.commit()
    return article_schema.jsonify(article)

@auth.route('/delete/<id>/', methods=['DELETE'])
def article_delete(id):
    article = Articles.query.get(id)
    db.session.delete(article)
    db.session.commit()
    return article_schema.jsonify(article)
