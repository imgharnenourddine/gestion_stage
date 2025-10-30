from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='e861d5ca3a8eee5ac533994b07c0f983c6cdb33ba3fc6eccb09c12a683b8ac36'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:noureddine188@localhost:5432/gestion_projet'
db=SQLAlchemy(app)
from package import models
from package import routes
