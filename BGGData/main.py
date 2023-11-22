# This is a sample Python script.
import APIGet
import DataAnalysis
import reformatData
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # dataFrame = pd.read_csv("RawData/Aggregated.csv")
    #
    # reformated = reformatData.addMechanics(dataFrame)
    #print(reformated.head(10))
    #filteredDF.to_csv("ReformattedData_filterTest.csv")
    savepointDF = pd.read_csv("ReformattedData_final.csv")

    # gameIDList = savepointDF["gameID"].unique()
    # counter = 1000 # last save point!
    # # savepointDF = pd.read_csv("RawData/ReformattedData_filterTest_"+str(counter)+"_v2.csv")
    # filteredDF = DataAnalysis.FilterImplementationData(savepointDF,gameIDList,counter)
    # filteredDF.to_csv("ReformattedData_implementationTest_v2.csv")

    # mechanizedDF = reformatData.addMechanics(savepointDF)
    # mechanizedDF.to_csv("ReformattedData_final.csv")

    #filter empty names
    cleanedDF = savepointDF.dropna(subset=["name"])
    cleanedDF.to_csv("ReformattedData_final_cleaned.csv")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
