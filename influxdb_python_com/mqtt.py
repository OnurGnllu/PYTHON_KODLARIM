#main olarak bu klasör çalıştırılır. Influxdb Adapter buraya import edilir.
from datetime import datetime
from datetime import date
import paho.mqtt.client as mqttclient
import time
from influxdb_adapter import getvaluefrommqttt
def on_connect(client,usedata,flags,rc):
    if rc==0:
        print("client is connected")
        global connected
        connected=True
    else:
        print("connection failed")
def on_message(client,usedata,message):
    print("Message received = " +  str(message.payload.decode("utf-8")))
    getvaluefrommqttt(str(message.payload.decode("utf-8")))
    print("Topic = "+ str(message.topic))


#mqtt broker codes:

connected=False
Messagerecieved=False
mqtt_port = 1883
mqtt_broker = "io.adafruit.com"
mqtt_username = "onurgnllu"
mqtt_password = "aio_ZDwe95DR8PzK7bjY6AecWE2Gslsz"

client = mqttclient.Client("MQTT")
client.on_message=on_message
client.username_pw_set(mqtt_username,password=mqtt_password)
client.on_connect=on_connect
client.connect(mqtt_broker,port=mqtt_port)
client.loop_start()
client.subscribe("onurgnllu/f/counter_value")
while connected!=True:
    time.sleep(0.2)
while Messagerecieved!=True:
    time.sleep(0.2)

client.loop_stop()

