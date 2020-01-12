df = spark.read.csv('s3://krishpocone/samplefile.csv', header=False, inferSchema=True, sep=',')
df.count()
df.dtypes
df.take(5)
df_t = df.select('_c0','_c1','_c2', '_c3', '_c4', '_c5')
df_t.take(1)
df_t = df_t.withColumnRenamed('_c0', 'newid').withColumnRenamed('_c1', 'newcolumn')
