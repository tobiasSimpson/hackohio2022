import uvicorn
import pandas as pd
from fastapi import FastAPI

app = FastAPI()
global_data = {}

#Name of the display dorm
dormName="Busch House"
dfAllExtended = pd.DataFrame()

@app.on_event("startup")
async def startup_event():
    #Read complete dataset
    dfAllExtended = pd.read_csv('data\Dorm Buildings.csv')

@app.get("regression")
async def Regression(csv):
    dfDorm = pd.read_csv(csv)
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
    return [cols[maxIndx1], cols[maxIndx2]].to_json()

@app.get("learderboard")
async def Leaderboard(dfAll,dfDorm):

    return 0

@app.get("graph")
async def Graph(csv):
    dfDorm = pd.read_csv(csv)
    dfDorm = pd.concat([dfDorm[["Series Name"]],dfDorm[[dormName + " - Total Energy Consumption (Cleaned) (kBTU)"]]],axis=1)
    return dfDorm.to_json()

@app.get("nextWeek")
async def next_week(n):
    dfAll = dfAllExtended.iloc[0:n]
    #Create a datasubset for specific dorm
    dormNameCols = dfAll.columns
    dfDorm = dfAll[["Series Name"]]
    for x in dormNameCols:
        if dormName in x:
            dfDorm = pd.concat([dfDorm,dfAll[[x]]], axis=1)
    # Limit dataframe to past week
    dfDormWeek = dfDorm.iloc[int(n)-168:int(n)]
    return dfDormWeek.to_json()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, workers=1)