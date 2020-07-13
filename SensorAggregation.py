import json
import pandas as pd

url = open("sensor_data.json","r")
data = json.loads(url.read())

df = pd.DataFrame(data["array"])
df['timestamp'] = df['timestamp']/1000
df['date'] = pd.to_datetime(df['timestamp'], unit='s').dt.date

df = pd.DataFrame(data['array'])
df['timestamp'] = df['timestamp']/1000
df['date'] = pd.to_datetime(df['timestamp'], unit='s').dt.date #Convert to yyyy-mm-dd

#Set Min, Max, Median, Mean
df2 = df.groupby(['roomArea', 'date']).min()[['temperature','humidity']]
df2 = df2.rename(columns={'temperature' : 'min_temp', 'humidity' : 'min_humid'})

df3 = df.groupby(['roomArea', 'date']).max()[['temperature','humidity']]
df3 = df3.rename(columns={'temperature' : 'max_temp', 'humidity' : 'max_humid'})

df4 = df.groupby(['roomArea', 'date']).median()[['temperature','humidity']]
df4 = df4.rename(columns={'temperature' : 'median_temp', 'humidity' : 'median_humid'})

df5 = df.groupby(['roomArea', 'date']).mean()[['temperature','humidity']]
df5 = df5.rename(columns={'temperature' : 'avg_temp', 'humidity' : 'avg_humid'})

#Merge Data to df2
df2["max_temp"] = df3["max_temp"]
df2["max_humid"] = df3["max_humid"]
df2["median_temp"] = df4["median_temp"]
df2["median_temp"] = df4["median_humid"]
df2["avg_temp"] = df5["avg_temp"]
df2["avg_humid"] = df5["avg_humid"]
print(df2)