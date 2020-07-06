
from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
import pymysql
import config

databaseurl =  'mysql+pymysql://%s:%s@%s:%s/%s' % (config.MYSQL_USER, config.MYSQL_PASS, config.MYSQL_HOST, config.MYSQL_PORT, config.MYSQL_DB)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = databaseurl
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
db = SQLAlchemy(app)

class student(db.Model):
    __tablename__='student2'

    id=db.Column(db.Integer,primary_key=True,nullabel=False)
    name=db.Column(db.String(20),nullable=False)
    age=db.column(db.Integer,nullable=False)

    def __init__(self,id,name,age):
        self.id=id
        self.name=name
        self.age=age

    def __repr__(self):
        return ''%(self.id,self.name)

db.create_all()

@app.route('/', methods=['POST'])
def hello():
    if not request.json:
        return "failed!", 400
    student = {
        'id': request.args['id'],
        'name': request.args['name'],
        'age': request.args['age']
    }
    #初始化student对象
    stu = mytable(int(student['id']), student['name'], int(student['age']))
    #将新增项目插入数据库
    db.session.add(stu)
    #提交修改
    db.session.commit()
    return "Hello World!"
 
@app.route('/', methods=['GET'])
def get_one():
    if not request.args['id']:
        abort(400)
    get_id = request.args['id']
    #得到表中所有的数据
    ids = mytable.query.all()
    #使用filter找到指定项目
    get = mytable.query.filter_by(id = get_id).first()
    #获取表成员属性
    ret = 'id=%d,name=%s,age=%d' % (get.id, get.name, get.age)
    return ret
 
app.run(debug = False)