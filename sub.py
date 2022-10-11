import paho.mqtt.client as mqtt_client
import random
import time

def on_message(client, userdata, message):
    data = str(message.payload.decode('utf-8'))
    nickname = message.topic.split('/')[1]
    print(f"{nickname}: {data}")

#misquitte
broker = "broker.emqx.io"

client = mqtt_client.Client(f'lab {random.randint(10000, 99999)}')
client.on_message = on_message

try:
    client.connect(broker)
except Exception:
    print("Connection failed, check network")
    exit()

client.loop_start()
client.subscribe('ls/+')
print("Subscribing!")
time.sleep(600)
client.disconnect()
client.loop_stop()
print('Stop communication')
#while not client.is_connected()    