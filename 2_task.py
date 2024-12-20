import pymongo

if __name__=="__main__":
    print("welcome to Bank")
    client =pymongo.MongoClient("localhost:27017")
    print(client)
    db=client['Bank']  
    collection=db['Bank_collection']
    dictionary={"Name":"Bhumi","location":"Nagpur","Bank Name":"BOI"}
    collection.insert_one(dictionary)
    