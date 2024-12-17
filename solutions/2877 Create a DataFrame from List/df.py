import pandas as pd


def create_dataframe(student_data):
    cols = ["student_id", "age"]
    return pd.DataFrame(student_data, columns=cols)
