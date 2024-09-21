from databases import collection, collection2
from mongo_conn import client
import json


# Perform CRUD operations
def create_document(_id, name, age):
    document = {'_id': _id,'name': name, 'age': age}
    result = collection2.insert_one(document)  #insert_many([{},{}]) #insert([{},{}])
    print(f"Inserted ID: {result.inserted_id}")
    client.close()

def read_documents():


    # dict = {}
    # documents = collection.find() #{}, projection={'_id': 0, 'name': 1, 'age': 1}
    # print(documents)
    # for document in documents:
        # dict[document['_id']] = document
        # print(json.dumps(document))
    # json_data = json.dumps(dict)
    # print(json_data)


    documents = collection.find().limit(2) #skip(1)
    for document in documents:
        print(document)
    client.close()



def update_document(name, new_age):
    filter = {'name': name}
    update = {'$set': {'age': new_age}}
    result = collection.update_one(filter, update) #update()
    print(f"Updated documents: {result.modified_count}")
    client.close()

def delete_document(name):
    filter = {'name': name}
    result = collection.delete_one(filter)
    print(f"Deleted documents: {result.deleted_count}")
    client.close()



def delete_document(name):
    filter = {'name': name}
    result = collection.delete_one(filter) #remove()
    # result = collection.drop() # to drop all the data from the collection
    print(f"Deleted documents: {result.deleted_count}")
    # Close the client
    client.close()

# Example usage
create_document(103,'sunil', 30)
# read_documents()
# update_document('John Doe', 100)
# delete_document('John Doe')


