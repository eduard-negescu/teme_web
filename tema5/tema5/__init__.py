from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
 
app = Flask(__name__)

app.config['SECRET_KEY'] = 'c9500956983293fe3b147068ea838031'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['WTF_CSRF_SECRET_KEY'] = '2a7146dfbce9c5b2029872a4baee766b'
app.app_context().push()

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'warning'

from podcast_app import routes