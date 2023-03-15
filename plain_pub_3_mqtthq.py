from datetime import datetime
from random import randint
import time
import paho.mqtt.client as paho
from paho import mqtt

# server information: https://www.support.aceautomation.eu/knowledge-base/list-of-popular-mqtt-brokers-for-testing-and-how-to-connect-to-them/
   
def dump_pub(waktu, mess):
   f = open('Publisher Plain.csv', 'a')
   f.write(str(mess) + ";" + waktu + "\n")

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
    
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

mess50bytes = '/home/FL1--T01:25.8C;T01:25.8C;H01:70.5%'
mess100bytes = '/home/FL01a--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;Fan01:OFF;Fan02:OFF'
mess150bytes = '/home/FL01--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;L03:ON;L04:OFF;Fan01:OFF;Fan01:OFF;Fan02:OFF;Pow01:11.5W;Pow02:11.2W;;'
mess200bytes = '/home/FL01--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;L03:ON;L04:OFF;Fan01:OFF;Fan01:OFF;Fan02:OFF;Pow01:11.5W;Pow02:11.2W;Pow03:11.0W;Door01:CLOSE;Door02:OPEN;Win01:CLOSE;;'

mess = mess50bytes #ganti sesuai dgn panjang pesan yg diperlukan
mess_si = len(mess)

client.username_pw_set("aceautomation", "ilovetheseproducts")
client.connect("aceautomation.ddns.net", 1883)

        # plaintex = 4 byte -> payload = 20 bytes
b = 14  # plaintex = 14 byte -> payload = 30 bytes
        # plaintex = 24 byte -> payload = 40 bytes
    
message = {}
for i in range (20) :
    # mess = "0"
    # if b == 4:
    #     pl = randint (1000,9999)
    #     mess = str(pl)
    # elif b == 14:
    #     pl = randint (10000,99999)
    #     mess = str(pl)
    #     pl = randint (10000,99999)
    #     mess = mess + str(pl)
    #     pl = randint (1000,9999)
    #     mess = mess + str(pl)
    # elif b == 24:
    #     pl = randint (10000,99999)
    #     mess = str(pl)
    #     pl = randint (10000,99999)
    #     mess = mess + str(pl)
    #     pl = randint (10000,99999)
    #     mess = mess + str(pl)
    #     pl = randint (10000,99999)
    #     mess = mess + str(pl)
    #     pl = randint (1000,9999)
    #     mess = mess + str(pl)
    
    now = "{:.5f}".format(time.time())
    now = now[5:]
    
    payload = "p:"+mess+";" + "t:"+now 
    client.publish("iot/temp-1", payload=payload, qos=0)
    print("Published > ", payload)
    dump_pub(now, mess)
    print(len(payload))
    time.sleep(2)
            
client.disconnect()