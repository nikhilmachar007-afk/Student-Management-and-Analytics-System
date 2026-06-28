import pandas as pd
from validation import is_dataframe_empty

def display_student_records(dataframe, option, n=None, student_ids=None):
    if  is_dataframe_empty(dataframe):
        print("Dataframe is Empty.")
        return False
    
    n_low=0
    n_high=dataframe.shape[0]

    match option:
        case 1:
            return (dataframe)
        case 2:
            if n>n_low and n<=n_high:
                return (dataframe.sort_values(by="overall_score", ascending=False).head(n))
            else:
                print("Invalid n value.")
                return False
        case 3:
            if n>n_low and n<=n_high:
                return (dataframe.sort_values(by="overall_score", ascending=False).tail(n))
            else:
                print("Invalid n value.")
                return False
        case 4:
            dataframe=dataframe[dataframe["student_id"].isin(student_ids)]
            if not dataframe.empty:
                return (dataframe)
            else:
                print("Invalid Student IDs.")
                return False
        case _:
            print("Invalid Option.")
            return False


def analyze_study_hours(dataframe, option, n=None):
    if is_dataframe_empty(dataframe):
        print("Dataframe is Empty.")
        return False
    
    n_low=0
    n_high=dataframe.shape[0]

    match option:
        case 1:
            if n>n_low and n<=n_high:
                return (dataframe[["student_id", "study_hours"]].nlargest(n,columns="study_hours"))
            else:
                print("Invalid n value.")
                return False
        case 2:
            if n>n_low and n<=n_high:
                return (dataframe[["student_id", "study_hours"]].nsmallest(n,columns="study_hours"))
            else:
                print("Invalid n value.")
                return False
        case 3:
            return ((dataframe["study_hours"].mean()).round(2))
        case _:
            print("Invalid Option.")
            return False
        
def analyze_attendance_percentage(dataframe, option, n=None):
    if is_dataframe_empty(dataframe):
        print("Dataframe is Empty.")
        return False
    
    n_low=0
    n_high=dataframe.shape[0]

    match option:
        case 1:
            if n>n_low and n<=n_high:
                return (dataframe[["student_id", "attendance_percentage"]].nlargest(n,columns="attendance_percentage"))
            else:
                print("Invalid n value.")
                return False
        case 2:
            if n>n_low and n<=n_high:
                return (dataframe[["student_id", "attendance_percentage"]].nsmallest(n,columns="attendance_percentage"))
            else:
                print("Invalid n value.")
                return False
        case 3:
            return (dataframe["attendance_percentage"].mean())
        case _:
            print("Invalid Option.")
            return False
        
def analyze_internet_access(dataframe, option, student_ids=None):
    if is_dataframe_empty(dataframe):
        print("Dataframe is Empty.")
        return False
    
    match option:
        case 1:
            return ((dataframe["internet_access"]=="yes").sum())
        case 2:
            return ((dataframe["internet_access"]=="no").sum())
        case 3:
            dataframe=dataframe[["student_id", "internet_access"]][dataframe.student_id.isin(student_ids)]
            if not dataframe.empty:
                return dataframe
            else:
                return False 
        case _:
            print("Invalid Option.")
            return False
        

def analyze_extra_activities(dataframe, option, student_ids=None):
    if is_dataframe_empty(dataframe):
        print("Dataframe is Empty.")
        return False
    
    match option:
        case 1:
            return ((dataframe["extra_activities"]=="yes").sum())
        case 2:
            return ((dataframe["extra_activities"]=="no").sum())
        case 3:
            dataframe=dataframe[["student_id", "extra_activities"]][dataframe["student_id"].isin(student_ids)]
            if not is_dataframe_empty:
                return dataframe
            else:
                return False
        case _:
            print("Invalid option.")
            return False
        
    
def analyze_subject_performance(dataframe, option, subject=None):
    if is_dataframe_empty(dataframe):
        print("Dataframe is Empty.")
        return False
    
    match option:
        case 1:
            match subject:
                case 1:
                    return (dataframe[["student_id", "overall_score"]][dataframe["overall_score"]==dataframe["overall_score"].max()])
                case 2:
                    return (dataframe[["student_id", "math_score"]][dataframe["math_score"]==dataframe["math_score"].max()])
                case 3:
                    return (dataframe[["student_id", "science_score"]][dataframe["science_score"]==dataframe["science_score"].max()])
                case 4:
                    return (dataframe[["student_id", "english_score"]][dataframe["english_score"]==dataframe["english_score"].max()])
                case _:
                    print("Invalid Subject.")
                    return False
        case 2:
            match subject:
                case 1:
                    return (dataframe[["student_id", "overall_score"]][dataframe["overall_score"]==dataframe["overall_score"].min()])
                case 2:
                    return (dataframe[["student_id", "math_score"]][dataframe["math_score"]==dataframe["math_score"].min()])
                case 3:
                    return (dataframe[["student_id", "science_score"]][dataframe["science_score"]==dataframe["science_score"].min()])
                case 4:
                    return (dataframe[["student_id", "english_score"]][dataframe["english_score"]==dataframe["english_score"].min()])
                case _:
                    print("Invalid Subject.")
                    return False
        case _:
            print("Invalid Option.")
            return False
        
def analyze_average_score(dataframe, option, subject=None):
    if is_dataframe_empty(dataframe):
        print("Dataframe is Empty.")
        return False
    
    match option:
        case 1:
            return (dataframe[["overall_score"]].mean())
        case 2:
            return (dataframe[["math_score", "science_score", "english_score"]].mean())
        case 3:
            match subject:
                case 1:
                    return (dataframe[["math_score"]].mean())
                case 2:
                    return (dataframe[["science_score"]].mean())
                case 3:
                    return (dataframe[["english_score"]].mean())
                case _:
                    print("Invalid Subject.")
                    return False    
        case _:
            print("Invalid Option.")
            return False
        
def analyze_student_grade(dataframe, option, grade=None):
    if is_dataframe_empty(dataframe):
        print("Dataframe is Empty.")
        return False
    
    match option:
        case 1:
            match grade:
                case 1:
                    return (dataframe[["student_id"]][dataframe["final_grade"]=="A"])
                case 2:
                    return (dataframe[["student_id"]][dataframe["final_grade"]=="B"])
                case 3:
                    return (dataframe[["student_id"]][dataframe["final_grade"]=="C"])
                case 4:
                    return (dataframe[["student_id"]][dataframe["final_grade"]=="D"])
                case 5:
                    return (dataframe[["student_id"]][dataframe["final_grade"]=="E"])
                case 6:
                    return (dataframe[["student_id"]][dataframe["final_grade"]=="F"])
                case _:
                    print("Invalid Grade.")
                    return False
        case 2:
            return (dataframe.groupby(["final_grade"])["final_grade"].value_counts(sort=False))
        case 3:
            return ((dataframe.groupby(["final_grade"])["final_grade"].value_counts(sort=False)/len(dataframe)*100).round(2))
        case 4:
            return (dataframe["final_grade"].value_counts().idxmax())
        case 5:
            return (dataframe["final_grade"].value_counts().idxmin())
        case _:
            print("Invalid Option.")
            return False