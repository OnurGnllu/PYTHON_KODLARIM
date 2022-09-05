import cv2
from simple_facerec import SimpleFacerec
from datetime import datetime
from datetime import date
import paho.mqtt.client as mqttclient
import time
def on_connect(client,usedata,flags,rc):
    if rc==0:
        print("client is connected")
        global connected
        connected=True
    else:
        print("connection failed")
def on_connect(client,usedata,flags,rc):
    if rc==0:
        print("client is connected")
        global connected
        connected=True
    else:
        print("connection failed")

#mqtt broker codes:
connected=False
mqtt_port = 1883
mqtt_broker = "io.adafruit.com"
mqtt_username = "onurgnllu"
mqtt_password = "aio_ZDwe95DR8PzK7bjY6AecWE2Gslsz"

client = mqttclient.Client("MQTT")
client.username_pw_set(mqtt_username,password=mqtt_password)
client.on_connect=on_connect
client.connect(mqtt_broker,port=mqtt_port)
client.loop_start()
while connected!=True:
    time.sleep(0.2)
#mqqt kodları burada bitti.



today = date.today()
day = today.strftime("%b-%d-%Y")
day_str = "yoklama-" + day + ".csv"
print(day_str)

dosya = open(day_str, "a")
dosya.write("Ad, Saat")
dosya.close()


def mqtt_yaz(name):
    #with open('yoklama.csv','r+') as f:
    with open(day_str, 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])

        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
            name2 = name + " ismiyle giris yapildi."
            client.publish("onurgnllu/f/mytest", name2)
            client.loop_stop()


