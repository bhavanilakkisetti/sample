from flask_pymongo import PyMongo
import flask
from flask import *
app=flask.Flask(__name__)
mongodb_client=PyMongo(app,uri="mongodb://localhost:27017/Dataset2")
db=mongodb_client.db
@app.route('/')
#def add_one():
   # db.student.insert_one({"id":"503","name":"leela","branch":"cse"})
   # return flask.jsonify(message="success")
@app.route('/')
def index():
    return render_template('login.html')
@app.route('/success',methods=['POST','GET'])
def print_data():
   
    if request.method=='POST':
        result=request.form.get("name")
        s1="Subcode"
        s2="Subname"
        s3="Grade"
        s4="credits"
        

        tood=db.Result.find({'Htno':result})
        data=[]
        for doc in tood:
            
            doc['_id']=str(doc['_id'])
            data.append(doc)
        
        return render_template('result.html',data=data,d1=result,d2=s1,d3=s2,d4=s3,d5=s4)
if __name__=='__main__':
    app.run(debug=True)

