import pymongo
client = pymongo.MongoClient("mongodb+srv://ADUBEYFORU:Train12#$@alok.0ddhn.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    'name':'alok',
    'emailid':'dubeyalok@rediffmail.com',
    'surname':'dubey'
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d)