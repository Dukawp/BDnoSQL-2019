import mysql.connector
import urllib, json, time

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="sensordb"

)

print(mydb)

mycursor = mydb.cursor()
i=1
while(i<6):
  url = "http://nosql.hpeixoto.me/api/sensor/300{}" .format(i) 
  response = urllib.urlopen(url)
  data = json.loads(response.read())


  dataP = data['patient']
  dataB = data['bloodpress']

  sensorId = data['sensorid']
  sensorNum = data['sensornum']
  patientId = dataP['patientid']
  patientBirthday = dataP['patientbirthdate']
  patientAge = dataP['patientage']
  patientName = dataP['patientname']
  bodyTemp = data['bodytemp']
  typeOfSensor = data['type_of_sensor']
  timeStamp = data['timestamp']
  bpSystolic = dataB['systolic']
  bpDiastolic = dataB['diastolic']
  bpm = data['bpm']


  sq2 = "INSERT INTO patient VALUES ( {}, '{}', ('{}'), {})" .format(patientId, patientName,patientBirthday,patientAge,sensorId)
  mycursor.execute(sq2)
  mydb.commit()
  print(mycursor.rowcount, "record inserted.")
  i+=1

while True:
  i=1
  while(i<6):
    url = "http://nosql.hpeixoto.me/api/sensor/300{}" .format(i) 
    response = urllib.urlopen(url)
    data = json.loads(response.read())


    dataP = data['patient']
    dataB = data['bloodpress']

    sensorId = data['sensorid']
    sensorNum = data['sensornum']
    patientId = dataP['patientid']
    patientBirthday = dataP['patientbirthdate']
    patientAge = dataP['patientage']
    patientName = dataP['patientname']
    bodyTemp = data['bodytemp']
    typeOfSensor = data['type_of_sensor']
    timeStamp = data['timestamp']
    bpSystolic = dataB['systolic']
    bpDiastolic = dataB['diastolic']
    bpm = data['bpm']
    sq1 = "INSERT INTO sensor (sensorId,sensorNum,typeOfSensor,bodyTemp,bpSystolic,bpDiastolic,bpm,timeStamp,Patient_patientId) VALUES ( {}, {}, '{}', {}, {}, {}, {}, ('{}'), {})" .format(sensorId, sensorNum,typeOfSensor,bodyTemp,bpSystolic,bpDiastolic,bpm,timeStamp,patientId)
    mycursor.execute(sq1)


    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    i+=1
  print("A espera de novos dados ... 10 segundos")  
  time.sleep(11)

