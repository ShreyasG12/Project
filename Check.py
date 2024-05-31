from tkinter import *
def Train():
    """GUI"""
    import tkinter as tk
    import numpy as np
    import pandas as pd

    from sklearn.decomposition import PCA
    from sklearn.preprocessing import LabelEncoder

    root = tk.Tk()

    root.geometry("1400x700" )
    root.title("Machine Learning Based Predicting Student Academic Success")
    root.configure(background="#CCFFCC")
    
    gender = tk.IntVar()
    Nationlity = tk.IntVar()
    PlaceofBirth = tk.IntVar()
    StageID = tk.IntVar()
    GradeID = tk.IntVar()
    Topic = tk.IntVar()
    Semester = tk.IntVar()
    VisitedResources= tk.IntVar()
    AnnouncementsView= tk.IntVar()
    Discussion = tk.IntVar()
    ParentAnsweringSurvey = tk.DoubleVar()
    ParentsShoolSatisfaction = tk.IntVar()
    StudentAbsenceDays = tk.IntVar()
    Class=tk.IntVar()
   
    
    #===================================================================================================================
    def Detect():
        e1= gender.get()
        print(e1)
        e2=Nationlity.get()
        print(e2)
        e3= PlaceofBirth.get()
        print(e3)
        e4=StageID.get()
        print(e4)
        e5=GradeID.get()
        print(e5)
        e6=Topic.get()
        print(e6)
        e7=Semester.get()
        print(e7)
        e8=VisitedResources.get()
        print(e8)
        e9=AnnouncementsView.get()
        print(e9)
        e10=Discussion.get()
        print(e10)
        e11=ParentAnsweringSurvey.get()
        print(e11)
        e12=ParentsShoolSatisfaction.get()
        print(e12)
        e13=StudentAbsenceDays.get()
        print(e13)
        e14=Class.get()
        print(e13)
        
        
        #########################################################################################
        
        from joblib import dump , load
        a1=load('D:/23 Protech/100% code/Student Performance Prediction/23CP123-Student Academic Success/student_performance.joblib')
        v= a1.predict([[e1, e2, e3, e4, e5, e6, e7, e8, e9,e10, e11, e12, e13, e14]])
        print(v)
        if v[0]==0:
            print("High")
            yes = tk.Label(root,text="Performance of student in academics is 1st Class",background="green",foreground="white",font=('times', 20, ' bold '),width=38)
            yes.place(x=320,y=450)
                     
        elif v[0]==1:
            print("Medium")
            no = tk.Label(root, text="Performance of student in academics is 2nd Class", background="orange", foreground="white",font=('times', 20, ' bold '),width=38)
            no.place(x=320, y=450)
            
            
        else:
            print("Low")
            no = tk.Label(root, text="Student has preformed weak in Academics", background="red", foreground="white",font=('times', 20, ' bold '),width=38)
            no.place(x=320, y=450)
            


    l1=tk.Label(root,text="gender",background="olive",font=('times', 20, ' bold '),width=15)
    l1.place(x=5,y=5)
    gender=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=gender)
    gender.place(x=300,y=1)

    l2=tk.Label(root,text="Nationality",background="olive",font=('times', 20, ' bold '),width=15)
    l2.place(x=550,y=5)
    Nationlity=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Nationlity)
    Nationlity.place(x=850,y=1)

    l3=tk.Label(root,text="PlaceofBirth",background="olive",font=('times', 20, ' bold '),width=15)
    l3.place(x=5,y=70)
    PlaceofBirth=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=PlaceofBirth)
    PlaceofBirth.place(x=300,y=70)
    
    l4=tk.Label(root,text="StageID",background="olive",font=('times', 20, ' bold '),width=15)
    l4.place(x=550,y=70)
    StageID=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=StageID)
    StageID.place(x=850,y=70)

    l5=tk.Label(root,text="GradeID",background="olive",font=('times', 20, ' bold '),width=15)
    l5.place(x=5,y=130)
    GradeID=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=GradeID)
    GradeID.place(x=300,y=130)

    l6=tk.Label(root,text="Topic",background="olive",font=('times', 20, ' bold '),width=15)
    l6.place(x=550,y=130)
    Topic=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Topic)
    Topic.place(x=850,y=130)

    l7=tk.Label(root,text="Semester",background="olive",font=('times', 20, ' bold '),width=15)
    l7.place(x=5,y=190)
    Semester=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Semester)
    Semester.place(x=300,y=190)

    l8=tk.Label(root,text="VisitedResources",background="olive",font=('times', 20, ' bold '),width=15)
    l8.place(x=550,y=190)
    VisitedResources=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=VisitedResources)
    VisitedResources.place(x=850,y=190)

    l9=tk.Label(root,text="AnnouncementsView",background="olive",font=('times', 20, ' bold '),width=17)
    l9.place(x=5,y=260)
    AnnouncementsView=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=AnnouncementsView)
    AnnouncementsView.place(x=300,y=260)

    l10=tk.Label(root,text="Discussion",background="olive",font=('times', 20, ' bold '),width=10)
    l10.place(x=550,y=260)
    Discussion=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Discussion)
    Discussion.place(x=850,y=260)

    l11=tk.Label(root,text="ParentAnsweringSurvey",background="olive",font=('times', 18, ' bold '),width=20)
    l11.place(x=5,y=330)
    ParentAnsweringSurvey=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=ParentAnsweringSurvey)
    ParentAnsweringSurvey.place(x=300,y=330)

    l12=tk.Label(root,text="ParentsShoolSatisfaction",background="olive",font=('times', 18, ' bold '),width=20)
    l12.place(x=550,y=330)
    ParentsShoolSatisfaction=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=ParentsShoolSatisfaction)
    ParentsShoolSatisfaction.place(x=850,y=330)

    l13=tk.Label(root,text="StudentAbsenceDays",background="olive",font=('times', 20, ' bold '),width=17)
    l13.place(x=5,y=390)
    StudentAbsenceDays=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=StudentAbsenceDays)
    StudentAbsenceDays.place(x=300,y=390)
    
    l14=tk.Label(root,text="Class",background="olive",font=('times', 20, ' bold '),width=17)
    l14.place(x=550,y=390)
    Class=tk.Entry(root,bd=2,width=5,font=("TkDefaultFont", 20),textvar=Class)
    Class.place(x=850,y=390)

    def window():
       root.destroy()
    
    
    button1 = tk.Button(root,text="Submit",command=Detect,font=('times', 20, ' bold '),width=10,bg="green")
    button1.place(x=400,y=600)
    
    button1 = tk.Button(root,text="Logout",command=window,font=('times', 20, ' bold '),width=10,bg="red")
    button1.place(x=800,y=600)

    root.mainloop()

Train()