from pyspark import HiveContext
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

def quiet_py4j():
    """ turn down spark logging for the test context """
    logger = logging.getLogger('py4j')
    logger.setLevel(logging.WARN)

@pytest.fixture(scope="session",
            params=[pytest.mark.spark_local('local'),
                    pytest.mark.spark_yarn('yarn')])
def spark_context(request):
    if request.param == 'local':
        conf = (SparkConf()
                .setMaster("local[2]")
                .setAppName("pytest-pyspark-local-testing")
                )
    elif request.param == 'yarn':
        conf = (SparkConf()
                .setMaster("yarn-client")
                .setAppName("pytest-pyspark-yarn-testing")
                .set("spark.executor.memory", "1g")
                .set("spark.executor.instances", 2)
                )
    request.addfinalizer(lambda: sc.stop())

    sc = SparkContext(conf=conf)
    return sc

@pytest.fixture(scope="session")
def hive_context(spark_context):
    return HiveContext(spark_context)

@pytest.fixture(scope="session")
def streaming_context(spark_context):
    return StreamingContext(spark_context, 1)
