import pandas as pd
import matplotlib.pyplot as plt
from data_processing import *

plt.style.use("ggplot")

def pie_charts(dataframe, option):
    if dataframe.empty:
        print("DataFrame is Empty.")
        return False
    

    case1=dataframe["internet_access"].value_counts(sort=False)
    case2=dataframe["extra_activities"].value_counts(sort=False)
    case3=dataframe["final_grade"].value_counts(sort=False)

    match option:
        case 1:
            plt.pie(case1, labels=["Yes","No"], 
                    colors=["#4CAF50", "#FF7043"], 
                    shadow=True, explode=[0.05,0], 
                    autopct="%1.1f%%", 
                    wedgeprops={"edgecolor":"black"})
            plt.title("Students Internet Access Chart.", fontsize=20, color="Black", 
                      fontstyle="oblique")
            plt.tight_layout()
            plt.show()
        case 2:
            plt.pie(case2, labels=["Yes","No"], 
                    colors=["#3498DB", "#E74C3C"], 
                    shadow=True, explode=[0.05,0], 
                    autopct="%1.1f%%", 
                    wedgeprops={"edgecolor":"black"})
            plt.title("Students Extra Activities Chart.", 
                      fontsize=20, 
                      color="Black", 
                      fontstyle="oblique")
            plt.tight_layout()
            plt.show()
        case 3:
            plt.pie(case3, 
                    labels=case3.index, 
                    colors=["#4CAF50", "#2196F3","#FFC107", "#FF7043", "#AB47BC","#26C6DA"], 
                    explode=[0.1,0,0,0,0,0],
                    autopct="%1.1f%%",
                    startangle=60,
                    shadow=True,
                    wedgeprops={"edgecolor":"black"})
            plt.title("Distributed Grade Percentage Chart.",
                      fontsize=20, 
                      color="Black", 
                      fontstyle="oblique")
            plt.tight_layout()
            plt.show()
        case _:
            print("Invalid Option.")
            return False
        

def bar_charts(dataframe, option, student_id=None):
    if dataframe.empty:
        print("Dataframe is Empty.")
        return False
    

    y1=dataframe["final_grade"].value_counts(sort=False)
    x1=y1.index

    x2=["Maths", "Science", "English"]
    y2=dataframe[["math_score", "science_score", "english_score"]].mean()

    if not student_id is None:
        if student_id in dataframe["student_id"].values:
            filter=dataframe["student_id"]==student_id
            y3=dataframe[["math_score", "science_score", "english_score"]][filter].values.flatten()
            x3=["Maths", "Science", "English"]
        else:
            print("Invalid Student ID.")
            return False

    match option:
        case 1:
            plt.bar(x1,y1, color="Beige", width=0.25, edgecolor="black")
            plt.title("Grade Distribution Chart.",color="black", fontsize=20, fontstyle="oblique")
            plt.xlabel("Grade.",color="black", fontsize=20, fontstyle="oblique")
            plt.ylabel("Number of Students",color="black", fontsize=20, fontstyle="oblique")
            plt.tight_layout()
            plt.show()
        case 2:
            plt.bar(x2,y2, color="#AB47BC", width=0.25, edgecolor="black")
            plt.title("Subject's Average Scores Chart.",color="black", fontsize=20, fontstyle="oblique")
            plt.xlabel("Subject.",color="black", fontsize=20, fontstyle="oblique")
            plt.ylabel("Average.",color="black", fontsize=20, fontstyle="oblique")
            plt.tight_layout()
            plt.show()
        case 3:
            plt.bar(x3,y3, color="#2196F3", width=0.25, edgecolor="black")
            plt.title(f"Student's Average Scores Chart. ID:{student_id}",color="black", fontsize=20, fontstyle="oblique")
            plt.xlabel("Subject.",color="black", fontsize=20, fontstyle="oblique")
            plt.ylabel("Average.",color="black", fontsize=20, fontstyle="oblique")
            plt.tight_layout()
            plt.show()
        case _:
            print("Invalid Option.")
            return False
        

def scatter_plots(dataframe, option):
    if dataframe.empty:
        print("Dataframe is Empty.")
        return False
    
    x1=dataframe["study_hours"]
    y1=dataframe["overall_score"]

    x2=dataframe["attendance_percentage"]
    y2=dataframe["overall_score"]


    match option:
        case 1:
            plt.scatter(x1, y1, s=12, color="Teal", alpha=0.7)
            plt.title("Students Study Hours vs Score Chart.", color="black", fontsize=20, fontstyle="oblique")
            plt.xlabel("Study Hour.",color="black", fontsize=20, fontstyle="oblique")
            plt.ylabel("Overall Score.",color="black", fontsize=20, fontstyle="oblique")
            plt.tight_layout()
            plt.show()
        case 2:
            plt.scatter(x2, y2, s=12, color="Violet", alpha=0.7)
            plt.title("Students Attendance vs Score Chart.", color="black", fontsize=20, fontstyle="oblique")
            plt.xlabel("Attendance Percentage.",color="black", fontsize=20, fontstyle="oblique")
            plt.ylabel("Overall Score.",color="black", fontsize=20, fontstyle="oblique")
            plt.tight_layout()
            plt.show()
        case _:
            print("Invalid Option.")
            return False
        

def histograms(dataframe):
    if dataframe.empty:
        print("Dataframe is Empty.")
        return False
    
    scores=dataframe["overall_score"]
    median=dataframe["overall_score"].median()
    bin_edges=[10,20,30,40,50,60,70,80,90,100]
    plt.hist(scores, bins=bin_edges, color="lightblue", edgecolor="black", label="No. of Students.")
    plt.axvline(median, color="red", label="median")
    plt.title("Overall Score Histogram Chart.",color="black", fontsize=20, fontstyle="oblique")
    plt.xlabel("Overall Score.",color="black", fontsize=20, fontstyle="oblique")
    plt.ylabel("No. of Students.",color="black", fontsize=20, fontstyle="oblique")
    plt.legend()
    plt.tight_layout()
    plt.show()


