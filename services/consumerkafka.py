from kafka import  KafkaConsumer
#from confluent_kafka import Producer
from json import dumps, loads
import joblib 
import pandas as pd 
from services.db import insert


def kafka_consumer():
    consumer = KafkaConsumer(
        'Workshop3',
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group-1',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
        )

    loaded_model = joblib.load('C:/Users/CHZ/Desktop/ETL/Workshop3/modelo.pkl')

    for m in consumer:
        mensaje = m.value
        print(m.value)
        df = pd.DataFrame.from_dict([mensaje])
        prediccion_happiness = loaded_model.predict(df[['GDP per capita', 'Social support', 'Healthy life expectancy', 'Freedom']])
        df["Prediccion_H"] = prediccion_happiness
        df['Prediccion_H'] = df['Prediccion_H'].round(3)
        print(df)
        insert(df)