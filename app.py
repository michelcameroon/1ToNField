from flask import Flask, render_template, request, redirect, url_for
#from models2 import db, OneTb, NTb, get_table_info
from models2 import db, OneTb, NTb


#from sqlalchemy import create_engine
#from sqlalchemy .orm import sessionmaker


app = Flask(__name__)

#engine = create_engine('sqlite:///your_database.db')
#Session = sessionmaker(bind=engine)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app3.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    tFieldNames = OneTb.get_field_names()
    print (tFieldNames)
    tFNoIds = []
    for tFieldName in tFieldNames:
        if tFieldName != 'id':
           tFNoIds.append(tFieldName)
    print ('tFNoIds')
    print (tFNoIds)



    ntFieldNames = NTb.get_field_names()
    print (ntFieldNames)
    ntFieldNamesNoIds = []
    for ntFieldName in ntFieldNames:
        if ntFieldName != 'id':
           ntFieldNamesNoIds.append(ntFieldName)
    print ('ntFieldNamesNoIds')
    print (ntFieldNamesNoIds)



    if request.method == 'POST':
        # Create a new 1Tb record
        table = OneTb.__tablename__
        data = {tFNoId: request.form[tFNoId] for tFNoId in tFNoIds}
        #insert_query = table.insert().values(**data)
        #insert_query = OneTb.insert().values(**data)
        new_record = OneTb(**data)
        db.session.add(new_record)
        '''
        db.session.execute(insert_query)

        name = request.form['name']
        new_record = OneTb(name=name)
        db.session.add(new_record)
        '''
        db.session.commit()

        #nrelations = NTb.query.all()
        #print ('nrelations')
        #print (nrelations)

        return redirect(url_for('index'))

    # Fetch all 1Tb records
    records = OneTb.query.all()

    ##nrelations = NTb.query.all()
    print ('records')
    print (records)
    #return render_template('index.html',records=records,nrelations=nrelations,tnFieldNamesNoIds=tnFieldNamesNoIds,ntFieldNamesNoIds=ntFieldNamesNoIds)

    #return render_template('index.html', records=records, tFieldNamesNoIds=tFieldNamesNoIds)
    return render_template('index.html', records=records, tFNoIds=tFNoIds)
    #return render_template('nrelations.html', nrelations=nrelations, ntFieldNamesNoIds=ntFieldNamesNoIds)




@app.route('/nrelations/<int:one_tb_id>', methods=['GET', 'POST'])
def nrelations(one_tb_id):
    fieldNames = NTb.get_field_names()
    print (fieldNames)
    fieldNamesNoIds = []
    for fieldName in fieldNames:
        if fieldName != 'id':
           fieldNamesNoIds.append(fieldName)
    print ('fieldNamesNoIds')
    print (fieldNamesNoIds)
    
    # list all relations 
    #nrelations = NTb.query.all()
    nrelations = NTb.query.filter(NTb.one_id == one_tb_id).all()
    #nrelations = NTb.query.all()
    print ('nrelations')
    print (nrelations)
    
    if request.method == 'POST':
        # Create a new nTb record
        data = {fieldNamesNoId: request.form[fieldNamesNoId] for fieldNamesNoId in fieldNamesNoIds}


        new_n_relation = NTb(**data)
        db.session.add(new_n_relation)

        db.session.commit()
        return redirect(url_for('index'))
     
    #table_info = get_table_info('nTb')
    #return render_template('nrelations.html', one_tb_id=one_tb_id, table_info=table_info, fieldNamesNoIds=fieldNamesNoIds )
    return render_template('nrelations.html', one_tb_id=one_tb_id, fieldNamesNoIds=fieldNamesNoIds, nrelations=nrelations )

    

if __name__ == '__main__':
    app.run(debug=True)
