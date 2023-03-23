from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.functions import *
import json


def main():

    spark = SparkSession.builder.appName("SparkTest")\
        .config("spark.streaming.stopGracefullyOnShutdown", "true") \
        .config("spark.cassandra.connection.host", "localhost") \
        .config("spark.cassandra.connection.port", "9042") \
        .config("spark.cassandra.output.consistency.level", "LOCAL_QUORUM") \
        .config("spark.cassandra.input.consistency.level", "LOCAL_QUORUM") \
        .getOrCreate()

    input_df = spark \
        .readStream \
        .format("kafka") \
        .option("kafka.bootstrap.servers","localhost:9092") \
        .option("subscribe", "test") \
        .option("startingOffsets", "earliest") \
        .load()

    schema = StructType(
        [
            StructField("Name", StringType()),
            StructField("Email", StringType()),
            StructField("Device", StringType())
        ]
    )

    output_df = input_df.select(from_json(col("value").cast("string"), schema).alias("data"))
    cassandra_df = output_df.selectExpr("data.Name as name", "data.Email as email", "data.Device as device")
    cassandra_df = cassandra_df.withColumn("counter", lit(1))

    query = cassandra_df \
        .writeStream \
        .format("org.apache.spark.sql.cassandra") \
        .option("checkpointLocation", "checkpoints") \
        .option("table", "users") \
        .option("keyspace", "clickstream_data") \
        .outputMode("append") \
        .start()

    # start the query and wait for it to terminate
    query.awaitTermination()


if __name__ == "__main__":
    main()