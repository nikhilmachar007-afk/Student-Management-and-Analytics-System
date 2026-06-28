import pandas as pd
from config import *
from validation import *

def load_data_set(data_file_path):
    if does_file_exists(data_file_path):
        raw_df=pd.read_csv(data_file_path)
        return raw_df
    else:
        return False
    

def str_upper_column(dataframe,column):
    if validate_columns(dataframe, [column]):
        dataframe[column]=dataframe[column].str.upper()
        return dataframe
    else:
        print(f"{column} does not exists. No changes were made")
        return dataframe

def remove_columns(dataframe, columns):
    if validate_columns(dataframe,columns):
        dataframe=dataframe.drop(columns, axis=1)
    else:
        print("Given columns does not exists in the dataframe.")
    return dataframe


def remove_duplicates(dataframe):
    if not validate_duplicates(dataframe):
        dataframe=dataframe.drop_duplicates()
    return dataframe


def drop_null_values(dataframe):
    dataframe=dataframe.dropna(how="any",axis=0)
    return dataframe


def set_category_data(dataframe, columns):
    for column, category, ordered in columns:
        dtype=pd.api.types.CategoricalDtype(categories=category, ordered=ordered)
        dataframe[column]=dataframe[column].astype(dtype)
    return dataframe

def set_student_id_dtype(dataframe):
    dataframe["student_id"]=dataframe["student_id"].astype(int)
    return dataframe

def process_data(data_file_path):
    raw_df=load_data_set(data_file_path)
    if raw_df is False:
        return False
    if not is_dataframe_empty(raw_df):
        cleaned_df=raw_df.copy()
        cleaned_df=str_upper_column(cleaned_df,"final_grade")
        cleaned_df=remove_columns(cleaned_df, unrequired_columns)
        cleaned_df=remove_duplicates(cleaned_df)
        cleaned_df=drop_null_values(cleaned_df)
        cleaned_df=set_student_id_dtype(cleaned_df)
        cleaned_df=set_category_data(cleaned_df, categorical_columns)
    else:
        return False
    
    return cleaned_df
    
