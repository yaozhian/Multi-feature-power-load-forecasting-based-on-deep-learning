from pandas import read_csv
from datetime import datetime
# load data
dataset = read_csv('raw_data.csv',  index_col=0)
print(dataset.values)
# manually specify column names
dataset.columns = ['power', 'temperature', 'humidity', 'speed']
# drop the first 24 hours
dataset = dataset[24:]
# summarize first 5 rows
print(dataset.head(5))
# save to file
dataset.to_csv('power.csv')