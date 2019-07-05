import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot

#Read the file
data = pd.read_csv('1231.csv', parse_dates=['date'])


#rename the coloumns
dta_min= data['tmin']
dta_year = data['date']

begin_year = dta_year[0:1].dt.year
end_year = dta_year[-1:].dt.year


#Make the date as an index
dta_min = np.array(dta_min, dtype=np.float)
dta_min = pd.Series(dta_min)
dta_min.index = pd.Index(sm.tsa.datetools.dates_from_range(str(begin_year.values[0]), str(end_year.values[0])))


#plot the graphs
dta_min.plot(figsize=(10, 6)).set_title('Time-series graph for 1 time-series example')
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(111)
diff1 = dta_min.diff(1)
diff1.plot(ax =ax1).set_title('Performe First order difference')




diff1 = dta_min.diff(1)
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(dta_min, lags=30, ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(dta_min, lags=30, ax=ax2)


Arma_mod39 = sm.tsa.ARMA(dta_min, (0, 4)).fit()
print(Arma_mod39.aic, Arma_mod39.bic, Arma_mod39.hqic)
resid = Arma_mod39.resid
fig = plt.figure(figsize=(10, 6))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_acf(resid.values.squeeze(), lags=30, ax=ax1)
fig = sm.graphics.tsa.plot_pacf(resid, lags=30, ax=ax2)
fig = plt.figure(figsize=(10, 6))
ax = fig.add_subplot(111)
fig = qqplot(resid, line='q', ax=ax, fit = True)



#pridict for the future 10 years
predict_year = 10
predict_end_year = end_year.values[0] + predict_year
predict_dta = Arma_mod39.predict(str(end_year.values[0]), str(predict_end_year), dynamic=True)
print(predict_dta)


#
# predict_dta.plot(figsize=(10,6)).set_title('predicted tempreture')
# fig = plt.figure(figsize=(10,6))
# ax1 = fig.add_subplot(111)
# diff1 = dta_min.diff(1)
plt.show()
