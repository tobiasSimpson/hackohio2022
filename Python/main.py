import pandas as pd

#Name of the display dorm
dormName="Busch House"

def Regression(dfDorm):
    #Run a simple linear regression for current hour
    startIndx = [23,47,71,95,119,143,167]
    endIndx = [0,24,48,72,96,120,144]
    startAvg = [0,0,0,0,0]
    endAvg = [0,0,0,0,0]
    cols = ["Steam", "Electricity", "Chilled Water", "Hot Water", "Natural Gas"]

    for i in startIndx:
        startAvg[0] += dfDorm.iloc[i][dormName + " - Steam Consumption (kBTU)"]
        startAvg[1] += dfDorm.iloc[i][dormName + " - Electricity Consumption (kBTU)"]
        startAvg[2] += dfDorm.iloc[i][dormName + " - Chilled Water Consumption (kBTU)"]
        startAvg[3] += dfDorm.iloc[i][dormName + " - Hot Water Consumption (kBTU)"]
        startAvg[4] += dfDorm.iloc[i][dormName + " - Natural Gas Consumption (kBTU)"]
    startAvg = [x / 7 for x in startAvg]

    for i in endIndx:
        endAvg[0] += dfDorm.iloc[i][dormName + " - Steam Consumption (kBTU)"]
        endAvg[1] += dfDorm.iloc[i][dormName + " - Electricity Consumption (kBTU)"]
        endAvg[2] += dfDorm.iloc[i][dormName + " - Chilled Water Consumption (kBTU)"]
        endAvg[3] += dfDorm.iloc[i][dormName + " - Hot Water Consumption (kBTU)"]
        endAvg[4] += dfDorm.iloc[i][dormName + " - Natural Gas Consumption (kBTU)"]
    endAvg = [x / 7 for x in endAvg]

    max1 = -100000
    maxIndx1 = 0
    max2 = -100001
    maxIndx2 = 0
    for i in range(0,len(startAvg)):
        if startAvg[i] > 0 and endAvg[i] > 0:
            if endAvg[i] - startAvg[i] > max1:
                max1 = endAvg[i] - startAvg[i]
                maxIndx1 = i
            else:
                if endAvg[i] - startAvg[i] > max2:
                    max2 = endAvg[i] - startAvg[i]
                    maxIndx2 = i
    return [cols[maxIndx1], cols[maxIndx2]]

def Leaderboard(dfAll,dfDorm):

    return 0

def Graph(dfDorm):
    return pd.concat([dfDorm[["Series Name"]],dfDorm[[dormName + " - Total Energy Consumption (Cleaned) (kBTU)"]]],axis=1)

#Read complete dataset
dfAll = pd.read_csv("Python\Dorm Buildings.csv")

#Create a datasubset for specific dorm
dormNameCols = dfAll.columns
dfDorm = dfAll[["Series Name"]]
for x in dormNameCols:
    if dormName in x:
        dfDorm = pd.concat([dfDorm,dfAll[[x]]], axis=1)
#Limit dataframe to past week
n=len(dfDorm.index)
dfDormWeek = dfDorm.iloc[n-168:n]


print(Regression(dfDormWeek))