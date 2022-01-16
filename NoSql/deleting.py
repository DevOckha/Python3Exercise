import pymongo
from bson.objectid import ObjectId  

myclient = pymongo.MongoClient("mongodb+srv://ozymandias:leviAthan99!@cluster0.ydu9h.mongodb.net/node-app?retryWrites=true&w=majority")

mydb = myclient["node-app"]
mycollection = mydb['products']


#delete_one()
#delete_many()

for i in mycollection.find():
    print(i)


print('*'*30)

#mycollection.delete_one({'name':'Iphone 6'})
mycollection.delete_many({'name':{'$regex':'^S'}})


for i in mycollection.find():
    print(i)
