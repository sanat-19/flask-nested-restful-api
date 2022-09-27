from flask_restful import  Resource
from new_models import *
from flask import jsonify, request
from marshmallow import validate
from schema import *
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')

user_schema = UserSchema()

address_schema = AddressSchema()

company_schema = CompanySchema()

geo_schema = GeoSchema()

##########################ADDRESS###########################

class AddressList(Resource):
    def get(self):
        address = Addresses.query.order_by(Addresses.id.asc())
        try:
            address_json = [address_schema.dump(address) for address in address]
        except:
            logger.warning("There was problem in retrieving data")
        return jsonify(address_json)

    def post(self):
        data = request.get_json()
        address = Addresses(street=data['street'],suite=data['suite'],city=data['city'],zipcode=data['zipcode'], user=data['user'])
        try:
            db.session.add(address)
            db.session.commit()
        except:
            logger.warning("There was problem in creating data")
        res = address_schema.dump(address)
        return jsonify(res)

class singleAddress(Resource):
    def get(self, id):
        address = Addresses.query.get(id)
        address_json = address_schema.dump(address)
        return jsonify(address_json)

    def put(self, id):
        data = request.get_json()
        address = Addresses.query.get(id)
        address.street = data['street']
        address.suite = data['suite']
        address.city = data['city']
        address.zipcode = data['zipcode']
        address.user = data['user']
        db.session.commit()
        res = address_schema.dump(address)
        return jsonify(res)
    
    def delete(self, id):
        address = Addresses.query.get(id)
        db.session.delete(address)
        db.session.commit()
        res = address_schema.dump(address)
        return jsonify(res)


   

##########################USER############################

class UserList(Resource):
    def get(self):
        user = Users.query.order_by(Users.id.asc())
        user_json = [user_schema.dump(user) for user in user]
        return jsonify(user_json)

    def post(self):
        error = user_schema.validate(request.json)
        if error:
            return error, 422
        data = request.get_json()
        user = Users(name=data['name'],username=data['username'],email=data['email'],phone=data['phone'],website=data['website'])
        try:
            db.session.add(user)
            db.session.commit()
        except:
            logger.warning("There was problem in creating data")
        res = user_schema.dump(user)
        return jsonify(res)
        

class singleUser(Resource):
    def get(self, id):
        user = Users.query.get(id)
        user_json = user_schema.dump(user)
        return jsonify(user_json)

    def put(self, id):
        error = user_schema.validate(request.json)
        if error:
            return error, 422
        data = request.get_json()
        user = Users.query.get(id)
        user.name = data['name']
        user.username = data['username']
        user.email = data['email']
        user.phone = data['phone']
        user.website = data['website']
        db.session.commit()
        res = user_schema.dump(user)
        return jsonify(res)

    def delete(self, id):
        user = Users.query.get(id)
        db.session.delete(user)
        db.session.commit()
        res = user_schema.dump(user)
        return jsonify(res)


###################COMPANY############################

class CompanyList(Resource):
    def get(self):
        company = Companies.query.order_by(Companies.id.asc())
        company_json = [company_schema.dump(company) for company in company]
        return jsonify(company_json)

    def post(self):
        data = request.get_json()
        company = Companies(name=data['name'],catchPhrase=data['catchPhrase'],bs=data['bs'], user=data['user'])
        try:
            db.session.add(company)
            db.session.commit()
        except:
            logger.warning("There was problem in creating data")

        res = company_schema.dump(company)
        return jsonify(res)

class singleCompany(Resource):
    def get(self, id):
        company = Companies.query.get(id)
        company_json = company_schema.dump(company) 
        return jsonify(company_json)

    def put(self, id):
        data = request.get_json()
        company = Companies.query.get(id)
        company.name = data['name']
        company.catchPhrase = data['catchPhrase']
        company.bs = data['bs']
        company.user = data['user']
        db.session.commit()
        res = company_schema.dump(company)
        return jsonify(res)

    def delete(self, id):
        company = Companies.query.get(id)
        db.session.commit()
        res = company_schema.dump(company)
        return jsonify(res)


######################GEO#####################


class GeoList(Resource):
    def get(self):
        geo = Geos.query.order_by(Geos.id.asc())
        geo_json = [geo_schema.dump(geo) for geo in geo]
        return jsonify(geo_json)

    def post(self):
        data = request.get_json()
        geo = Geos(lat=data['lat'],lng=data['lng'], address=data['address'])
        try:
            db.session.add(geo)
            db.session.commit()
        except:
            logger.warning("There was problem in creating data")
        
        res = geo_schema.dump(geo)
        return jsonify(res)

class singleGeo(Resource):
    def get(self, id):
        geo = Geos.query.get(id)
        geo_json = geo_schema.dump(geo) 
        return jsonify(geo_json)

    def put(self, id):
        data = request.get_json()
        geo = Geos.query.get(id)
        geo.lat = data['lat']
        geo.lng = data['lng']
        db.session.commit()
        res = geo_schema.dump(geo)
        return jsonify(res)
    
    def delete(self, id):
        geo = Geos.query.get(id)
        db.session.delete(geo)
        db.session.commit()
        res =  geo_schema.dump(geo)
        return jsonify(res)

        
