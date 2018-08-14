from flask import Flask
from flask_restful import Api
import api_resource

app = Flask(__name__)
api = Api(app)
api.add_resource(api_resource.People, '/people')
api.add_resource(api_resource.UpdateStatus, '/updatestatus/id/<id>/survived/<status>')
api.add_resource(api_resource.DeletePeople, '/delete/<id>')
api.add_resource(api_resource.InsertPerson,
                 "/insert/survived/<status>/pclass/<pclass>/fname/<fname>/sname/" +
                 "<sname>/sex/<sex>/age/<age>/ssa/<ssa>/pca/<pca>/fare/<fare>")

if __name__ == '__main__':
    app.run(port='5002')
