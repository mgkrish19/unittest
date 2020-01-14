def test_with_df(spark_session):
        df1 = spark_session.createDataFrame(data=[[1, 'a'], [2, 'b']], schema=['c1', 'c2'])
        assert df1.count() == 5 
