import requests
import json
import random
import time
import configparser
from paho.mqtt import client as mqtt_client


cnf = configparser.ConfigParser()  
cnf.read("pythonmqtt.ini") 

broker = cnf["Pythonmqtt"]["broker"]
port = cnf["Pythonmqtt"].getint("port")
vhost = cnf["Pythonmqtt"]["vhost"]
topic = cnf["Pythonmqtt"]["topic"]
username = cnf["Pythonmqtt"]["username"]
password = cnf["Pythonmqtt"]["password"]
time_update =cnf["Pythonmqtt"].getint("time_update")

# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 1000)}'

headers = {
    'Content-Type': 'application/json',
}


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(vhost + ":" + username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client

def publish(client):
    msg_count = 0
    while True:
        time.sleep(time_update)
        msg = f"messages: {msg_count}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()

