import requests  # for using API
import time
import xml.etree.ElementTree as ET  # for parsing XML
import bs4 as bs
import pandas as pd
def GetBGGBoardgames():
    stillGettingRight = True;
    currentID=1
    while(stillGettingRight):
        time.sleep(2)
        requestURL = "https://boardgamegeek.com/xmlapi2/thing?id="
        for i in range(100):
            requestURL = requestURL + str(currentID) + ","
            currentID = currentID +1
        requestURL= requestURL +"&type=boardgame&stats=1"
        print(requestURL)
        request = requests.get(requestURL)
        parsed = bs.BeautifulSoup(request.text, "lxml-xml")
        data=[]
        for item in parsed.find_all('item'):
            entry={}
            itemID = item.get("id")
            entry["gameID"]= itemID
            for children in item.findChildren():
                name=children.name
                if name == "poll" or name == "thumbnail" or name == "image" or name == "result" or name == "ratings"\
                        or name == "description" or name == "link" or name == "statistics" or name == "results" or name == "ranks":
                    continue
                elif name == "name":
                    if children.get("type") != "primary":
                        continue
                    entry[name] = children.get("value")
                elif name == "rank":
                    entry[children.get("type")+"_rank"] = children.get("value")
                    entry[children.get("type")+"_Average"] = children.get("bayesaverage")
                else:
                    entry[name] = children.get("value")
            data.append(entry)
            for link in item.find_all("link"):
                mechEntry = {"gameID": itemID}
                if link.get("type") == "boardgamemechanic":
                    mechEntry["mechanic"]=link.get("value")
                    data.append(mechEntry)
                elif link.get("type") == "boardgameimplementation":
                    mechEntry["implementation"]=link.get("value")
                    data.append(mechEntry)

        dataFrame = pd.DataFrame(data)
        if(dataFrame.empty):
            print("Got nothing AAAAAAAAAAAA")
        dataFrame.to_csv("RawData/upTo"+str(currentID)+".csv",index=False)
        if currentID>100000:
            stillGettingRight=False