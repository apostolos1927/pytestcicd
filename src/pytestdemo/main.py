from pyspark.sql import SparkSession, DataFrame


def get_taxis(spark: SparkSession) -> DataFrame:
    return spark.read.table("samples.nyctaxi.trips")


def remove_record_by_id(df: DataFrame, id_column: str, id_to_remove: int) -> DataFrame:
    # Ensure the ID column exists in the DataFrame
    if id_column not in df.columns:
        raise ValueError(f"The column '{id_column}' does not exist in the DataFrame.")
    return df.filter(df[id_column] != id_to_remove)


# Create a new Databricks Connect session. If this fails,
# check that you have configured Databricks Connect correctly.
# See https://docs.databricks.com/dev-tools/databricks-connect.html.
def get_spark() -> SparkSession:
    try:
        from databricks.connect import DatabricksSession

        return DatabricksSession.builder.serverless(True).getOrCreate()
    except ImportError:
        return SparkSession.builder.getOrCreate()


def main():
    get_taxis(get_spark()).show(5)


if __name__ == "__main__":
    main()
