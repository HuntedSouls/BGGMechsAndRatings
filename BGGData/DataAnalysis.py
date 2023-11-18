import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
def FilterData(dataFrame):
    #remove all subtyperanks nan so we can filer by them
    dataFrame = dataFrame[dataFrame['subtype_rank'].notna()]
    rankedDF = dataFrame.query("subtype_rank != 'Not Ranked'")

    #Fill nan in average so we can filter 0s
    rankedDF["bayesaverage"] =rankedDF["bayesaverage"].fillna(0)
    rankedDF = rankedDF.query("bayesaverage != 0.0")

    implList = rankedDF.groupby("gameID")["implementation"].apply(list).reset_index(name='impls')

    # filter through implementations
    for gameID in rankedDF["gameID"]:
        implementations = implList.loc[implList['gameID'] == gameID]
        cleaned = [x for x in implementations if str(x) != 'nan']
        listOfGameIDS =[]
        listOfGameIDS.append(gameID)
        for name in cleaned:
            foundGames = rankedDF.loc[rankedDF['name'] == name]
            if not foundGames.empty:
                listOfGameIDS.append(foundGames.iloc[0]["gameID"])


def HandleMechanicsMess(rankedDF, listOfGameIDS):
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
        #define the higher year to be the entry and do some math see combine stdeviation