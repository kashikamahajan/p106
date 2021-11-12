import numpy as np
import pandas as pd
import plotly_express as px
import csv
def getDataSource():
    days=[]
    marks=[]
    with open("Student Marks vs Days Present.csv") as file:
        data=csv.DictReader(file)
        for row in data:
            days.append(float(row["Days Present"]))
            marks.append(float(row["Marks In Percentage"]))
    
    return {"x":marks,"y":days}

def findCorrelation(datasource):
    correlation=np.corrcoef(datasource["x"],datasource["y"])
    print("Correlation is:",correlation[0,1])

def gra():
    with open("Student Marks vs Days Present.csv") as file:
        data=csv.DictReader(file)
        fig=px.scatter(data,x="Marks In Percentage", y="Days Present")
        fig.show()

def setup():
    datasource=getDataSource()
    findCorrelation(datasource)
    gra()

setup()