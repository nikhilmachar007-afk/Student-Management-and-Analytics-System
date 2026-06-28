from pathlib import Path

Base_Dir=Path(__file__).resolve().parent.parent

raw_data_path=Base_Dir / "data" / "raw" / "Student_Performance.csv"
cleaned_data_path=Base_Dir / "data" / "processed" / "cleaned_Student_Performance.csv"

required_columns=[
    "student_id",
    "study_hours",
    "attendance_percentage",
    "internet_access",
    "extra_activities",
    "math_score",
    "science_score",
    "english_score",
    "overall_score",
    "final_grade"
]

unrequired_columns=[
    "age",
    "gender",
    "school_type",
    "parent_education",
    "travel_time",
    "study_method"
]

categorical_columns=[
    ("internet_access",["no", "yes"], False),
    ("extra_activities",["no", "yes"], False ),
    ("final_grade",["A","B","C","D","E","F"], True)
    ]

def get_student_data():
    Student_id=int(input("Enter Student ID: "))
    study_hours=float(input("Enter Study Hours: "))
    attendance_percentage=float(input("Enter attendance Percentage: "))
    internet_access=input("Enter Internet Access (yes/no): ").strip().lower()
    extra_activities=input("Enter Extra Activities (yes/no): ").strip().lower()
    math_score=int(input("Enter Math Score: "))
    science_score=int(input("Enter Math Score: "))
    english_score=int(input("Enter Math Score: "))
    final_grade=input("Enter Grade: ").strip().upper()
    
    student_data={
        "student_id":Student_id,
        "study_hours":study_hours,
        "attendance_percentage":attendance_percentage,
        "internet_access":internet_access,
        "extra_activities":extra_activities,
        "math_score":math_score,
        "science_score":science_score,
        "english_score":english_score,
        "overall_score":0.0,
        "final_grade":final_grade
    }

    return student_data