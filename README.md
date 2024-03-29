# hss-python
Simple API server suite written in python, Designed by Clean Architecture and DDD

## Dependency
Python3.10

  -> Python Standard Library(typing, hashlib, secrets, time, os)
  
  -> flask, flask-restful, mysqlclient 
  
  (Since an interface is provided, it is easy to change to other libraries by writing code that implements it and creating a Factory.)
  
## Setup

After implementing the web framework and database code to be used (Flask+Flask-RESTful+MySQL code is implemented by default), just run main.py

## Usage
example:
```
python3 main.py
```

### h5n_authorization
Resource Owner Pasword Credentials Grant in OAuth2.
After running, POST the values of "grant_type", "username", "password", and "scope" to the server-address:port-number/oauth2/token in the form format, and the token (token, expires_in) will be returned.

example:
```
curl -XPOST -d grant_type="password" -d username="horizon" -d password="Halcyon441" -d scope="api" 192.168.1.9:5000/oauth2/token
```

## Licence
Written under the MIT License.

## Authors
Created by horizon2038.
The code design is based on the Clean Architecture book and Vaughn Vernon's DDD book.

