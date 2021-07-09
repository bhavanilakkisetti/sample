from flask_pymongo import PyMongo
import flask
from pymongo import MongoClient
from flask import *
app=flask.Flask(__name__)
mongodb_client=PyMongo(app,uri="mongodb://localhost:27017/Dataset3")
db=mongodb_client.db
print("connect")
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/success',methods=['POST','GET'])
def print_data():
    if request.method=='POST':
        radio=request.form.get("r1",False)
        select=request.form.get("s1")
        yoy=db.list_collection_names()
        print(yoy)
        print(radio)
        print(select)
        result1=request.form.get("name")
        print(result1)
        s1="Subcode"
        s2="Subname"
        s3="Grade"
        s4="credits"
        data=[]
        #1-1
        if radio=='results':
            tood=db[select].find({'Htno':result1})
            for doc in tood:
                doc['_id']=str(doc['_id'])
                data.append(doc)
        elif radio=='backlog':
            tood=db[select].find({'Htno':result1,"Credits":"0"})
            for doc in tood:
                doc['_id']=str(doc['_id'])
                data.append(doc)
    if not data:
        return render_template('zerobacklog.html')
    return render_template('res.html',data=data,d1=result1,d2=s1,d3=s2,d4=s3,d5=s4)
            
       
if __name__=='__main__':
    app.run(debug=True)


