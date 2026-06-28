import pandas as pd
import os
from config import *
from validation import *

def does_file_exists(data_file_path):
    if not os.path.exists(data_file_path):
        return False
    return True

def is_dataframe_empty(dataframe):
    if dataframe.empty:
        return True
    else:
        return False
   
def validate_columns(dataframe, columns):
    for column in columns:
        if not column in dataframe.columns:
           return False
    return True

def validate_duplicates(dataframe):
    if (dataframe.duplicated().sum())!=0:
        return False
    return True
    

def validate_student_id(dataframe):
    if (dataframe.student_id.isna().sum())!=0:
        print("Student ID is NaN.")
        return False
    for ID in dataframe.student_id:
        if ID<1:
            print("Invalid student IDs exists.")
            return False
    return True


def validate_attendance_percentage(dataframe):
    if (dataframe.attendance_percentage.isna().sum())!=0:
        print("Attendance percentage has Null values.")
        return False
    for percentage in dataframe.attendance_percentage:
        if percentage<0 or percentage>100:
            print("Invalid Attnedance percentage exists.")
            return False
    return True

def validate_study_hours(dataframe):
    if (dataframe.study_hours.isna().sum())!=0:
        print("Study hours has Null values.")
        return False
    for hour in dataframe.study_hours:
        if hour<0 or hour>100:
            print("Invalid Study Hours exists.")
            return False
    return True 

def validate_internet_access(dataframe):
    if (dataframe.internet_access.isna().sum())!=0:
        print("Internet access has Null values.")
        return False
    for status in dataframe.internet_access:
        if not status in ["yes","no"]:
            print("Invalid Internet Access exists.")
            return False
    return True 

def validate_extra_activities(dataframe):
    if (dataframe.extra_activities.isna().sum())!=0:
        print("Extra Activities has Null values.")
        return False
    for status in dataframe.extra_activities:
        if not status in ["yes", "no"]:
            print("Invalid Extra Activities exists.")
            return False
    return True

def validate_score(dataframe):
    columns=["math_score","science_score","english_score","overall_score" ]
    invalid_columns=""
    status=False
    for column in columns:
        if (dataframe[column].isna().sum())!=0:
            invalid_columns=invalid_columns+column+" "
    if len(invalid_columns)!=0:
        status=True
        print(f"{invalid_columns} have Null values.")

    invalid_columns=""

    for column in columns:
        for score in dataframe[column]:
            if score<0 or score>100:
                invalid_columns=invalid_columns+column+" "
                break
    if len(invalid_columns)!=0:
        print(f"{invalid_columns} and have Invalid values.")
        return False
    else:
        if status:
            return False
        else:
            return True

def validate_final_grade(dataframe):
    if dataframe.final_grade.isna().sum()!=0:
        print("Final Grade has null values.")
        return False
    grades=["A","B","C","D","E","F"]
    for grade in dataframe.final_grade:
        if not grade in grades:
            print("Final grades has Invalid values.")
            return False
    return True


def validate_dataframe(dataframe, columns):
    if is_dataframe_empty(dataframe):
        print("Dataframe is Empty.")
        return False
    
    if not validate_columns(dataframe, columns):
        return False
    
    if not validate_duplicates(dataframe):
        return False
    
    if not validate_student_id(dataframe):
        return False
    
    if not validate_attendance_percentage(dataframe):
        return False
    
    if not validate_study_hours(dataframe):
        return False
    
    if not validate_internet_access(dataframe):
        return False
    
    if not validate_extra_activities(dataframe):
        return False
    
    if not validate_score(dataframe):
        return False

    if not validate_final_grade(dataframe):
        return False
    
    return True