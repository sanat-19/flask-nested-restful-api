from flask import Flask
from flask_migrate import Migrate
from new_models import db
from schema import *
from flask_restful import Api
from restful import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:solitaire@localhost:5432/final_task' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
db.init_app(app)
migrate = Migrate(app, db)


@app.before_first_request
def createTable():
    db.create_all()

#################RESTFUL#############################
api.add_resource(singleUser,'/api/user/<id>/')
api.add_resource(UserList,'/api/user/')

api.add_resource(AddressList,'/api/address/')
api.add_resource(singleAddress,'/api/address/<id>/')

api.add_resource(CompanyList,'/api/company/')
api.add_resource(singleCompany,'/api/company/<id>/')

api.add_resource(GeoList,'/api/geo/')
api.add_resource(singleGeo,'/api/geo/<id>/')

if __name__ == '__main__':
    app.run(debug=True)
