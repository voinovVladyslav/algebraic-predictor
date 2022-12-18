from . import api as api_app
from flask_restful import Api
from . import views

api = Api(api_app)

api.add_resource(views.HelloWorld, '/api/hello/', endpoint='hello')
