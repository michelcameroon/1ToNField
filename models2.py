from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class OneTb(db.Model):
    __tablename__ = 'oneTb'
    id = db.Column(db.Integer, primary_key=True)
    # from here zou can change, add or remove te fieldNames you to have 
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(200))
    salary = db.Column(db.Integer)

    # this function  return all fieldNames of this table in an array
    def get_field_names():
        oneTb_fields = [column.key for column in OneTb.__table__.columns]
        return oneTb_fields



class NTb(db.Model):
    __tablename__ = 'nTb'
    id = db.Column(db.Integer, primary_key=True)
    one_id = db.Column(db.Integer, db.ForeignKey('oneTb.id'))
    # from here zou can change, add or remove te fieldNames you to have 
    value = db.Column(db.String(100))
    price = db.Column(db.Integer)

    # this function  return all fieldNames of this table in an array
    def get_field_names():
        nTb_fields = [column.key for column in NTb.__table__.columns]
        return nTb_fields
 


# example how to use this function

if __name__ == '__main__': 

    # it list all th fieldNames of OneTb       
    OneTbFieldNames = OneTb.get_field_names() 
    print ('OneTbFieldNames') 
    print (OneTbFieldNames) 

    # it list all th fieldNames of NTb       
    NTbFieldNames = NTb.get_field_names() 
    print ('NTbFieldNames') 
    print (NTbFieldNames)

