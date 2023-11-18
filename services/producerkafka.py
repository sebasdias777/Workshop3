from kafka import KafkaProducer
#from confluent_kafka import Producer
from json import dumps, loads
import pandas as pd 
from services.transformations import transformaciones

def kafka_producer():
    df = transformaciones()
    producer = KafkaProducer(
        value_serializer = lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers = ['localhost:9092'],
    )

    for index, row in df.iterrows():
        mensaje = row.to_dict()
        producer.send("Workshop3", value=mensaje)
        print("message sent")