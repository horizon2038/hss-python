import json
from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse
from typing import Protocol

from application.userdata import UserData
from application.tokendata import TokenData
from application.userauthenticationinputport import UserAuthenticationInputport
from application.applicationexception import ApplicationException

class Token(Resource):
    def __init__(self, user_authentication_usecase: UserAuthenticationInputport):
        self.user_authentication_usecase: UserAuthenticationInputport = user_authentication_usecase

    def post(self):
        try:
            parser: any = self.__init_parser()
            inputdata: dict = self.__load_argument(parser)
            userdata: UserData = UserData(str(inputdata["username"]), str(inputdata["password"]))
            tokendata: TokenData = self.user_authentication_usecase.authenticate(userdata)
            return jsonify({"access_token": tokendata.token, "token_type": "bearer", "expires_in": tokendata.expires_in, "refresh_token": "None"})
        
        except ApplicationException as e:
            error_message: str = str(e) 
            print("error: {}".format(error_message))
            return jsonify({"error": error_message})

    def __init_parser(self) -> any:
        parser = reqparse.RequestParser()
        self.__add_argument(parser)
        return parser

    def __add_argument(self, parser: any):
        parser.add_argument("grant_type", location="form")
        parser.add_argument("username", location="form")
        parser.add_argument("password", location="form")
        parser.add_argument("scope", location="form")

    def __load_argument(self, parser: any) -> dict:
        args: any = parser.parse_args()
        return self.__repack_argument(args)

    def __repack_argument(self, args: any) -> dict:
        inputdata: dict = {"grant_type": args["grant_type"], "username": args["username"], "password": args["password"], "scope": args["scope"]}
        return inputdata