from mongo_conn import client
import pandas as pd




{
    "_id": "ObjectId",
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30,
    "dept": "physics",
    "address": {
        "street": "123 Main St",
        "city": "New York",
        "state": "NY"
    }
}

# Fields in this document: like colums in sql
# _id (unique identifier)
# name
# email
# age
# address (embedded document with sub-fields)
# street
# city
# state

# Query data

# Useful Operators:
# $eq (equal)
# $ne (not equal)
# $gt (greater than)
# $lt (less than)
# $in (in array)
# $nin (not in array)
# $exists (field exists)
# $regex (regular expression)

# Useful Aggregation Stages:
# $match (filter)
# $project (transform)
# $group (aggregate)
# $sort (sort)
# $limit (limit)

db = client['Cluster01']
collection = db['mycollection']


# Query data
data = collection.find()

# Convert to DataFrame
df = pd.DataFrame(data)

print(df)


# Query data and convert to DataFrame
df = pd.DataFrame(collection, query={'name': 'John Doe'}) #filter

# Aggregation pipeline
pipeline = [
    {"$match": {"field": "value"}},
    {"$project": {"field1": 1, "field2": 1}} #  for filtering #Purpose: Reshape documents by selecting specific fields.Syntax: {"$project": {"field1": 1, "field2": 1}}
                                            #Effect: Include only field1 and field2 in the output documents.
]
data = db.collection.aggregate(pipeline)

# Convert to DataFrame
df = pd.DataFrame(list(data))

print(df)


db.collection.countDocuments()


data = collection.find({ "field1": "value1", "field2": "value2" }) #filter
data = db.collection.find({ "$and": [{ "field1": "value1" }, { "field2": "value2" }] })
data =db.collection.find({ "field": null })
data =db.collection.find({ "field": { "$exists": true } })
db.collection.find({ "field": { "$ne": "value" } })
db.collection.find({ "field": { "$gt": "value" } })
data =db.collection.find({ "field": "/pattern/" }) #regex filter


data =db.collection.find().sort({ "field": 1 }) #asc
data =db.collection.find().sort({ "field": -1 }) #dsc
data =db.collection.find().sort({ "field1": 1, "field2": -1 })

df = pd.DataFrame(list(data))

print(df)

document = {'name': 'John Doe', 'age': 30}
collection.insert_one(document)
db.collection.insertOne({ "field": "value" })
db.collection.insertMany([{ "field": "value1" }, { "field": "value2" }])

db.collection.updateOne({ "field": "value" }, { "$set": { "newField": "newValue" } })
db.collection.updateMany({ "field": "value" }, { "$set": { "newField": "newValue" } })
db.collection.updateOne({ "field": "value" }, { "$inc": { count: 1 } }) #increment

data =db.collection.find().sort({ "field": -1 }).limit(10)
data =db.collection.find({ "field": { "$gt": "value" } }).sort({ "field": -1 }).limit(10)
data =db.collection.find().skip(10)
data =db.collection.find().skip(10).limit(10)

df = pd.DataFrame(list(data))

print(df)


b.collection.deleteOne({ field: "value" })
db.collection.deleteMany({ field: "value" })

db.collection.distinct("field")


data = db.collection.aggregate([
    { "$match": { field: "dept" } },  #Purpose: Filter documents based on a condition.Syntax: { $match: { field: "value" } }Effect: Only include documents where field equals "value".
    { "$group": { _id: "$field", count: { "$sum": 1 } } }  # Group documents by a common field and perform aggregation.
])
db.collection.aggregate([{ "$group": { _id: "$field", count: { "$sum": 1 } } }])

