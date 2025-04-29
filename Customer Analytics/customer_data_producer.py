import json
import streamlit as st
import time  
from confluent_kafka import Producer


kafka_config = {
    'bootstrap.servers': 'pkc-921jm.us-east-2.aws.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'SWJ4E7VFKNXBEOHF',
    'sasl.password': 'gpbsFTK2INYCNIYNNIWYiVldnAeTdpiXZFq4pzsXUK6hjCFaApWat7j5pFqvhY25',
    'group.id': 'sentiment_analysis_group',
    'auto.offset.reset': 'earliest'
}

KAFKA_TOPIC  = "customer_click_data"
producer = Producer(kafka_config)

st.title("Customer Click Analytics")
user_id = st.number_input("User ID", min_value=1, max_value=1000000, step=1)
activity = st.selectbox("Activity", ["view_product", "add_to_cart", "checkout", "search", "wishlist"])
product = st.selectbox("Product", ["Laptop", "Mobile", "Headphone", "Smartwatch", "Camera", "Tablet"])

def send_event():
    event = {
        "user_id": user_id,
        "activity": activity,
        "product": product,
        "timestamp": int(time.time())
    }
    
    producer.produce(KAFKA_TOPIC, key=str(user_id), value=json.dumps(event))
    producer.flush()
    st.success(f"Sent this event: {event}")
    
if st.button("Send Data"):
    send_event()
    