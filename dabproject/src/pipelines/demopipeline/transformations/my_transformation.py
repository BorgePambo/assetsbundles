from pyspark import pipelines as dp


@dp.table
def transform():
    return spark.range(10)