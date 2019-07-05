# from os import sendfile

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.stattools import adfuller
from statsmodels.graphics.api import qqplot
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

class processdata:
    def __init__(self,data,predict_year,data_type):
        self.data =data
        self.prefict_year =predict_year
        self.data_type =data_type

        #define processing function

    def process_minmac(self):
       if self.data_type == 'max':
        max_data =self.data['tmax']
       elif self.data_type == 'min':
        max_data =self.data['tmin']




       data_year = self.data['date']


       begin_year=data_year[0:1].dt.year

       end_year =data_year[-1:].dt.year

       predict_month = data_year[0:1].dt.year

       predict_day = data_year[0:1].dt.year




       max_data =np.array(max_data, dtype=np.float)


       arma_mod96=sm.tsa.ARMA(max_data,(9,6)).fit()
       predict_end_year =end_year.values[0]+self.predict_year

       predict_dta =arma_mod96.predict(str(end_year.values[0]),str(predict_end_year),dynamic=True)


       print(predict_dta)

       predict_dta.to_json(self.data_type+'.json',date_format='iso')


       json_date =FJD.format_json(self.data_type+'.json',str(predict_month.values[0]),str(predict_day.values[0]))
       print(json_date)


       fig,ax =plt.subplots(figsize=(12,8))
       ax=max_data.ix[str(begin_year.values[0]):].plot(ax=ax)
       arma_mod96.plot_predict(str(end_year.values[0]),str(predict_end_year),dynamic=True, ax=ax,plot_insample=False)

       #fig = plt.gcf()

       #plt.show()

       plt.savefig(self.data_type+'.png',dpi=100)


       send=SendFile(fileName=self.data_type+'png')
       send.send()








