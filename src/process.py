import pandas as pd

def add_student(dataframe, student_data):
    if not student_data["student_id"] in dataframe["student_id"].values:
        if student_data["student_id"]<=0:
            print("Invalid Student ID")
            return False
    else:
         print("Student ID already Exists.")
         return False
    
    if not ((student_data["study_hours"]>0) and (student_data["study_hours"]<=24)):
            print("Invalid Study hours.")
            return False
    
    if not ((student_data["attendance_percentage"]>=0 )and (student_data["attendance_percentage"]<=100)):
            print("Invalid attendance percentage.")
            return False
    
    if not (student_data["internet_access"] in ["yes","no"]):
        print("Invalid Internet Access.")
        return False  

    if not (student_data["extra_activities"] in ["yes","no"]):
         print("Invalid Extra Activities.")
         return False

    if not ((student_data["math_score"]>=0) and (student_data["math_score"]<=100)):
         print("Invalid Maths Score.")
         return False

    if not ((student_data["science_score"]>=0) and (student_data["science_score"]<=100)):
         print("Invalid Science Score.")
         return False

    if not ((student_data["english_score"]>=0) and (student_data["english_score"]<=100)):
         print("Invalid English Score.")
         return False  

    student_data["overall_score"]=round((student_data["math_score"]+student_data["science_score"]+student_data["english_score"])/3, 1)

    if not student_data["final_grade"] in ["A", "B", "C", "D", "E", "F"]:
         print("Invalid Final Grade.")
         return False
  
    dataframe.loc[len(dataframe)]=student_data  
    return dataframe

def delete_student(dataframe, student_id):
    if student_id in dataframe["student_id"].values:
        dataframe=dataframe.drop(dataframe[dataframe["student_id"]==student_id].index)
        dataframe=dataframe.reset_index(drop=True)
        return dataframe
    else:
        print("Delete Unsuccessfull.")
        return False
    

def update_student(dataframe, updated_student_data):
     if updated_student_data["student_id"]>0:
          if not updated_student_data["student_id"] in dataframe["student_id"].values:
               print("Student ID does not Exists.")
               return False
     else:
          print("Invalid Student ID.")
          return False

     if not ((updated_student_data["study_hours"]>0) and (updated_student_data["study_hours"]<=24)):
               print("Invalid Study hours.")
               return False
     
     if not ((updated_student_data["attendance_percentage"]>=0 )and (updated_student_data["attendance_percentage"]<=100)):
               print("Invalid attendance percentage.")
               return False
     
     if not (updated_student_data["internet_access"] in ["yes","no"]):
          print("Invalid Internet Access.")
          return False  

     if not (updated_student_data["extra_activities"] in ["yes","no"]):
          print("Invalid Extra Activities.")
          return False

     if not ((updated_student_data["math_score"]>=0) and (updated_student_data["math_score"]<=100)):
          print("Invalid Maths Score.")
          return False

     if not ((updated_student_data["science_score"]>=0) and (updated_student_data["science_score"]<=100)):
          print("Invalid Science Score.")
          return False

     if not ((updated_student_data["english_score"]>=0) and (updated_student_data["english_score"]<=100)):
          print("Invalid English Score.")
          return False  

     updated_student_data["overall_score"]=round((updated_student_data["math_score"]+updated_student_data["science_score"]+updated_student_data["english_score"])/3, 1)

     if not updated_student_data["final_grade"] in ["A", "B", "C", "D", "E", "F"]:
          print("Invalid Final Grade.")
          return False
     
     index=dataframe[dataframe["student_id"] == updated_student_data["student_id"]].index 
     dataframe.loc[index[0]]=updated_student_data
     return dataframe

     
