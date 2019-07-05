import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

#Read the file
data = pd.read_csv('1231.csv', parse_dates=['date'])

#rename the coloumns
dta = data['tmin']
dta_year = data['date']


begin_year = dta_year[0:1].dt.year

end_year = dta_year[-1:].dt.year

dta = data['tmin']


dta = np.array(dta, dtype=np.float)

dta = pd.Series(dta)
#Make the date as an index
dta.index = pd.Index(sm.tsa.datetools.dates_from_range(str(begin_year.values[0]), str(end_year.values[0])))

#plot the graphs
dta.plot(figsize=(10, 6)).set_title('Time-series graph for 1 time-series example')

fig = plt.figure(figsize=(10, 6))

ax1 = fig.add_subplot(111)

diff1 = dta.diff(1)

diff1.plot(ax =ax1).set_title('Performe First order difference')

diff1 = dta.diff(1)

fig = plt.figure(figsize=(10, 6))

ax1 = fig.add_subplot(211)

fig = sm.graphics.tsa.plot_acf(dta, lags=30, ax=ax1)

ax2 = fig.add_subplot(212)

fig = sm.graphics.tsa.plot_pacf(dta, lags=30, ax=ax2)
