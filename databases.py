from mongo_conn import client



# Access the database and collection (creates them if they don't exist)
db = client['Cluster01']
collection = db['mycollection']
collection2 = db.create_collection("mycollection2")

# # List database names
# databases = client.list_database_names()
# print(databases)


# Insert a document
# document = {'name': 'John Doe', 'age': 30}
# collection.insert_one(document)

# List database names
databases = client.list_database_names()
print(databases)


# Drop collection
# db['mycollection'].drop()
# or
# db.drop_collection('mycollection')


# Drop database
# client.drop_database('mydatabase')