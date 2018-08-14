from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2 as dbapi2
from sqlalchemy import create_engine

db_connect = create_engine("postgresql://postgres:mysecretpassword@localhost/titanic")
app = Flask(__name__)
api = Api(app)


class People(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(
            "select id, survived,pclass,name,sex,age,siblings_spouses_aboard,parents_children_aboard, fare from people")
        return {'people': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}


class Update_Status(Resource):
    def get(self, id, status):
        if int(status) == 1:
            new_status = 'TRUE'
        elif int(status) == 0:
            new_status = 'FALSE'
        else:
            return {'message': 'wrong status'}

        conn = db_connect.connect()
        conn.execute("update people set survived = %s where id = %d" % (new_status, int(id)))
        return {'message': 'done'}


class Delete_People(Resource):
    def get(self, id):

        conn = db_connect.connect()
        conn.execute("delete from people where id = %d" % (int(id)))
        return {'message': 'done'}


class Insert_Person(Resource):
    def get(self, status, pclass, fname, sname, sex, age, ssa, pca, fare):

        if int(status) == 1:
            new_status = 'TRUE'
        elif int(status) == 0:
            new_status = 'FALSE'
        else:
            return {'message': 'wrong status'}

        full_name = fname + " " + sname
        conn = db_connect.connect()
        conn.execute(
            "insert into people (survived,pclass,name,sex,age,siblings_spouses_aboard,parents_children_aboard, fare) "
            "values (%s, %s, \'%s\', \'%s\', %s, %s, %s, %s)" % (new_status, pclass, full_name, sex, age, ssa, pca, fare))
        return {'message': 'done'}


api.add_resource(People, '/people')
api.add_resource(Update_Status, '/updatestatus/id/<id>/survived/<status>')
api.add_resource(Delete_People, '/delete/<id>')
api.add_resource(Insert_Person,
                 '/insert/survived/<status>/pclass/<pclass>/fname/<fname>/sname/<sname>/sex/<sex>/age/<age>/ssa/<ssa>/pca/<pca>/fare/<fare>')

if __name__ == '__main__':
    db = dbapi2.connect(database="titanic", user="postgres", host='localhost', password="mysecretpassword")
    app.run(port='5002')
