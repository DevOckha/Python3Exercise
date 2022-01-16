import re
import pymongo
from bson.objectid import ObjectId  

#myclient = pymongo.MongoClient("mongodb://localhost:27017") client ile bağlantı
myclient = pymongo.MongoClient("mongodb+srv://ozymandias:leviAthan99!@cluster0.ydu9h.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb['products']

# product = {'name':'Samsung S5', 'price':2000}
# result = mycollection.insert_one(product)

# print(result)
# print(result.inserted_id)


# productList = [
#     {'name':'Samsung S6', 'price':3000, 'description':'iyi telefon'},
#     {'name':'Samsung S7', 'price':4000, 'categories':['Telefon', 'Elektronik']},
# ]

# result = mycollection.insert_many(productList)
# print(result.inserted_ids)

#result = mycollection.find_one()

# for i in mycollection.find({}, {'_id':0, 'name':1, 'price':1}):
#     print(i)

# result = mycollection.find({'name':'Samsung S5'})
# for i in result:
#     print(i)

# result = mycollection.find_one({'_id': ObjectId('61adfe0c8c2f3c959b1d405c')})

# result = mycollection.find({
#     'name':{
#         '$in' : ['Samsung S5','Samsung S6']
#     }
# })
#$gt büyük $gte büyük eşit $eq eşittir $lt küçük $lte küçük eşit
# result = mycollection.find({
#     'price': {
#         '$gte': 2000
#     }
# })

# result = mycollection.find({
#     'name': {
#         '$regex': '^S'
#     }
# })

# for i in result:
#     print(i)