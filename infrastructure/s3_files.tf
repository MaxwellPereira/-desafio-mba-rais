resource "aws_s3_bucket_object" "delta_insert_rais" {
  bucket = aws_s3_bucket.dl.id
  key    = "emr-code/pyspark/01_delta_spark_insert_rais.py"
  acl    = "private"
  source = "../etl/01_delta_spark_insert_rais.py"
  etag   = filemd5("../etl/01_delta_spark_insert_rais.py")
}

resource "aws_s3_bucket_object" "delta_insert_enem" {
  bucket = aws_s3_bucket.dl.id
  key    = "emr-code/pyspark/01_delta_spark_insert_enem.py"
  acl    = "private"
  source = "../etl/01_delta_spark_insert_enem.py"
  etag   = filemd5("../etl/01_delta_spark_insert_enem.py")
}

