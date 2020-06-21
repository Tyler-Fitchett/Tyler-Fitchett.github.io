#!/use/bin/python
import json
from bson import json_util
import bottle
from bottle import route, run, request, abort
from datetime import datetime
import pymongo
from pymongo import MongoClient

connection = MongoClient('localhost', 27017)
db = connection['market']
collection = db['stocks']


@route('/createStock', method='POST')         ## Create a stock document using input from curl
def create_document():
  data = request.body.readline()
  if not data:
    abort(400, 'Error')
  entity = json.loads(data)
  if not entity.has_key('Ticker'):
    abort(400, 'No id specified')
  try:
    collection.save(entity)
  except:
    return False



@route('/getStock',method='GET')             ## Retrieve a stock document using input from curl
def get_document():
  ticker = request.query.ticker
  cursor=collection.find_one({'Ticker':request.query.ticker})       
  if not ticker:
    abort(404, 'Ticker not found')
    
  return json.loads(json.dumps(cursor, indent=4, default=json_util.default))


@route('/updateStock',method='PATCH')      ## Update a stock document using input from curl
def update_document():
  ticker_key = request.query.ticker
  sector = request.query.sector
  collection.update_one({"Ticker":ticker_key}, {"$set": {"Sector":sector}})
  if not ticker_key:
    abort(404, 'Ticker not found')
  if not sector:
    abort(404, 'error in result')
    
    
@route('/deleteStock',method='DELETE')   ## Delete a stock document using input from curl
def delete_document():
  ticker = request.query.ticker
  collection.delete_one({"Ticker":ticker})
  
  
@route('/stockReport',method='POST')     ## generate a report of stock document using ticker inputs from curl
def stock_report():
  data = request.body.readline()
  
  if not data:
    abort(400, 'Error')
  myList = data.strip('][').split(',')
  z=''
  x=0
  while(x != len(myList)):
    for y in collection.find({'Ticker':myList[x]},{'Ticker':1, 'Price':1, 'Volume':1, 'Average Volume':1, "_id":0}):
      z += str(y)
      z += '\n'
    x+=1
  return z


@route('/industryReport',method='GET')    ## generate industry reports for documents searched by industry specified from curl input
def industry_report():
  industry_name = request.query.industry
  print industry_name 
  z = ''
  ##y = 1
  for x in collection.find({"Industry":request.query.industry}).limit(5):
    z += str(x)
  ##print z
  return z


      


if __name__ == '__main__':
  #app.run(debug=True)
  run(host='localhost', port=8080)
  