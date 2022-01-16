import pymongo
from bson.objectid import ObjectId  

myclient = pymongo.MongoClient("mongodb+srv://ozymandias:leviAthan99!@cluster0.ydu9h.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb['products']

# mycollection.update_one(
#     {'name': 'Samsung S6'},
#     {'$set':{
#         'name':'Iphone 7',
#         'price': 5000
#     }}
# )

mycollection.update_many(
    {'name': 'Samsung S7'},
    {'$set':{
        'name':'Iphone 8',
        'price': 5000
    }}
)
for i in mycollection.find():
    print(i)