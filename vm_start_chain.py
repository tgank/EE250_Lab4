#Tali Gankin
#https://github.com/tgank/EE250_Lab4/tree/main 
import paho.mqtt.client as mqtt
import time

USERNAME = "asfox"
BROKER_IP = "172.20.10.2"
PING_TOPIC = f"{USERNAME}/ping"
PONG_TOPIC = f"{USERNAME}/pong"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(PONG_TOPIC)
    print("Subscribed to", PONG_TOPIC)

def on_message(client, userdata, msg):
    try:
        n = int(msg.payload.decode().strip())
    except ValueError:
        print("Got non-integer payload:", msg.payload)
        return

    n2 = n + 1
    print(f"Received on {msg.topic}: {n} -> publishing {n2} to {PING_TOPIC}")
    time.sleep(1)
    client.publish(PING_TOPIC, str(n2))

if __name__ == "__main__":
    start = int(input("Enter starting integer: "))

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(BROKER_IP, 1883, 60)
    client.loop_start()
    time.sleep(1)
    
    print(f"Publishing initial {start} to {PING_TOPIC}")
    client.publish(PING_TOPIC, str(start))
    time.sleep(1)

    # keep program alive
    while True:
        time.sleep(1)
