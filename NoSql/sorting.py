import pymongo
from bson.objectid import ObjectId  

myclient = pymongo.MongoClient("mongodb+srv://ozymandias:leviAthan99!@cluster0.ydu9h.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb['products']


#result = mycollection.find().sort('name')
#result = mycollection.find().sort('name', -1)
#result = mycollection.find().sort('price')
#result = mycollection.find().sort('price', -1)
result = mycollection.find().sort([('name',1),('price', -1)])



for i in result:
    print(i)
