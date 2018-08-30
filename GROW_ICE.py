""" Script to grow sea ice with varying air temperature and snow depth
Contributions:
A. Mahoney(University of Alaska Fairbanks): original 1D excel model for growing sea ice with constant temperature/snow-depth/freezing point
J. Shates (University of Wisconsin-Madison): initial translation from excel to python, data discovery and processing met data, precip to snow depth 
O. Baadshaug (Univeristy of Tromsoe): updates to sea ice function, handling nans and inputting hourly data 
J. (University of Tromsoe): converting daily snow depth values to hourly values

hourly met data:
in-situ hourly temperature & wind measurements: https://www.esrl.noaa.gov/gmd/dv/iadv/
site information: https://www.esrl.noaa.gov/gmd/obop/brw/

daily precip data: http://climate.gi.alaska.edu/acis_data
documentation: http://www.rcc-acis.org/docs_datasets.html

snow density measurements taken at 71 17'18.8"N 156 29'34.5"W
"""

#import modules and functions

from update2_sea_ice import Grow_Ice
from update2_sea_ice import Remove_bad_values
from snowfall_functions import get_snowdepth
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
import pickle
import calendar
import pandas as pd
##### load in temperature and date data. -999.9= missing value
#files are in .p form and sent separately

ymdh = pickle.load( open( "YMDH.p", "rb" ) )
temp10m = pickle.load( open( "TEMP10M.p", "rb" ) )
temp2m = pickle.load( open( "TEMP2M.p", "rb" ) )
PRECIP = pickle.load( open( "DAILY_PRECIP.p", "rb" ) )
precip=np.array(PRECIP[14:])

YMDH = []
for i in ymdh:
    YMDH.append(datetime.strptime(i, '%Y%m%d%H'))

first_indx = np.where(ymdh == '2017101500')[0][0]
last_indx = np.where(ymdh == '2018040101')[0][0]

Ta=temp2m[first_indx:last_indx]

Dates=YMDH[first_indx:last_indx]


Ta=Remove_bad_values(Ta, -999.9)

daily=get_snowdepth(precip)

for i,day in enumerate(daily):
     if i==0:
         hourly_tmp = np.ones((1,24))
         hourly = np.ones((1,24))
         hourly[:] = daily[i]
        # print('\nIndex: %i' % i)
        # print('Daily T: %f' % daily[i])
     else:    
         hourly_tmp_old = hourly_tmp
        # print('\nIndex: %i' % i)
        # print('Daily T: %f' % daily[i])
         if daily[i]==0:
            hourly_tmp = hourly_tmp_old
         else:
             hourly_tmp[:]=daily[i]
        # print(hourly_tmp)
         hourly = np.vstack((hourly,hourly_tmp))
     #print(hourly)
HS=np.ravel(hourly)

HS_final=HS[-1] 
#final value of snow depth for sanity check
print('Final snow depth over the ice: %f' %HS_final)

#Hs=0.
Fw = 4.

Dt_days = 1./24.



[Hi,hours] = Grow_Ice(Ta,HS,Fw,Dt_days)
dates=[Dates[j] for j in hours]
print('Final ice thickness: %f' %Hi[-1])
#print(hours)
# print(Hi)
fig=plt.figure(figsize=([8,6]))


month1=calendar.month_abbr[10]
year1='2017'

month2=calendar.month_abbr[4]
year2='2018'

ax = fig.add_subplot(111)

ax.plot(dates[1:],Hi[1:])# ax.plot(np.arange(len(Ta)+1), Hi)


plt.ylabel('Sea Ice Thickness[m]')
titlestring='Sea Ice Thickness \n' + month1 +' '+ year1 +'-'+ month2+' '+year2 + '\n Fw=4w/m2'
plt.title(titlestring)
plt.xlim((dates[0],dates[-1]))
plt.ylim(0, 2)
#plt.savefig('SEA_ICE.png')
#plt.show(block=False)
plt.show()