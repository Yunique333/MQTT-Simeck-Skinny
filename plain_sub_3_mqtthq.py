from datetime import datetime
import json
import time
import paho.mqtt.client as paho
from paho import mqtt

# server information: https://www.support.aceautomation.eu/knowledge-base/list-of-popular-mqtt-brokers-for-testing-and-how-to-connect-to-them/

def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)
client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
client.on_connect = on_connect

client.username_pw_set("aceautomation", "ilovetheseproducts")
client.connect("aceautomation.ddns.net", 1883)

        # plaintex = 4 byte -> payload = 20 bytes
b = 14  # plaintex = 14 byte -> payload = 30 bytes
        # plaintex = 24 byte -> payload = 40 bytes

def dump_sub(msg, timeSend):
	now = "{:.5f}".format(time.time())
	now = now[5:]
	f = open('Subscriber Plain.csv', 'a')
	f.write(msg + ";" + now + ";" + timeSend + "\n")


def on_message(client, userdata, msg):
    msg = msg.payload.decode("utf-8")
    mess=msg[2:]
    mess=mess.split(";")[0,1,2]
    timeSend = msg.split(";")[3]
    timeSend = timeSend[2:]
    dump_sub(mess, timeSend)
    print("Subscribed > ", msg)
    

client.on_message = on_message
client.subscribe("iot/temp-1", qos=0)

client.loop_forever()