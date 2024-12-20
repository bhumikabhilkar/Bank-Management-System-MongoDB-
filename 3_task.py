import pymongo

if __name__=="__main__":
    print("welcome to Bank")
    client =pymongo.MongoClient("localhost:27017")
    print(client)
    db=client['Bank']
    collection=db['Bank_collection']
    #dictionary={"name":"HUzefa", "marks":88}
    #collection.insert_one(dictionary)
    insertThese=[
        {'Name':"Rahul",'Location':'Nagpur','Bank Name':"BOI"},
        {'Name':"Ishan",'Location':'Delhi','Bank Name':"HDFC"},
        {'Name':"Kajal",'Location':'City','Bank Name':"SBI"},
        {'Name':"Falgun",'Location':'Nagpur','Bank Name':"CANERA"},
    ]
    
    
    collection.insert_many(insertThese)