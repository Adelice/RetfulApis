from flask import Flask,request
from flask_restful import Api,Resource
from flask_marshmallow import Marshmallow
from marshmallow import fields,validates,ValidationError,validate


app = Flask(__name__)
api=Api(app)
ma=Marshmallow()

#class to validates data
class RegisterStudent(ma.Schema):
    studentname=fields.String(required=True, validate=validate.Length(min=5, max=10,error="invalid name length"))
    studentemail=fields.Email(required=True)
    studentclass=fields.String(required=True)

#create a view 
class HelloWorld(Resource):
    def get(self,**kwargs):
        return {"message":"This hello World page"}
    def post(self):
        json_data=request.get_json()
        return json_data
class RegisterStudentClassView(Resource):
    """Student Registration view"""
    def post(self):
        json_data=request.get_json() 
        # validates api data
        try:
             RegisterStudent().load(json_data)
        except ValidationError as err:
            return err.messages, 400
        return {"message": "Sucessfully registered"},200
        
        RegisterStudent().load(json_data)


api.add_resource(HelloWorld,"/")  
api.add_resource(RegisterStudentClassView,"/addstudent")  


if __name__=="main":
    app.run(debug=True)
