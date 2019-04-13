import urllib3
import json
import datetime
import time
import random

http = urllib3.PoolManager()
LDR, temp, humidity = 0, 0, 0
dt = str(datetime.datetime.now())

d = {"time_stamp": "0",
     "Sensor1": {"name": "LDR Sensor",
                 "Value": LDR,
                 "Desc": "blr_sensor"
                 },
     "Sensor2": {"name": "LDR Sensor",
                 "Value": temp,
                 "Desc": "blr_sensor"
                 },
     "Sensor3": {"name": "LDR Sensor",
                 "Value": humidity,
                 "Desc": "blr_sensor"
                 }
     }

while True:
    d['time_stamp'] = str(datetime.datetime.now())
    d['Sensor1']['Value'] = random.randrange(1, 100, 1)
    d['Sensor2']['Value'] = random.randrange(1, 100, 1)
    d['Sensor3']['Value'] = random.randrange(1, 100, 1)
    encode_data = json.dumps(d).encode('utf-8')
    r = http.request('POST',
                     'http://localhost:8000/uploadsensordata',
                     body=encode_data,
                     headers={'Content-Type': 'application/json'}
                     )

    time.sleep(5)


    print(d)