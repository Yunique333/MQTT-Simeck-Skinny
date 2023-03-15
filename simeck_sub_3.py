from datetime import datetime
from random import randint
import time
import paho.mqtt.client as paho
from paho import mqtt
from SimeckCipher import SimeckCipher as Simeck

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

mess = mess50bytes
mess_si = len(mess)

key1 = 0x1FE2548B4A0D14DC
key1_si = 64
block1_si = 32

key2 = 0x2541FE8B1FE24A0C548B4A0D14DCD14D
key2_si = 128
block2_si = 64

cipher = Simeck(master_key=key1, key_size=key1_si, block_size=block1_si)

def dump_sub(msg, timeSend):
	now = "{:.5f}".format(time.time())
	now = now[5:]
	f = open('Subscriber Simeck.csv', 'a')
	f.write(msg + ";" + now + ";" + timeSend + "\n")

def on_message(client, userdata, msg):
    msg = msg.payload.decode("utf-8")
    mess=msg[2:]
    mess1=mess.split(";")[0]
    msgl = cipher.decrypt_dt(mess1,block1_si,key1_si)
    print(msgl)
    timeSend = msg.split(";")[1]
    timeSend1 = timeSend[2:]
    dump_sub(str(msgl), timeSend1)
    print("Subscribed > ", msg)
    
client.on_message = on_message
client.subscribe("test/1", qos=1)

client.loop_forever()