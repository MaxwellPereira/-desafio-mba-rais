from pyspark.sql import SparkSession 
from pyspark.sql import functions as f

# Cria objeto da Spark Session
spark = (SparkSession.builder.appName("DeltaExercise")
    .config("spark.jars.packages", "io.delta:delta-core_2.12:1.0.0")
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
    .getOrCreate()
)

# Importa o modulo das tabelas delta
from delta.tables import *

# Leitura de dados

# Leitura de dados
rais = (
    spark.read.format("csv")
    .option("inferSchema", True)
    .option("header", True)
    .option("delimiter", ";")
    .option("encodinf", "latin1")
    .load("s3://datalake-maxwell-igti-mba/raw-data/rais")
)

rais.printSchema()

print("Writing delta table...")
(
    rais
    .write.mode('overwrite')
    .format('delta')
    .partitionBy('year')
    .save("s3://datalake-mba-igti-tf/staging-zone/rais")
)