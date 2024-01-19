from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'c9500956983293fe3b147068ea838031'
app.config['WTF_CSRF_SECRET_KEY'] = '2a7146dfbce9c5b2029872a4baee766b'
app.app_context().push()



from validare_formular import routes