import math

import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
def FilterRankData(dataFrame):
    #remove all subtyperanks nan so we can filer by them
    #filterDF = dataFrame[dataFrame['subtype_rank'].notna()]
    blacklistDF = dataFrame.query("subtype_rank != 'Not Ranked'")

    #Fill nan in average so we can filter 0s
    blacklistDF["bayesaverage"] =blacklistDF["bayesaverage"].fillna(0)
    blacklistDF = blacklistDF.query("bayesaverage != 0.0")

    whiteListedIDS=blacklistDF["gameID"].unique()
    filteredDF = dataFrame.loc[dataFrame['gameID'].isin(whiteListedIDS)]
    # for gameID in blacklistedGameIDs:
    #     filteredDF = filteredDF.loc[not filteredDF['gameID'].isin(gameID)]
    return filteredDF

def FilterImplementationData(filteredDF,gameIDList,counter):
    implList = filteredDF.groupby("gameID")["implementation"].apply(list).reset_index(name='impls')
    #counter = 0
    # gameIDList=filteredDF["gameID"].unique()
    # filter through implementations
    solvedGameID = []
    for gameID in gameIDList:
        if not solvedGameID.__contains__(gameID):
            implementations = implList.loc[implList['gameID'] == gameIDList[counter]]
            cleaned = [x for x in implementations if str(x) != 'nan']
            listOfGameIDS = [gameIDList[counter]]
            solvedGameID.append(gameIDList[counter])
            for name in cleaned:
                foundGames = filteredDF.loc[filteredDF['name'] == name]
                if not foundGames.empty:
                    newID = foundGames.iloc[0]["gameID"]
                    listOfGameIDS.append(newID)
                    solvedGameID.append(newID)
            filteredDF = HandleReimplementations(filteredDF, listOfGameIDS)
        else:
            print("already done this! ",gameID)
        if counter >= len(gameIDList):
            filteredDF.to_csv("RawData/ReformattedData_filterTest_" + str(counter) + ".csv")
            break
        counter = counter+1
        if counter%1000==0:
            filteredDF.to_csv("RawData/ReformattedData_filterTest_"+str(counter)+".csv")
            print("created save point: ", counter)

        #print("finished gameID : ", gameID)

    return filteredDF

def HandleReimplementations(rankedDF, listOfGameIDS):
    mechList = rankedDF.groupby("gameID")["mechanic"].apply(list).reset_index(name='mechs')
    thisMechs ={}
    for gameID in listOfGameIDS:
        mechanics = mechList.loc[mechList['gameID'] == gameID]
        cleaned = [x for x in mechanics if str(x) != 'nan']
        thisMechs[gameID] = cleaned

    equal=[]
    for gameID in listOfGameIDS:
        if gameID == listOfGameIDS[0]:
            continue
        if thisMechs[gameID].sort() == thisMechs[listOfGameIDS[0]].sort():
            equal.append(gameID)
    #do some magic if they found equal games
    mainGame = pd.Series()
    if len(equal)>0:
        avgRatingList =[]
        baeysianRatingList =[]
        stdRatingList =[]
        voteCountList=[]
        yearList=[]
        for gameID in equal:
            selected = rankedDF.loc[rankedDF['gameID'] == gameID]
            avgRatingList.append(selected.iloc[0]["average"])
            baeysianRatingList.append(selected.iloc[0]["bayesaverage"])
            stdRatingList.append(selected.iloc[0]["stddev"])
            voteCountList.append(selected.iloc[0]["usersrated"])
            yearList.append(selected.iloc[0]["yearpublished"])
        #define the older year to be the entry and delete all "tied" games
        olderYear = min(yearList)
        olderGameID = equal[yearList.index(olderYear)]
        mainGame = rankedDF.iloc[0][rankedDF['yearpublished'] == olderGameID]
        for gameID in equal:
            rankedDF = rankedDF[rankedDF["gameID"] != gameID]
        #and do some math see combine averages and stdeviation
        mainGame["average"] = weightedAverage(voteCountList,avgRatingList)
        mainGame["bayesaverage"] = weightedAverage(voteCountList, baeysianRatingList)
        mainGame["stddev"] =mixStddev(voteCountList,stdRatingList)
        mainGame["usersrated"] =sum(voteCountList)
        #add line to dataframe
    return pd.concat([rankedDF,mainGame], ignore_index=True)

def weightedAverage(weights,averages):
    sum = 0
    for i in range(len(averages)):
        sum = sum + averages[i]*weights[i]
    return sum/(sum(weights))

def mixStddev(sameplsizes,stddevs):
    sum = 0
    for i in range(len(stddevs)):
        sum = sum + (stddevs[i]**2)/sameplsizes[i]
    return math.sqrt(sum)