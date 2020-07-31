from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:gopalg0pal@localhost/news_curator'
db = SQLAlchemy(app)

from app import routes