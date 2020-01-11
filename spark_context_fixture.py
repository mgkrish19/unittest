import pytest
from pyspark import SparkConf,SparkContext,HiveContext,

@pytest.fixture(scope="session")
def spark_context(request):
    conf = (SparkConf().setMaster("local[2]").setAppName("pytest-pyspark-local-testing"))
	sc = SparkContext(conf=conf)
    request.addfinalizer(lambda: sc.stop())
    return sc

	
@pytest.fixture(scope="session")
def hive_context(spark_context):
    return HiveContext(spark_context)
