from flask import jsonify
from flask import request
from flask import Flask
from MySQLCommand import MySQLCommand

app=Flask(__name__)

@app.route('/student',methods=['POST'])
def add_student():
    #{"id":1,"name":"wcg","age":18,"grade":12}
    #student={
    #    'id':request.json['id'],
    #    'name':request.json['name'],
    #    'age':request.json['age'],
    #    'grade':request.json['grade'],
    #    }
    student={
        'id':request.args['id'],
        'name':request.args['name'],
        'age':request.args['age'],
        'grade':request.args['grade'],
        }
    mysql=MySQLCommand("localhost",3306,"root","wch1132","chris_wang","student")
    mysql.connectMysql()
    mysql.insertMysql(request.args['name'],request.args['age'],request.args['grade'])
    re=mysql.queryMysqlById(request.args['id'])
    mysql.closeMysql()
    return re[1]+"_"+str(re[2]) if len(re) else "null"

app.run(debug=False)