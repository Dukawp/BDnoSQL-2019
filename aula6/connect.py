import urllib.request, json, time
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["analysis"]
collection = db["analysis"]

while True:
  i=1
  while(i<6):
    url1="http://nosql.hpeixoto.me/api/sensor/300{}".format(i)
    response1=urllib.request.urlopen(url1)
    data1=json.loads(response1.read())

    url2="http://nosql.hpeixoto.me/api/sensor/400{}".format(i)
    response2=urllib.request.urlopen(url2)
    data2=json.loads(response2.read())

    print("Inserting Cardiac...")
    db.analysis.insert_one(data1)
    print(data1)
    print("-------------------------------------------")
    print("Inserting Blood...")
    print(data2)
    db.analysis.insert_one(data2)
    
    i+=1
  time.sleep(11)

print("The process has finished.")
client.close()