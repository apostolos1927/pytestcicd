from src.pytestdemo.main import get_taxis, get_spark
import pytest
from pandas.testing import assert_frame_equal
import pandas as pd
from src.pytestdemo.main import remove_record_by_id


@pytest.fixture
def sample_dataframe():
    data = [
        {"ID": 1, "Name": "Alice", "Age": 23},
        {"ID": 2, "Name": "Bob", "Age": 25},
        {"ID": 3, "Name": "Charlie", "Age": 30},
        {"ID": 4, "Name": "David", "Age": 29},
    ]

    return get_spark().createDataFrame(data)


def test_remove_record_by_id(sample_dataframe):
    id_to_remove = 2
    filtered_df = remove_record_by_id(
        df=sample_dataframe, id_column="ID", id_to_remove=id_to_remove
    )
    filtered_df_pandas = filtered_df.toPandas()
    expected_data = {
        "ID": [1, 3, 4],
        "Name": ["Alice", "Charlie", "David"],
        "Age": [23, 30, 29],
    }
    expected_df = pd.DataFrame(expected_data)
    assert_frame_equal(
        filtered_df_pandas.sort_index(axis=1), expected_df.sort_index(axis=1)
    )


def test_main():
    taxis = get_taxis(get_spark())
    assert taxis.count() > 5
