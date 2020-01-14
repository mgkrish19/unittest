def test_with_df(spark_session):
        df1 = spark_session.createDataFrame(data=[[1, 'a'], [2, 'b']], schema=['c1', 'c2'])
        df2 = spark_session.read.csv('/home/hadoop/samplefile.csv', header=False, inferSchema=True, sep=',')
        assert df1.count() ==  2
        assert df2.count() == 10
