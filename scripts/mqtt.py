import time
import datetime
import json
import base64
import paho.mqtt.client as paho
import base64todecimal as basetodec
import mysql.connector

broker="lora.kent.ac.uk"
mydb = mysql.connector.connect(
    host="dragon.kent.ac.uk",
    user="ajh203",
    passwd = "li3serv",
    database = "ajh203",
    port = 3306
)

mycursor = mydb.cursor()
sql = "INSERT INTO SensorData (sensor,dataValue,dataTimeStamp,dataLongitude,dataLatitude,dataHardwareSerial,dataAltitude) VALUES (%s,%s,%s,%s,%s,%s,%s)"

#define callback
def on_message(client, userdata, message):
    time.sleep(1)
    jsonMessage = json.loads(message.payload.decode("utf-8"))
    print("HERE")
    print("Device id",jsonMessage['dev_id'])
    print("Time",jsonMessage['metadata']['time'].replace("T"," ").replace("Z",""))
    # print("Payload",basetodec.base64todecimal(jsonMessage['payload_raw']))
    # print("Hardware serial",jsonMessage['hardware_serial'])
    # print("Meta",jsonMessage['metadata'])
    # print("Latitude",jsonMessage['metadata']['latitude'])
    # print("Longitude",jsonMessage['metadata']['longitude'])
    # print("Altitude",jsonMessage['metadata']['altitude'])
    # print("Timestamp",str(datetime.datetime.now()))
    # print("received message =",jsonMessage)
    val = (jsonMessage['dev_id'],
        basetodec.base64todecimal(jsonMessage['payload_raw']),
        str(datetime.datetime.now()),
        jsonMessage['metadata']['longitude'],
        jsonMessage['metadata']['latitude'],
        jsonMessage['hardware_serial'],
        jsonMessage['metadata']['altitude'])
    print(val);
    mycursor.execute(sql,val)
    mydb.commit()
    print("Commited")



client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
######Bind function to callback
client.username_pw_set(username="kentwatersensors",password="ttn-account-v2.mRzaS7HOchwKsQxdj1zD-KwjxXAptb7s9pca78Nv7_U")
client.on_message=on_message
#####
print("connecting to broker ",broker)
client.connect(broker,1883,6000)#connect
client.loop_start() #start loop to process received messages
print("subscribing ")
client.subscribe("kentwatersensors/devices/+/up")#subscribe

while(True):
    print("Waiting")
    time.sleep(60)
# client.disconnect() #disconnect
# client.loop_stop() #stop loop
