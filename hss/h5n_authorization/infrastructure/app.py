from flask import Flask
from flask_restful import Api

from application.userauthenticationinputport import UserAuthenticationInputport
from infrastructure.authorizationserver import Token
from infrastructure.ipaddressloader import IPAddressLoader

class ServerCore():
    def __init__(self, user_authentication_usecase: UserAuthenticationInputport, ip_address_loader: IPAddressLoader):
        self.ip_address_loader: IPAddressLoader = ip_address_loader
        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.api.add_resource(Token, '/oauth2/token', resource_class_kwargs={'user_authentication_usecase': user_authentication_usecase})

    def run(self):
        __ip_address: str = self.ip_address_loader.load_ip_address()
        self.app.run(debug=True, host=__ip_address, port=5000) #TODO: chenge the hard coding of the ip address

