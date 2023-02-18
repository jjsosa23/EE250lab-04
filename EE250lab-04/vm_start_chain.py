import paho.mqtt.client as mqtt
import time
import socket

#summ = 0

def on_message(client, userdata, msg):
    print("Callback - " + msg.topic + " " + str(msg.payload, "utf-8"))

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("jjsosa/pong")
    client.message_callback_add("jjsosa/pong", on_message_from_ping)
    #client.publish("jjsosa/ping", summ)
   
def on_message_from_ping(client, userdata, message):
    summ = int(message.payload.decode()) + 1
    #summ = summ + 1

    #print("summ)
    print("Sending ping")
    print(summ)
    time.sleep(1)
    client.publish("jjsosa/ping", summ)

if __name__ == '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(host="172.20.10.4", port=1883, keepalive=60) #Raspberrypi address 
    client.publish("jjsosa/ping", 0)
    client.loop_forever()
    time.sleep(1)

    #summ = 0