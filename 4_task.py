import pymongo

if __name__ == "__main__":
    print("Welcome to Bank")
    client = pymongo.MongoClient("localhost:27017")
    print(client)
    db = client['Bank']
    collection = db['Bank_collection']
    
    # Fetch and print all documents
    print("All documents in the collection:")
    for document in collection.find():
        print(document)
