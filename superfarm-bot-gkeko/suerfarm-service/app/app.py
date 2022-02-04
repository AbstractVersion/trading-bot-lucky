from flask import Flask, request, jsonify, make_response
from flask_cors import CORS, cross_origin
from flask_restplus import Resource, Api, inputs, fields
import requests
import datetime, logging
import time
import json
import os

from influxdb import InfluxDBClient
import time 

# cg = CoinGeckoAPI()
# print ('Initializint...')


app = Flask(__name__)    
CORS(app)

api = Api(app = app, 
		  version = "0.1", 
		  title = "Dion Service API v.01", 
		  description = "Perform CRUD Operations on Dion Mongo DB",
          prefix='/dion-service',
          doc='/doc/') 

def queryInflux(value=None, hours=None, minutes=None):
    try:
        client = InfluxDBClient(    host= "localhost", 
                                    port=8086, 
                                    username="admin", 
                                    password="admin"
                                )
        client.create_database("superfarm")
        client.switch_database("superfarm")
        print("connected to influx")
    except:
        print('ERROR during connection with INFLUX DB')
    dictout = {}
    query = str('SELECT value FROM superfarm_usd where time> now() - '+str(hours)+'h ORDER BY time DESC')#+' and time <= '+ str(now)
    result = client.query(query)
    dictout['data'] = result.raw
    return dictout

api_space = api.namespace('api', description='Base api endpoint')
@api_space.route('/')                  
class PingApi(Resource):           
    @api.expect()
    def get(self):                  
        return app.response_class(
                    response=json.dumps({'status': 'up'}),
                    status=200,
                    mimetype='application/json'
                )

natura_space = api.namespace('superfarm', description='Base endpoint to get superfarm usd price')
@natura_space.route('/usd')                 
class NatureGeometryWithinCount(Resource):           
    @api.expect()
    def get(self): 
        hour = request.args.get('hour', default = 1, type = int)        
        response = json.dumps(queryInflux(hour))
        return  app.response_class(
                    response=response,
                    status=200,
                    mimetype='application/json'
                )