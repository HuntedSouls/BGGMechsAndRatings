# This is a sample Python script.
import APIGet
import DataAnalysis
import reformatData
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dataFrame = pd.read_csv("RawData/Aggregated.csv")
    # remove all subtyperanks nan so we can filer by them
    dataFrame = dataFrame[dataFrame['subtype_rank'].notna()]
    rankedDF = dataFrame.query("subtype_rank != 'Not Ranked'")

    # Fill nan in average so we can filter 0s
    rankedDF["bayesaverage"] = rankedDF.loc[:,"bayesaverage"].fillna(0)
    rankedDF = rankedDF.query("bayesaverage != 0.0")
    #DataAnalysis.CountNonRanked(dataFrame)
    reformated = reformatData.addMechanics(rankedDF)
    print(reformated.head(10))
    reformated.to_csv("RawData/ReformattedData.csv")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
