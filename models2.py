from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class OneTb(db.Model):
    __tablename__ = 'oneTb'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(200))
    salary = db.Column(db.Integer)

    def get_field_names():
        oneTb_fields = [column.key for column in OneTb.__table__.columns]
        return oneTb_fields



class NTb(db.Model):
    __tablename__ = 'nTb'
    id = db.Column(db.Integer, primary_key=True)
    one_id = db.Column(db.Integer, db.ForeignKey('oneTb.id'))
    value = db.Column(db.String(100))
    price = db.Column(db.Integer)

    def get_field_names():
        nTb_fields = [column.key for column in NTb.__table__.columns]
        return nTb_fields
 
    #one = db.relationship('oneTb', backref=db.backref('nTb', lazy=True))


# Beispiel zur Verwendung der Funktion
if __name__ == '__main__': 

     
    OneTbFieldNames = OneTb.get_field_names() 
    print ('OneTbFieldNames') 
    print (OneTbFieldNames) 


    NTbFieldNames = NTb.get_field_names() 
    print ('NTbFieldNames') 
    print (NTbFieldNames)

