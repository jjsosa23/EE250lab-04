import paho.mqtt.client as mqtt
import socket
import time



def on_message(client, userdata, msg):
    print("Callback - " + msg.topic + " " + str(msg.payload, "utf-8"))

def on_connect(client, userdata, flags, rc):
    print("Connected to server (i.e., broker) with result code "+str(rc))
    client.subscribe("jjsosa/ping")
    client.message_callback_add("jjsosa/ping", on_message_from_pong)
    

def on_message_from_pong(client, userdata, message):
    summ = int(message.payload.decode()) + 1
    #summ = summ + 1

    #print("summ)
    print("Sending pong")
    print(summ)
    time.sleep(1)
    client.publish("jjsosa/pong", summ)


if __name__ == '__main__':
    client = mqtt.Client()
    client.on_message_from_pong = on_message
    client.on_connect = on_connect
    client.connect(host="172.20.10.4", port=1883, keepalive=60) #Raspberrypi address 

    client.loop_forever()

    #summ = 0
    
