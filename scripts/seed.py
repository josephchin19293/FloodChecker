import requests
import json
import mysql.connector
import base64todecimal as basetodec

mydb = mysql.connector.connect(
    host="dragon.kent.ac.uk",
    user="ajh203",
    passwd = "li3serv",
    database = "ajh203",
    port = 3306
)

mycursor = mydb.cursor()

headers = {
    'Accept': 'application/json',
    'Authorization': 'key ttn-account-v2.mRzaS7HOchwKsQxdj1zD-KwjxXAptb7s9pca78Nv7_U',
}

params = (
    ('last', '7d'),
)

response = requests.get('https://kentwatersensors.data.thethingsnetwork.org/api/v2/query', headers=headers, params=params)
y = json.loads(response.content)

sql = "INSERT INTO SensorData (sensor,dataValue,dataTimeStamp,dataLongitude,dataLatitude,dataHardwareSerial,dataAltitude) VALUES (%s,%s,%s,%s,%s,%s,%s)"
val = []

longlat = []
for x in y:
    if(x['device_id'] == 'lairdc0ee400001012345'):
        longlat = {'long':1.0742298,'lat': 51.281,'hardware':'C0EE400001012345','altitude':8}
    elif(x['device_id'] == 'lairdc0ee4000010109f3'):
        longlat = {'long':1.0776373,'lat':51.279247,'hardware':'C0EE4000010109F3','altitude':9}

    val.append((x['device_id'],basetodec.base64todecimal(x['raw']),x['time'].replace("T"," ").replace("Z",""),longlat['long'],longlat['lat'],longlat['hardware'],longlat['altitude']))
    print((x['device_id'],basetodec.base64todecimal(x['raw']),x['time'].replace("T"," ").replace("Z",""),longlat['long'],longlat['lat'],longlat['hardware']))
mycursor.execute("DELETE FROM Data", "")
mycursor.executemany(sql,val)

mydb.commit()

print(mycursor.rowcount,"was inserted.")

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://kentwatersensors.data.thethingsnetwork.org/api/v2/query?last=7d', headers=headers)
