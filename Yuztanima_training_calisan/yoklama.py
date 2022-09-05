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
#mqtt broker codes: end



today = date.today()
day = today.strftime("%b-%d-%Y")
day_str = "yoklama-" + day + ".csv"
print(day_str)

dosya = open(day_str, "a")
dosya.write("Ad, Saat")
dosya.close()

def yoklamayaYaz(name):
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




# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")

# Load Camera
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]

        cv2.putText(frame, name,(x1, y1 - 10), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)

        yoklamayaYaz(name)


    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
