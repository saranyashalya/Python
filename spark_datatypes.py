from pyspark.sql.types import IntegerType, FloatType, ArrayType
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
import pandas as pd

spark = SparkSession.builder.appName('Spark_DT').getOrCreate()
df = pd.DataFrame(data = {
    "integers" : [1,2,3],
    "float" : [-1.0, 0.5, 2.7],
    "integer_arrays" : [[1,2],[3,4,5],[6,7,8,9]]
})

print(df)
df = spark.createDataFrame(df)
#df.printSchema()
#df.show()

def square(x):
    return x**2

square_udf_int = udf(lambda x : square(x), IntegerType())
square_udf_float = udf(lambda x: square(x), FloatType())

df.select('integers','float', square_udf_int('integers').alias('Int squared'), 
          square_udf_float('float').alias('Float squared')).show()


## Composite type output

def square(val):
    return [float(x)**2 for x in val]
square_udf_array = udf(lambda x : square(x), ArrayType(FloatType()))

df.select('integer_arrays', square_udf_array('integer_arrays').alias('Array squared')).show()