import pandas as pd

def Regression(dfDorm):

    return 0

def Leaderboard(dfAll,dfDorm):

    return 0

def Graph(dfDorm,dormName):
    return pd.concat([dfDorm[["Series Name"]],dfDorm[[dormName + " - Total Energy Consumption (Cleaned) (kBTU)"]]],axis=1)

#Name of the display dorm
dormName="Busch House"
#Read complete dataset
dfAll = pd.read_csv("Python\Dorm Buildings.csv")

#Create a datasubset for specific dorm
dormNameCols = dfAll.columns
dfDorm = dfAll[["Series Name"]]
for x in dormNameCols:
    if dormName in x:
        dfDorm = pd.concat([dfDorm,dfAll[[x]]], axis=1)
print(dfDorm)
#Limit dataframe to past week
n=len(dfDorm.index)
dfDormWeek = dfDorm.iloc[n-168:n]
