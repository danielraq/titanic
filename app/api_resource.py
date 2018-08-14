from app import config
from flask_restful import Resource

db_connect = config.get_db_connect()


class People(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute(
            "select id, survived,pclass,name,sex,age,siblings_spouses_aboard,parents_children_aboard, fare from people")
        return {'people': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}


class UpdateStatus(Resource):
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


class DeletePeople(Resource):
    def get(self, id):
        conn = db_connect.connect()
        conn.execute("delete from people where id = %d" % (int(id)))
        return {'message': 'done'}


class InsertPerson(Resource):
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
            "values (%s, %s, \'%s\', \'%s\', %s, %s, %s, %s)" %
            (new_status, pclass, full_name, sex, age, ssa, pca, fare))
        return {'message': 'done'}
