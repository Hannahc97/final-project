
from flask_sqlalchemy import SQLAlchemy
import os


uri = os.environ.get("DATABASE_URL")

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

DB = ""

class buildDb():
    db = False
    def build(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = uri
        self.db = SQLAlchemy(app)
        global DB
        DB = self.db
        return self.db

