import pandas as pd

def regression(dfDorm):
    return 0

def leaderboard(dfAll,dfDorm):
    return 0

def graph(dfDorm):
    return 0

#Name of the display dorm
dormName="Busch House"
#Read complete dataset
dfAll = pd.read_csv("Python\Dorm Buildings.csv")

#Create a datasubset for specific dorm
dormNameCols = dfAll.columns
dfDorm = dfAll[["Series Name"]]
for x in dormNameCols:
    if dormName in x:
        dfDorm = pd.concat([dfDorm,dfAll[[x]]])