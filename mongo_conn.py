from pymongo import MongoClient

# Connection settings
# MONGO_HOST = 'localhost'
# MONGO_PORT = 27017

# # Create a client
# client = MongoClient(MONGO_HOST, MONGO_PORT)

# Close the client
# client.close()


from pymongo import MongoClient

# Connection settings
MONGO_HOST = 'cluster01.h2shv.mongodb.net'
MONGO_PORT = 27017
MONGO_DB = 'Cluster01'
MONGO_USERNAME = 'psamanta1401'
MONGO_PASSWORD = 'JdHnusH6OY7K7sZt'

# Create a client with authentication
client = MongoClient(
    f'mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}/{MONGO_DB}'
)