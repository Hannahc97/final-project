
from flask_sqlalchemy import SQLAlchemy
uri = 'postgres://u6ra4mnc747cdk:p3b20e55cd87aab70dce4ae71024e1cea7feb1255d4b803a5737e514f68b12d5d@c9tiftt16dc3eo.cluster-czz5s0kz4scl.eu-west-1.rds.amazonaws.com:5432/dfe0sk8mnmgjpp'

if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

DB = ""

class buildDb():
    db = False
    def build(self, app):
        db = SQLAlchemy(app)
    
    def getDb(self):
        global DB
        DB = self.db
        return self.db
