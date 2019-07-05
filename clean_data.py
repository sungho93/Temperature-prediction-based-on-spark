import pandas as pd
from datetime import datetime
from dateutil import parser

data_raw = pd.read_csv('1792347.csv', encoding='utf-8')


# screening data

data_raw['date'] = data_raw['DATE'].apply(parser.parse)

data_raw['tmac'] =data_raw['TMAX'].astype(float)

data_raw['tmin'] =data_raw['TMIN'].astype(float)

#get the requierd columns and filter out the null values

data =data_raw.loc[:,['date','tmax','tmin']]

#filter empty data

data =[(pd.Series.notnull(data['tmax'])) & pd.Series.notnull(data['tmin'])]

#filterout eligible data based on filter conditions

data =data[(data["date"]>= datetime(1980,7,16)) &(data["date"]<=datetime(2012,7,16))]

data.query("date.dt.day == 28 & date.dt.month == 6", inplace=True)


#write the final result to CSV file

data.to_csv('1231.csv', index=None)
