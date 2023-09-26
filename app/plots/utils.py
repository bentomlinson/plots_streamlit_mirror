from zipfile import ZipFile

import numpy as np
import pandas as pd


def import_data_from_zipfile(zip_file_path):
    data_dict = dict()
    with ZipFile(zip_file_path) as zf:
        for zipped_file_name in zf.namelist():
            sensor, data_type, _ = zipped_file_name.split(".")
            if sensor not in data_dict.keys():
                data_dict[sensor] = dict()
            with zf.open(zipped_file_name) as f:
                data_dict[sensor][data_type] = pd.read_parquet(f)
    return data_dict


def rename_lidar_columns(df) -> pd.DataFrame:
    sensor = "LIDAR"
    csh = 2  # Maybe data should be imported already with this adjustment

    # Flatten columns and rename heights
    heights = sorted(list(set(df.columns.get_level_values(1))))
    client_heights = [f"{x+csh:.0f}m" for x in heights]
    rename_heights = dict(zip(heights, client_heights))
    df = df.swaplevel(0, 1, axis=1)
    df.rename(columns=rename_heights, level=0, inplace=True)
    df.columns = ["-".join(a) for a in df.columns.to_flat_index()]
    # Add sensor as prefix to columns
    df = df.add_prefix(f"{sensor}")
    return df


def prepare_data_for_plotting(data_dict):
    final_df = pd.DataFrame()
    for sensor in data_dict.keys():
        # Set flagged data to NaN
        mask = data_dict[sensor]["reduced_bool_flags"]["PDA"]
        df = data_dict[sensor]["unflagged_data"].copy()
        df[mask] = np.nan

        # Add sensor to column names
        if sensor == "LIDAR":
            df = rename_lidar_columns(df)
        else:
            df = df.add_prefix(f"{sensor}-")
        final_df = pd.concat([final_df, df], axis=1)
    return final_df


def sum_columns(df, max_col, min_col, new_col_name):
    if set([max_col, min_col]) > set(df.columns):
        return df
    df[new_col_name] = df[max_col] + df[min_col]
    df = df.sort_index(axis=1)
    return df


def diff_columns(df, max_col, min_col, new_col_name):
    if set([max_col, min_col]) > set(df.columns):
        return df
    df[new_col_name] = df[max_col] - df[min_col]
    df = df.sort_index(axis=1)
    return df


def convert_pitch_roll_to_tilt(pitch, roll):
    pitch_rad = np.radians(pitch)
    roll_rad = np.radians(roll)
    angle = np.arctan(np.sqrt(np.tan(roll_rad) ** 2 + np.tan(pitch_rad) ** 2))
    return np.degrees(angle)


def pitch_roll_to_tilt(df, pitch_col, roll_col, new_col_name):
    if set([roll_col, pitch_col]) > set(df.columns):
        return df
    roll_df = df[[roll_col]].copy()
    roll_df[roll_df < 0] = roll_df + 360
    roll_df = roll_df - 180
    # return roll_df
    df[new_col_name] = convert_pitch_roll_to_tilt(df[pitch_col], roll_df[roll_col])
    if df[new_col_name].mean() > 120:
        df[new_col_name] = 180 - df[new_col_name]
    return df


def add_variables(df):
    df = df.copy()
    df = sum_columns(
        df, "AHRS-AHRSpitch_Max", "AHRS-AHRSpitch_Min", "AHRS-AHRSpitch_Sum"
    )
    df = diff_columns(
        df, "AHRS-AHRSroll_Max", "AHRS-AHRSroll_Min", "AHRS-AHRSroll_Diff"
    )
    df = pitch_roll_to_tilt(df, "ADCP-ADCPpitch", "ADCP-ADCProll", "ADCP-ADCPtilt")
    return df


def import_and_prepare_data(zip_file_path):
    data_dict = import_data_from_zipfile(zip_file_path)
    df = prepare_data_for_plotting(data_dict)
    df = add_variables(df)
    return df
