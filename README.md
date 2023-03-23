# RealTime-ClickStream-DataAnalytics-Pipeline

This project is a real-time streaming data engineering project that captures clickstream data from a self-built e-commerce website and processes it in real-time using Apache Kafka, Apache Spark Streaming, and Apache Cassandra. The project consists of two Spark applications: one that cleans and processes the data in real-time and loads it into Cassandra, and another that identifies frequent visitors to the website and sends them personalized email offers. Streamlit is used to build the e-commerce website.


## Technologies Used

The following technologies were used in the implementation of this project:

Apache Kafka: A distributed streaming platform that allows you to publish and subscribe to streams of records.
Apache Spark Streaming: A scalable and fault-tolerant stream processing engine that allows you to process real-time data streams.
Apache Cassandra: A distributed NoSQL database that provides high availability and scalability.
Streamlit: An open-source app framework used to build the e-commerce website.

## Project Architecture
The project consists of the following components:

Clickstream data source: The project captures clickstream data from a self-built e-commerce website.
Apache Kafka: The clickstream data is then ingested into an Apache Kafka topic in real-time.
Spark Streaming application 1: This Spark application reads the data from the Kafka topic, cleans and processes it in real-time, and then loads it into Apache Cassandra.
Spark Streaming application 2: This Spark application reads the data from Cassandra, identifies frequent visitors to the website, and sends them personalized email offers.

## Setup and Configuration
To run this project, you will need to set up and configure the following components:

Apache Kafka
Apache Spark
Apache Cassandra
Streamlit
You will also need to configure the Spark Streaming applications to connect to the Kafka and Cassandra clusters.

## Running the Project
Once you have set up and configured the components, you can run the project as follows:

Start the Kafka cluster.
Start the Spark Streaming application 1 to ingest and process the clickstream data in real-time.
Start the Spark Streaming application 2 to identify frequent visitors and send them personalized email offers.
Launch the Streamlit e-commerce website.

## Conclusion
This real-time streaming data engineering project demonstrates how you can use Apache Kafka, Apache Spark Streaming, Apache Cassandra, and Streamlit to process and analyze clickstream data in real-time. The project can be extended to include additional processing steps and analysis, depending on the requirements of your use case.
