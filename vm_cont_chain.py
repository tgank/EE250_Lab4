#Tali Gankin
#https://github.com/tgank/EE250_Lab4/tree/main 
import paho.mqtt.client as mqtt
import time

USERNAME = "asfox"
BROKER_IP = "172.20.10.2" #my rpi not working so borrowed a friends
PING_TOPIC = f"{USERNAME}/ping"
PONG_TOPIC = f"{USERNAME}/pong"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(PING_TOPIC)
    print("Subscribed to", PING_TOPIC)

def on_message(client, userdata, msg):
    try:
        n = int(msg.payload.decode().strip())
    except ValueError:
        print("Got non-integer payload:", msg.payload)
        return

    n2 = n + 1
    print(f"Received on {msg.topic}: {n} -> publishing {n2} to {PONG_TOPIC}")
    client.publish(PONG_TOPIC, str(n2))

if __name__ == "__main__":
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_IP, 1883, 60)
    client.loop_start()

    while True:
        time.sleep(1)
