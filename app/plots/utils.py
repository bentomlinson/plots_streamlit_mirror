"""Helper functions for plotting scripts."""

import pandas as pd

def import_df(file_path):
    TIMESTAMP_LABEL = "timestamp"
    TIMESTAMP_FORMAT = "%d-%m-%Y %H:%M"
    
    df = pd.read_csv(file_path, header=1)
    df.drop(0, axis=0, inplace=True)
    df[TIMESTAMP_LABEL] = pd.to_datetime(df[TIMESTAMP_LABEL], format=TIMESTAMP_FORMAT)
    df.set_index(TIMESTAMP_LABEL, inplace=True)
    df = df.apply(pd.to_numeric)
    return df
