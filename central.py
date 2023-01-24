from email.quoprimime import header_decode
from multiprocessing.connection import Client
import turtle
import time
import paho.mqtt.client as paho
import time
import random
import paho.mqtt.client as mqtt
import rpyc

#hostname
broker="localhost"

#port
port=1883

#time to live
timelive=60
delay = 0.01

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("carro")

def on_message(client, userdata, msg):
    temp = msg.payload.decode()
    print(str(temp))
    if int(temp) > 110:
        message= "Cuidado, temperatura alta. Vá para os box's"
        print("Recebendo")
        ret= client.publish("volante", message)
    time.sleep(5)

def on_message_equipe(client, userdata, msg): 
    ret= client.publish("volante", msg)
    time.sleep(5)
            

client = mqtt.Client()
client.connect(broker,port,timelive)
client.on_connect = on_connect
client.on_message = on_message
client.on_message_equipe = on_message_equipe
client.loop_start()
time.sleep(5)
class MeuServico(rpyc.Service):

    def exposed_message_pilot(self, message):
        on_message_equipe(client, self, message)

from rpyc.utils.server import ThreadedServer
t = ThreadedServer(MeuServico, port=18866)
t.start()