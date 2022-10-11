import paho.mqtt.client as mqtt_client
import random
import serial
import time

check_time = 0.2
real_time = time.time()

def get_connection(port):
    ser = serial.Serial(port, timeout=1)
    return ser

def process(ser):
    global check_time
    global real_time
    data = ser.read()
    if(data == b"1"):
        print(time.time() - real_time)
        if(time.time() - real_time > check_time):
            print("Данные отправлены!")
            client.publish("TebloevKlypin",random.randint(0, 9))
    elif(data == b"0"):
        real_time = time.time()    
        
    

if __name__ == '__main__':
    ser = get_connection('/dev/ttyACM0')
    broker = 'broker.emqx.io'
    client = mqtt_client.Client(f'lab_{random.randint(10000,99999)}')
    
    try:
        client.connect(broker)
    except Exception:
        print('Failed to connect')
        exit()
    
    print("Publishing...")
    while(True):
        process(ser)