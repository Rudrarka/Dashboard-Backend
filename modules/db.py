import pymongo
import os


class Database:
    def mongodb_conn(self):
        try:
            print(os.getenv('mongo_url'))
            myclient =pymongo.MongoClient(os.getenv('mongo_url'))
            mydb = myclient['dashboard']
            print('connected')
        except :
            print ("Could not connect to server")
        return mydb
