# Customer-Analytics-

Customer Analytics Retention:

Ecommerce UI : 
Our generated clicks on UI is sending the data based on clicks to the confulent kafka which is producer and from kafka, we fetch the data into some other programs and process the data and send it to NoSQL db mongodb.
Once our data is available after processing in mongodb, we pull the data and connect to powerbi/ui.

Three system: 
1)Producer (UI + kafka)
2)Process + MongoDB
3)Analytics UI/Dashboard

get the data and sending the event to kafka topic producer.

now part 2,we created a processor which will try to listen to kafka topic(consumer_click_data) and store in mongodb.

customer_data_process.py for consuming the data.
first connect mongodb and then creating consumer object
Consumer will establish the communication and it will subscribe the kafka topic "customer_click_data" in which data are sent by the producer.
Producers is sending the data and consumer will listen and consume data. Once it will consume the data.Read the data from from kafka and send it to mongodb.

Both is live. Producer and consumer.

calling the processor. MongoDB is a consumer.

thirdly we connected mongodb to powerbi by proving mongo uri.



=============================================================
Energy Consumption Analytics:
Data Source: Smart Meter,Weather data, Grid performance metrics,
Pipeline: Kafka for smart meter readings, spark streaming, spark streaming for usage analysis, MongoDB for time-series data, Snowflake for reporting.
Analytics : PowerBI for consumption patterns, Streamlit for energy optimization
Peak load prediction,



