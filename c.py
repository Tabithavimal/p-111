from typing import Counter
import plotly.graph_objects as go
import plotly.figure_factory as ff
import csv
import random 
import statistics
import pandas as pd

df=pd.read_csv('c.csv')
data=df["id,url,title,subtitle,image,claps,responses,reading_time,publication,date"].tolist()
def randomsetofmean(counter):
    dataset=[]
    for index in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)

        populationmean=statistics.mean(dataset)
        return populationmean

meanlist=[]
for index in range(0,1000):
    meanlist.append(randomsetofmean(100))

populationstd=statistics.stdev(meanlist)
populationmean=statistics.mean(meanlist)

df1=pd.read_csv('c.csv')
data1=df1["id,url,title,subtitle,image,claps,responses,reading_time,publication,date"].tolist()
sample1mean=statistics.mean(data1)



zscore1=(populationmean-sample1mean)/populationstd


print(zscore1)
