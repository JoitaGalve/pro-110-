import csv
import pandas as pd
import random
import plotly.figure_factory as ff
import statistics

df = pd.read_csv("medium_data.csv")

data = df["reading_time"].tolist()
populationMean = statistics.mean(data)


def randomSetOfMean(counter):
    dataSet = []

    for i in range(0, counter):
        randomIndex = random.randint(0, len(data) - 1)
        value = data[randomIndex]
        dataSet.append(value)

    sampleMean = statistics.mean(dataSet)
    standardDeviation = statistics.stdev(dataSet)

    return sampleMean

def showFig(meanList):
    df = meanList
    fig = ff.create_distplot([data], ["reading_time"], show_hist = False)
    fig.show()

def setup():
    meanList = []
    
    for i in range(0, 100):
        setOfMeans = randomSetOfMean(100)
        meanList.append(setOfMeans)
    showFig(meanList)  

    print("Sample mean is: " + str(setOfMeans))

def stdevi():
    meanList = []
    
    for i in range(0, 100):
        setOfMeans = randomSetOfMean(30)
        meanList.append(setOfMeans)
    
    standardDeviation = statistics.stdev(meanList)
    print("Standard Deviation is: " + str(standardDeviation))


print("Mean of population is: " + str(populationMean))

setup()
stdevi()  
        