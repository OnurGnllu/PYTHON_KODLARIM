#https://www.youtube.com/watch?v=qvCQfBoQzzc&list=PLLqmi_UARmfkBDjLukGGMBATGrD-U8lLd&index=7
from influxdb import InfluxDBClient
from datetime import datetime
client=InfluxDBClient(host="localhost",port="8086")
print(client.get_list_database()) #influxdbde açık olan databesleri görüntüler
client.switch_database("trainingdB") #trainingdB veritabanına bağlan
print(client.get_list_measurements()) #trainingdB içerisindeki measurements verilerini alır
def getvaluefrommqttt(name):

    json_body = [
        {
            "measurement": "deletable",
            "tags": {
                "sensor_name": name
            },
            "fields": {
                "temp": 127
            }
        }
    ]
    client.write_points(json_body)

results = client.query('SELECT * FROM deletable')
print(results)
results2 = list(results.get_points(measurement='deletable',tags={"sensor_name": "kitchen_temp"}))
