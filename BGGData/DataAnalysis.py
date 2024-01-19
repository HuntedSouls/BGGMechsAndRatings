import math
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def GnerateHistograms(dataframe):
    dataframe.hist("average",bins=100)

    dataframe.hist("bayesaverage", bins=100)

def MechanicsGraphics(dataframe,columnMechanic):
    dframe = dataframe.iloc[:,columnMechanic:]
    mechsCount = dframe.sum(axis=0)
    ordered = mechsCount.sort_values(ascending=False)
    cut = ordered[4:]
    plot = cut.plot(figsize=(10, 10), kind="bar")
    plot.set_xticks([])
    plot.set_xlabel("Mechanics")
    plot.set_ylabel("Games featured")
    plt.suptitle("Mechanics representation")

def MechanicsStats(dataframe,columnMechanic):
    dframe = dataframe.iloc[:,columnMechanic:]
    mechsCount = dframe.sum(axis=0)
    ordered = mechsCount.sort_values(ascending=False)
    cut = ordered[4:]
    plot = cut.plot(figsize=(10, 10), kind="bar")
    plot.set_xticks([])
    plot.set_xlabel("Mechanics")
    plot.set_ylabel("Games featured")
    plt.suptitle("Mechanics representation")