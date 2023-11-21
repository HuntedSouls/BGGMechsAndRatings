import pandas as pd
import numpy as np
def repeatUniqueGameIDS(df):
    # repeating all values for game ID except mechanics and implementations
    lastGameID = 0
    countIndexes = []
    data = {}
    # count = 0
    for series_name, series in df.items():
        # print(series_name)
        if series_name != "implementation" and series_name != "mechanic":
            data[series_name] = []
        else:
            continue
        gameIDCounter = 0
        skipCounter = 0
        for element in series:
            # print(element)
            if series_name == "gameID":
                currentGameID = element
                if currentGameID != lastGameID:
                    # count = count + 1
                    lastGameID = currentGameID
                    data[series_name].append(currentGameID)
                    countIndexes.append(series.value_counts()[currentGameID])
                    # if (count > 10):
                    #     count = 0
                    #     break
            elif series_name != "implementation" and series_name != "mechanic":
                print(gameIDCounter)
                if skipCounter == 0:
                    # count = count + 1
                    if (not pd.isna(element)):
                        currentValue = element
                        data[series_name].append(currentValue)
                    else:
                        data[series_name].append(np.nan)

                    if (count > 10):
                        count = 0
                        break
                if skipCounter < (countIndexes[gameIDCounter] - 1):
                    skipCounter = skipCounter + 1
                else:
                    skipCounter = 0
                    gameIDCounter = gameIDCounter + 1
                # if (count > 10):
                #     count = 0
                #     break
    return pd.DataFrame(data)

def addMechanics(df):
    reformated = df.groupby('gameID').first().reset_index()
    reformated = reformated.drop(["mechanic", "implementation"], axis=1)
    print("Reformation done on baisc, starting mech part")
    mechlist = df['mechanic'].unique()
    mechlist = np.delete(mechlist, 0)
    gameIDList = reformated["gameID"].unique()
    data = {}
    for mechanic in mechlist:
        data[mechanic] = []
        for element in gameIDList:
            rows = df.loc[df['gameID'] == element]
            found = False
            for index, row in rows.iterrows():
                if row["mechanic"] == mechanic:
                    found = True
            if found:
                data[mechanic].append(1)
            else:
                data[mechanic].append(0)
        print("done on mech ",mechanic)
    mechanicDF = pd.DataFrame(data)
    return reformated.join(mechanicDF)