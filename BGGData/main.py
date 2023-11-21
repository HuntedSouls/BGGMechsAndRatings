# This is a sample Python script.
import APIGet
import DataAnalysis
import reformatData
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #dataFrame = pd.read_csv("RawData/Aggregated.csv")

    #filteredDF = DataAnalysis.FilterRankData(dataFrame)
    #DataAnalysis.CountNonRanked(dataFrame)
    #reformated = reformatData.addMechanics(filteredDF)
    #print(reformated.head(10))
    #filteredDF.to_csv("ReformattedData_filterTest.csv")
    filteredDF = pd.read_csv("ReformattedData_filterTest.csv")

    gameIDList = filteredDF["gameID"].unique()
    counter = 0 # last save point!
    # savepointDF = pd.read_csv(""RawData/ReformattedData_filterTest_"+str(counter)+".csv"")
    filteredDF = DataAnalysis.FilterImplementationData(filteredDF,gameIDList,counter)
    filteredDF.to_csv("ReformattedData_implementationTest.csv")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
