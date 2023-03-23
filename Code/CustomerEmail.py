from pyspark.sql import SparkSession
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def email(row):

    if row.counter >= 3:

        # Set up the email parameters
        sender_email = "your_eamil"
        receiver_email = row.email
        password = "your_password"
        subject = "Discount Offers on " + row.device
        message = f"Hello {row.name}, we have some amazing discounts for you on {row.device}.\n The product has now 50% discount"

        # Create the message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Add the message body
        msg.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, password)

        # Send the email
        text = msg.as_string()
        server.sendmail(sender_email, receiver_email, text)
        server.quit()

        print('Email sent successfully')


def main():
    spark = SparkSession.builder.appName("SparkTest") \
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .config("spark.cassandra.connection.host", "localhost") \
        .config("spark.cassandra.connection.port", "9042") \
        .config("spark.cassandra.output.consistency.level", "LOCAL_QUORUM") \
        .config("spark.cassandra.input.consistency.level", "LOCAL_QUORUM") \
        .getOrCreate()

    input_df = spark \
        .read \
        .format("org.apache.spark.sql.cassandra") \
        .option("table", "users") \
        .option("keyspace", "clickstream_data") \
        .load()

    input_df.foreach(email)

if __name__ == "__main__":
    main()