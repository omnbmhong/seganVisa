from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import create_engine

from os import path
from flask_login import LoginManager
from flask_cors import CORS

db = SQLAlchemy()
DB_NAME = "segantravel.db"


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SECRET_KEY'] = "mmtek"
    # app.config['SQL_ALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:omnbmh801206@localhost:3306/segantravel'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")
    
    from .models import User, Articles

    
    engine = create_engine('mysql+pymysql://root:omnbmh801206@localhost:3306/{}'.format("segantravel"),encoding='utf8')
    if table_exists(engine, "articles"):
        print("已存在，无需新建Orders Table")
    else:
        print("新建表单Orders")
        create_database(app)
        
    if table_exists(engine, "user"):
        print("已存在，无需新建User Table")
    else:
        print("新建表单User")
        create_database(app)
    
    login_manager = LoginManager()
    login_manager.login_view = "auth.login"
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def table_exists(engine, table_name):
    with engine.connect() as con:
        sql="show tables;"
        tables = con.execute(sql).fetchall()
        for table_col in tables:
            if table_name == table_col[0]:
                return True 
        return False
    
def create_database(app):
    db.create_all(app=app)
    print("Created database!Success")