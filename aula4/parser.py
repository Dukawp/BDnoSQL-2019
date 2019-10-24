import urllib, json

url = "http://nosql.hpeixoto.me/api/sensor/3001"
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



print(sensorId)
print(sensorNum)
print(bpm)
print(patientId)
print(timeStamp)