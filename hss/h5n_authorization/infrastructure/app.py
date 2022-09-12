from flask import Flask
from flask_restful import Api

from application.userauthenticationinputport import UserAuthenticationInputport
from infrastructure.authorizationserver import Token
from infrastructure.ipaddressloader import IPAddressLoader

class ServerCore():
    def __init__(self, user_authentication_usecase: UserAuthenticationInputport):
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(Token, '/oauth2/token', resource_class_kwargs={'user_authentication_usecase': user_authentication_usecase})

    def run(self):
        self.app.run(debug=True, host="0.0.0.0", port=5000) #TODO: chenge the hard coding of the ip address

