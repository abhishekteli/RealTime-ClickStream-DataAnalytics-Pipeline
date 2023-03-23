from kafka import KafkaProducer
import streamlit as st
import json

producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer = lambda m : json.dumps(m).encode("ascii"))

st.title("Hello from GETMART")
name = st.text_input("Name")
email = st.text_input("Email")
devices = ['Laptops', 'Mobile', 'Computer', 'Tablets']
device = st.selectbox("Please select the Product to buy",devices)


col1, col2 , col3, col4, col5, col6= st.columns(6)

with col1:
    button1 = st.button("Buy Now")

with col6:
    button2 = st.button("Buy Later")


if button1:
    st.write(f"Hello {name} :wave:")
    st.write(f"You have selected to buy {device}")
    st.write(f"Your purchase is successful, we have sent the invoice to your email : {email}")

if button2:
    st.write(f"Hello {name} :wave:")
    st.write(f"You have opted to buy {device} later")
    st.write(f"Your product has been saved in your cart")
    data = {'Name':name,'Email':email,'Device':device}
    producer.send("test",data)
    producer.close()
