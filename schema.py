from marshmallow import Schema, fields,  validate, validates
from flask_marshmallow import Marshmallow
from new_models import *


class GeoSchema(Schema):
    id = fields.Int()
    lat = fields.Str()
    lng = fields.Str()
    address = fields.Int()

class AddressSchema(Schema):
    id  = fields.Int()
    user = fields.Int()
    street = fields.String()
    suite = fields.String()
    city = fields.String()
    zipcode = fields.String()
    geo = fields.Nested(GeoSchema)
    
class CompanySchema(Schema):
    id = fields.Int()
    name = fields.String()
    catchPhrase = fields.String()
    bs = fields.String()
    user = fields.Int()

class UserSchema(Schema):
    id = fields.Int()
    name = fields.String()
    username = fields.String(validate=validate.Length(min=1))
    phone = fields.String(validate=validate.Length(equal=10))
    website = fields.String()
    email = fields.String(validate=validate.Email(error="Please enter valid email address"))

    company = fields.Nested(CompanySchema)
    address = fields.Nested(AddressSchema)



