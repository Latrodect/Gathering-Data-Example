# -*- coding: utf-8 -*-
"""
Created on Wed Feb  2 23:24:56 2022

@author: hbaha
"""

import numpy as np
import pandas as pd
import datetime

data = pd.read_csv('TestCaseData.csv')
data.columns =[ 'Date', 'Value']
data['Date']=( data.Date.str.split("/")
              .apply(lambda x: '/ '.join(x[::-1]).rstrip('/'))
              .where(data['Date'].str.contains('/'),data['Date']) )

data['Date'] = pd.to_datetime(data['Date'])
print("Formatted Time Value")
print("   ")
print(data)
print("-----------------------------------------------------------------")
print("Format needs to be like that '2021-02-04(Year,Month,Day)'")
start_Date = str(input("Start Date: "))
print("Format needs to be like that '2021-02-04(Year,Month,Day)'")
end_Date = str(input("End Date: "))
starttime=datetime.datetime.strptime(
    start_Date, '%Y-%m-%d')
endtime=datetime.datetime.strptime(
    end_Date, '%Y-%m-%d')
mask = (data['Date'] > starttime.date()) & (data['Date'] <= endtime.date())
data_Mask = data.loc[mask]

print("-----------------------------------------------------------------")
print("Time in Range")
print("  ")
print(data_Mask)
max_Val  = data_Mask['Value'].loc[data_Mask['Value'].idxmax()] 
min_Val  = data_Mask['Value'].loc[data_Mask['Value'].idxmin()] 
sum_val  = data_Mask['Value'].sum()
print("-----------------------------------------------------------------")
print("Minimum, Maximum & Sum Value of Range")
print(" max:",max_Val," min:",min_Val," sum:", sum_val)