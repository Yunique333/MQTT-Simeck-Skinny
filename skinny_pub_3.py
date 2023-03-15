from datetime import datetime
from random import randint
import random as rand
import time
import paho.mqtt.client as paho
from paho import mqtt
from SkinnyCipher import SkinnyCipher as Skinny

def dump_pub(waktu, mess, messc):
   f = open('Publisher Skinny.csv', 'a')
   f.write(str(mess) + ";" + str(messc) + ";" + waktu + "\n")

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
    
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set("aceautomation", "ilovetheseproducts")
client.connect("aceautomation.ddns.net", 1883)

           
mess50bytes = '/home/FL1--T01:25.8C;T01:25.8C;H01:70.5%'
mess100bytes = '/home/FL01a--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;Fan01:OFF;Fan02:OFF'
mess150bytes = '/home/FL01--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;L03:ON;L04:OFF;Fan01:OFF;Fan01:OFF;Fan02:OFF;Pow01:11.5W;Pow02:11.2W;;'
mess200bytes = '/home/FL01--T01:25.8C;T02:26.0C;Hum01:70.8%;Hum02:71.2%;L01:ON;L02:ON;L03:ON;L04:OFF;Fan01:OFF;Fan01:OFF;Fan02:OFF;Pow01:11.5W;Pow02:11.2W;Pow03:11.0W;Door01:CLOSE;Door02:OPEN;Win01:CLOSE;;'

mess = mess100bytes; #ganti sesuai dgn panjang pesan yg diperlukan
mess_si = len(mess)

block_si = 64

key1 = 0x1FE2548B4A0D14DC
key1_si = 64

key2 = 0x1FEA0D14DC8B4A0D142548B4DC1FE254
key2_si = 128

key = key1 #ganti sesuai dgn kunci yg diperlukan
key_si = key1_si #ganti sesuai dgn kunci yg diperlukan
block_si = block1_si #fixed

cipher = Skinny(key, key_si, block_si, mode='ECB')

for i in range (10) :
    now = "{:.5f}".format(time.time())
    now = now[5:]
    if i > 0:
        mess = ''.join(rand.sample(mess,mess_si))
    messc = cipher.encrypt_dt(mess)
    payload = "p:"+messc+";"+"t:"+now 

    client.publish("test/1", payload=payload, qos=1)
    print("Published > ", payload)

    dump_pub(now, mess, messc)

    print(len(str(payload)))

    time.sleep(2)
            
client.disconnect()

