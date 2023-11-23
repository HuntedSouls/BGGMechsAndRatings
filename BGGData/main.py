# This is a sample Python script.
import APIGet
import DataAnalysis
import reformatData
import matplotlib.pyplot as plt
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
    # savepointDF = pd.read_csv("ReformattedData_final_cleaned.csv")

    # gameIDList = savepointDF["gameID"].unique()
    # counter = 1000 # last save point!
    # # savepointDF = pd.read_csv("RawData/ReformattedData_filterTest_"+str(counter)+"_v2.csv")
    # filteredDF = DataAnalysis.FilterImplementationData(savepointDF,gameIDList,counter)
    # filteredDF.to_csv("ReformattedData_implementationTest_v2.csv")

    # mechanizedDF = reformatData.addMechanics(savepointDF)
    # mechanizedDF.to_csv("ReformattedData_final.csv")

    # #filter empty names
    # cleanedDF = savepointDF.dropna(subset=["name"])
    # cleanedDF.to_csv("ReformattedData_final_cleaned.csv")

    # # grouping by mehcanics grouping
    # savepointDF = reformatData.JoinMehcanics("Area Movement",
    #                                          ["Area Movement","Grid Movement","Point to Point Movement","Three Dimensional Movement"],savepointDF)
    # savepointDF = reformatData.JoinMehcanics("Auction",
    #                                          ["Auction Compensation", "Auction/Bidding","Auction: Dexterity","Auction: Dutch","Auction: Dutch Priority",
    #                                           "Auction: English","Auction: Fixed Placement","Auction: Multiple Lot","Auction: Once Around",
    #                                           "Auction: Sealed Bid","Auction: Turn Order Until Pass",], savepointDF)
    # savepointDF = reformatData.JoinMehcanics("Deduction",
    #                                          ["Deduction", "Induction"], savepointDF)
    # savepointDF = reformatData.JoinMehcanics("Grid Board",
    #                                          ["Hexagon Grid", "Square Grid"], savepointDF)
    # savepointDF = reformatData.JoinMehcanics("Impulse",
    #                                          ["Area-Impulse", "Impulse Movement"], savepointDF)
    # savepointDF = reformatData.JoinMehcanics("Pattern Movement",
    #                                          ["Movement Template", "Pattern Movement"], savepointDF)
    # savepointDF = reformatData.JoinMehcanics("Predictive Bid",
    #                                          ["Bids As Wagers", "Predictive Bid"], savepointDF)
    # savepointDF = reformatData.JoinMehcanics("Real-Time",
    #                                          ["Real-Time", "Elapsed Real Time Ending"], savepointDF)
    # savepointDF = reformatData.JoinMehcanics("Turn Order",
    #                                          ["Turn Order: Auction", "Turn Order: Claim Action", "Turn Order: Pass Order", "Turn Order: Progressive",
    #                                           "Turn Order: Random", "Turn Order: Role Order","Turn Order: Stat-Based", "Turn Order: Time Track"], savepointDF)
    # savepointDF = reformatData.JoinMehcanics("Worker Placement",
    #                                          ["Worker Placement", "Worker Placement with Dice Workers", "Worker Placement, Different Worker Types"], savepointDF)
    # savepointDF.to_csv("MechanicsFiltered.csv")

    ### data analysis part
    # unfiltered graphics
    # dataFrame = pd.read_csv("RawData/ReformatedData_unfiltered.csv")
    # DataAnalysis.GnerateHistograms(dataFrame)
    # plt.show()
    # DataAnalysis.MechanicsGraphics(dataFrame,26)
    # plt.show()

    # filtered graphics
    dataFrame = pd.read_csv("ReformattedData_final_cleaned.csv")
    # DataAnalysis.GnerateHistograms(dataFrame)
    # plt.show()
    DataAnalysis.MechanicsGraphics(dataFrame,29)
    plt.show()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
