import pandas as pd
import time
from config import raw_data_path, cleaned_data_path, get_student_data
from validation import validate_dataframe, does_file_exists
from data_processing import process_data
from process import *
from charts import *
from analysis import *


if not does_file_exists(cleaned_data_path):
    Dataframe=process_data(raw_data_path)
else:
    Dataframe=process_data(cleaned_data_path)

if not validate_dataframe(Dataframe, Dataframe.columns):
    print("Dataset is Not Valid. ")
    exit(0)

if not does_file_exists(cleaned_data_path):
    Dataframe.to_csv(cleaned_data_path, index=False)


print("===================================================")
print("STUDENT MANAGEMENT AND PERFORMANCE ANALYTICS SYSTEM")
print("===================================================")

while True:
    print("------------------------")
    print("-------MAIN MENU--------")
    print("------------------------")
    print("1. Manage Student Records.")
    print("2. Analyze Student Records.")
    print("3. Generate Charts.")
    print("4. View Dataset.")
    print("5. Exit.")

    try:
        main_option=int(input("Enter your option: "))
    except ValueError:
        print("Invalid Option Input. Try Again.")
        continue

    match main_option:
        case 1:
            while True:
                print("------------------------")
                print("Manage Students Records.")
                print("------------------------")
                print("1. Add Student.")
                print("2. Delete Student.")
                print("3. Update Student.")
                print("4. Back.")


                try:
                    choice1=int(input("Enter Your Choice: "))
                except ValueError:
                    print("Invalid Choice Input. Try Again.")
                    continue

                match choice1:
                    case 1:
                        student_data=get_student_data()
                        df=add_student(Dataframe, student_data)
                        if df is not False:
                            Dataframe=df
                            Dataframe.to_csv(cleaned_data_path, index=False)
                            print("Student Record added Successfully.")
                    case 2:
                        try:
                            student_id=int(input("Enter Student ID: "))
                        except ValueError:
                            print("Invalid n value. Try Again")
                            continue

                        df=delete_student(Dataframe, student_id)
                        if df is not False:
                            Dataframe=df
                            Dataframe.to_csv(cleaned_data_path, index=False)
                            print("Student Record Deleted Successfully.")
                    case 3:
                        updated_student_data=get_student_data()
                        df=update_student(Dataframe, updated_student_data)
                        if df is not False:
                            Dataframe=df
                            Dataframe.to_csv(cleaned_data_path, index=False)
                            print("Student Record Updated Successfully.")
                    case 4:
                        break
                    case _:
                        print("Invalid Choice Input. Try Again.")
        case 2:
            while True:
                print("------------------------")
                print("Analyze Student Records.")
                print("------------------------")
                print("1. Student Records Analysis.")
                print("2. Study Hours Analysis.")
                print("3. Attendance Analysis.")
                print("4. Internet Access Analysis.")
                print("5. Extra Activities Analysis.")
                print("6. Subject Performance Analysis.")
                print("7. Average Scores Analysis.")
                print("8. Grade Analysis.")
                print("9. Back.")

                try:
                    choice2=int(input("Enter Your Option: "))
                except ValueError:
                    print("Invalid Choice Input. Try Again.")
                    continue

                match choice2:
                    case 1:
                        print("-------------------------")
                        print("Student Records Analysis.")
                        print("-------------------------")
                        print("1. Display All Students.")
                        print("2. Display Top N Students.")
                        print("3. Display Bottom N Students.")
                        print("4. Display Student by Student IDs.")
                        print("5. Back.")

                        while True:
                            try:
                                choice2_1=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid choice Input. Try Again.")
                                continue

                            match choice2_1:
                                case 1:
                                    df=display_student_records(Dataframe, 1)
                                    if df is not False:
                                        print(df)
                                case 2:
                                    try:
                                        n=int(input("Enter N value: "))
                                    except ValueError:
                                        print("Invalid n Value. try again.")
                                        continue
                                    df=display_student_records(Dataframe, 2, n)
                                    if df is not False:
                                        print(df)
                                case 3:
                                    try:
                                        n=int(input("Enter N value: "))
                                    except ValueError:
                                        print("Invalid n Value. try again.")
                                        continue

                                    df=display_student_records(Dataframe, 3, n)
                                    if df is not False:
                                        print(df)
                                case 4:
                                    try:
                                        student_ids=tuple(map(int,input("Enter Student IDs (eg:1,2,3,...): ").strip().split(",")))
                                    except ValueError:
                                        print("Invalid Input. Try again.")
                                        continue
                                    df=display_student_records(Dataframe, 4, None ,student_ids)
                                    if df is not False:
                                        print(df)
                                case 5:
                                    break
                                case _:
                                    print("Invalid Choice Input.")                               
                    case 2:
                        print("----------------------")
                        print(" Study Hours Analysis.")
                        print("----------------------")
                        print("1. N Students with Highest Study Hours.")
                        print("2. N Students with Lowest Study Hours.")
                        print("3. Average Study Hours.")
                        print("4. Back.")
                        
                        while True:
                            try:
                                choice2_2=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid choice Input. Try Again.")
                                continue

                            match choice2_2:
                                case 1:
                                    try:
                                        n=int(input("Enter n Value: "))
                                    except ValueError:
                                        print("Invalid n Value. Try Again.")
                                        continue
                                    df=analyze_study_hours(Dataframe, 1, n)
                                    if df is not False:
                                        print(df)
                                case 2:
                                    try:
                                        n=int(input("Enter n Value: "))
                                    except ValueError:
                                        print("Invalid n Value. Try Again.")
                                        continue
                                    df=analyze_study_hours(Dataframe, 2, n)
                                    if df is not False:
                                        print(df)
                                case 3:
                                    df=analyze_study_hours(Dataframe, 3)
                                    if df is not False:
                                        print(f"Average Study Hours: {df}")
                                case 4:
                                    break
                                case _:
                                    print("Invalid Choice Input.")
                    case 3:
                        print("--------------------")
                        print("Attendance Analysis.")
                        print("--------------------")
                        print("1. N Students with Highest Attendance.")
                        print("2. N Students with Lowest Attendance.")
                        print("3. Average Attendance.")
                        print("4. Back.")

                        while True:
                            try:
                                choice2_3=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid choice Input. Try Again.")
                                continue

                            match choice2_3:
                                case 1:
                                    try:
                                        n=int(input("Enter n value: "))
                                    except ValueError:
                                        print("Invalid n Value. Try Again")
                                        continue
                                    df=analyze_attendance_percentage(Dataframe, 1, n)
                                    if df is not False:
                                        print(df)
                                case 2:
                                    try:
                                        n=int(input("Enter n value: "))
                                    except ValueError:
                                        print("Invalid n Value. Try Again")
                                        continue
                                    df=analyze_attendance_percentage(Dataframe, 2, n)
                                    if df is not False:
                                        print(df)
                                case 3:
                                    df=analyze_attendance_percentage(Dataframe, 3)
                                    if df is not False:
                                        print(f"Average Attendance Percentage: {df}")
                                case 4:
                                    break
                                case _:
                                    print("Invalid Choice Input.")
                    case 4:
                        print("-------------------------")
                        print("Internet Access Analysis.")
                        print("-------------------------")
                        print("1. Students with Internet Access.")
                        print("2. Students without Internet Access.")
                        print("3. Internet Status By Student ID.")
                        print("4. Back.")

                        while True:
                            try:
                                choice2_4=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid choice Input. Try Again.")
                                continue

                            match choice2_4:
                                case 1:
                                    df=analyze_internet_access(Dataframe, 1)
                                    if df is not False:
                                        print(f"Number of Students with internet Access: {df}")
                                case 2:
                                    df=analyze_internet_access(Dataframe, 2)
                                    if df is not False:
                                        print(f"Number of Students without internet Access: {df}")
                                case 3:
                                    try:
                                        student_ids=tuple(map(int, input("Enter Student IDs: (eg: 1,2,3,..): ").strip().split(",")))
                                    except ValueError:
                                        print("Invalid Student IDs. Try again.")
                                        continue
                                    df=analyze_internet_access(Dataframe, 3, student_ids)
                                    if df is not False:
                                        print(df)
                                case 4:
                                    break
                                case _:
                                    print("Invalid Input Choice.")                          
                    case 5:
                        print("--------------------------")
                        print("Extra Activities Analysis.")
                        print("--------------------------")
                        print("1. Students involved in Extra Activities.")
                        print("2. Students not involved in Extra Activities.")
                        print("3. Extra Activities By Student ID.")
                        print("4. Back.")
                        while True:
                            try:
                                choice2_5=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid choice Input. Try Again.")
                                continue

                            match choice2_5:
                                case 1:
                                    df=analyze_extra_activities(Dataframe, 1)
                                    if df is not False:
                                        print(f"Number of Students  in Extra Activities: {df}")
                                case 2:
                                    df=analyze_extra_activities(Dataframe, 2)
                                    if df is not False:
                                        print(f"Number of Students not in Extra Activities: {df}")
                                case 3:
                                    try:
                                        student_ids=tuple(map(int, input("Enter Student IDs: (eg: 1,2,3,..): ").strip().split(",")))
                                    except ValueError:
                                        print("Invalid Student IDs. Try again.")
                                        continue
                                    df=analyze_extra_activities(Dataframe, 3, student_ids)
                                case 4:
                                    break
                                case _:
                                    print("Invalid Input Choice.")
                    case 6:
                        while True:
                            print("-----------------------------")
                            print("Subject Performance Analysis.")
                            print("-----------------------------")
                            print("1. Highest Scorers.")
                            print("2. Lowest Scorers.")
                            print("3. Back.")
                            try:
                                choice2_6=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid choice Input. Try Again.")
                                continue

                            match choice2_6:
                                case 1:
                                    print("---------------")
                                    print("Highest Scorers")
                                    print("---------------")
                                    print("1. Overall Highest Scorers.")
                                    print("2. Math Highest Scorers.")
                                    print("3. Science Highest Scorers.")
                                    print("4. English Highest Scorers.")
                                    print("5. Back")

                                    while True:
                                        try:
                                            choice2_6_1=int(input("Enter Your Choice: "))
                                        except ValueError:
                                            print("Invalid Choice Input. Try Again.")
                                            continue

                                        match choice2_6_1:
                                            case 1:
                                                df=analyze_subject_performance(Dataframe, 1, 1)
                                                if df is not False:
                                                    print(df)
                                            case 2:
                                                df=analyze_subject_performance(Dataframe, 1, 2)
                                                if df is not False:
                                                    print(df)
                                            case 3:
                                                df=analyze_subject_performance(Dataframe, 1, 3)
                                                if df is not False:
                                                    print(df)
                                            case 4:
                                                df=analyze_subject_performance(Dataframe, 1, 4)
                                                if df is not False:
                                                    print(df)
                                            case 5:
                                                break
                                            case _:
                                                print("Invalid Choice Input.")
                                case 2:
                                    print("---------------")
                                    print("Lowest Scorers")
                                    print("---------------")
                                    print("1. Overall Lowest Scorers.")
                                    print("2. Math Lowest Scorers.")
                                    print("3. Science Lowest Scorers.")
                                    print("4. English Lowest Scorers.")
                                    print("5. Back")
                                        
                                    while True:
                                        try:
                                            choice2_6_2=int(input("Enter Your Choice: "))
                                        except ValueError:
                                            print("Invalid Choice Input. Try Again.")
                                            continue

                                        match choice2_6_2:
                                            case 1:
                                                df=analyze_subject_performance(Dataframe, 2, 1)
                                                if df is not False:
                                                    print(df)
                                            case 2:
                                                df=analyze_subject_performance(Dataframe, 2, 2)
                                                if df is not False:
                                                    print(df)
                                            case 3:
                                                df=analyze_subject_performance(Dataframe, 2, 3)
                                                if df is not False:
                                                    print(df)
                                            case 4:
                                                df=analyze_subject_performance(Dataframe, 2, 4)
                                                if df is not False:
                                                    print(df)
                                            case 5:
                                                break
                                            case _:
                                                print("Invalid Choice Input.")
                                case 3:
                                    break
                                case _:
                                    print("Invalid Choice Input.")
                    case 7:
                        while True:
                            print("------------------------")
                            print("Average Scores Analysis.")
                            print("------------------------")
                            print("1. Average Overall Score")
                            print("2. Average Of All Subjects")
                            print("3. Average Of Selected Subject")
                            print("4. Back")

                            try:
                                choice2_7=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid choice Input. Try Again.")
                                continue
                            
                            match choice2_7:
                                case 1:
                                    df=analyze_average_score(Dataframe, 1)
                                    if df is not False:
                                        print("Average:", df)
                                case 2:
                                    df=analyze_average_score(Dataframe, 2)
                                    if df is not False:
                                        print("Average:", df)
                                case 3:
                                    print("----------------------------")
                                    print("Average of selected Subject.")
                                    print("----------------------------")
                                    print("1. Maths Average.")
                                    print("2. Science Average.")
                                    print("3. English Average.")
                                    print("4. Back.")

                                    while True:
                                        try:
                                            choice2_7_1=int(input("Enter Your Choice: "))
                                        except ValueError:
                                            print("Invalid Choice Input. Try Again.")
                                            continue

                                        match choice2_7_1:
                                            case 1:
                                                df=analyze_average_score(Dataframe, 3, 1)
                                                if df is not False:
                                                    print("Average:", df)
                                            case 2:
                                                df=analyze_average_score(Dataframe, 3, 2)
                                                if df is not False:
                                                    print("Average:", df)
                                            case 3:
                                                df=analyze_average_score(Dataframe, 3, 3)
                                                if df is not False:
                                                    print("Average:", df)
                                            case 4:
                                                break
                                            case _:
                                                print("Invalid Choice input.")
                                case 4:
                                    break
                                case _:
                                    print("Invalid Choice Input.")
                    case 8:
                        while True:
                            print("---------------")
                            print("Grade Analysis.")
                            print("---------------")
                            print("1. Students With Particular Grade.")
                            print("2. Number Of Students In Each Grade.")
                            print("3. Percentage Of Students In Each Grade.")
                            print("4. Most Common Grade.")
                            print("5. Least Common Grade.")
                            print("6. Back.")

                            try:
                                choice2_8=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid choice Input. Try Again.")
                                continue

                            match choice2_8:
                                case 1:
                                    print("--------------------------------")
                                    print("Students with Particular Grade.")
                                    print("--------------------------------")
                                    print("1. Grade - A.")
                                    print("2. Grade - B.")
                                    print("3. Grade - C.")
                                    print("4. Grade - D.")
                                    print("5. Grade - E.")
                                    print("6. Grade - F.")
                                    print("7. Back.")
                                    
                                    while True:

                                        try:
                                            choice2_8_1=int(input("Enter Your Choice: "))
                                        except ValueError:
                                            print("Invalid Choice Input. Try Again.")
                                            continue

                                        match choice2_8_1:
                                            case 1:
                                                df=analyze_student_grade(Dataframe, 1, 1)
                                                if df is not False:
                                                    print(df)
                                            case 2:
                                                df=analyze_student_grade(Dataframe, 1, 2)
                                                if df is not False:
                                                    print(df)
                                            case 3:
                                                df=analyze_student_grade(Dataframe, 1, 3)
                                                if df is not False:
                                                    print(df)
                                            case 4:
                                                df=analyze_student_grade(Dataframe, 1, 4)
                                                if df is not False:
                                                    print(df)
                                            case 5:
                                                df=analyze_student_grade(Dataframe, 1, 5)
                                                if df is not False:
                                                    print(df)
                                            case 6:
                                                df=analyze_student_grade(Dataframe, 1, 6)
                                                if df is not False:
                                                    print(df)
                                            case 7:
                                                break
                                            case _:
                                                print("Invalid Choice Input.")
                                case 2:
                                    df=analyze_student_grade(Dataframe, 2)
                                    if df is not False:
                                        print(df)
                                case 3:
                                    df=analyze_student_grade(Dataframe, 3)
                                    if df is not False:
                                        print(df)
                                case 4:
                                    df=analyze_student_grade(Dataframe, 4)
                                    if df is not False:
                                        print(f"Most Common Grade: {df}")
                                case 5:
                                    df=analyze_student_grade(Dataframe, 5)
                                    if df is not False:
                                        print(f"Least Common Grade: {df}")
                                case 6:
                                    break
                                case _:
                                    print("Invalid Choice Input.")
                    case 9:
                        break
                    case _:
                        print("Invalid Choice Input.")
                    
        case 3:
            while True:
                print("----------------")
                print("Generate Charts.")
                print("----------------")
                print("1. Pie Charts.")
                print("2. Bar Charts.")
                print("3. Scatter Plots.")
                print("4. Histogram.")
                print("5. Back.")

                try:
                    choice3=int(input("Enter Your Choice: "))
                except ValueError:
                    print("Invalid Choice Input. Try Again.")
                    continue

                match choice3:
                    case 1:
                        print("-----------")
                        print("PIE CHARTS.")
                        print("-----------")
                        print("1. Internet Access.")
                        print("2. Extra Activities.")
                        print("3. Grade Distribution.")
                        print("4. Back.")

                        while True:
                            try:
                                choice3_1=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid Choice Input.")
                                continue

                            match choice3_1:
                                case 1:
                                    pie_charts(Dataframe, 1)
                                case 2:
                                    pie_charts(Dataframe, 2)
                                case 3:
                                    pie_charts(Dataframe, 3)
                                case 4:
                                    break
                                case _:
                                    print("Invalid Choice Input.")
                    case 2:
                        print("-----------")
                        print("BAR CHARTS.")
                        print("-----------")
                        print("1. Grade Distribution.")
                        print("2. Average Subject Scores.")
                        print("3. Student Subject Comparison.")
                        print("4. Back.")

                        while True:
                            try:
                                choice3_2=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid Choice Input. Try again.")
                                continue

                            match choice3_2:
                                case 1:
                                    bar_charts(Dataframe, 1)
                                case 2:
                                    bar_charts(Dataframe, 2)
                                case 3:
                                    try:
                                        student_id=int(input("Enter Student ID: "))
                                    except ValueError:
                                        print("Invalid Student Id Input. Try Again.")
                                        continue
                                    bar_charts(Dataframe, 3, student_id)
                                case 4:
                                    break
                                case _:
                                    print("Invalid Choice Input.")
                    case 3:
                        print("-------------")
                        print("Scatter Plot.")
                        print("-------------")
                        print("1. Study Hours vs Overall Score.")
                        print("2. Attendance vs Overall Score.")
                        print("3. Back.")

                        while True:
                            try:
                                choice3_3=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid Choice Input. Try Again.")
                                continue

                            match choice3_3:
                                case 1:
                                    scatter_plots(Dataframe, 1)
                                case 2:
                                    scatter_plots(Dataframe, 2)
                                case 3:
                                    break
                                case _:
                                    print("Invalid Choice Input.")
                    case 4:
                        print("-------------")
                        print("Histogram.")
                        print("-------------")
                        print("1. Overall Score Distribution.")
                        print("2. Back.")

                        while True:
                            try:
                                choice3_4=int(input("Enter Your Choice: "))
                            except ValueError:
                                print("Invalid Choice Input. Try Again.")
                                continue

                            match choice3_4:
                                case 1:
                                    histograms(Dataframe)
                                case 2:
                                    break
                                case _:
                                    print("Invalid Choice Input.")
                    case 5:
                        break
                    case _:
                        print("Invalid Choice Input.")
        case 4:
            print("\nCurrent Dataset:\n")
            print(Dataframe)
        case 5:
            print("Exiting...")
            time.sleep(1)
            exit(0)
        case _:
            print("Invalid Option Input.")


        