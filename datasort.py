# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 19:08:23 2023

@author: Reena Shrestha
"""

import pandas as pd
import os
import numpy as np
from collections import Counter

path = "C:/Users/Reena Shrestha/OneDrive - lamar.edu/Desktop/Machine learning/Project_2"
os.chdir(path)
# convert  text file into a csv file
WM = pd.read_csv('WellMain.txt', sep= '|', encoding= 'unicode_escape')

WQ = pd.read_csv('WaterQualityMajor.txt', sep= '|', encoding= 'unicode_escape'
                 , on_bad_lines='skip')

a = WQ[(WQ['Aquifer'] == 'Woodbine')]


ParamD = dict(Counter(a['ParameterDescription']))
print (ParamD)
Para_list = pd.DataFrame.from_dict(ParamD.items())

#Selecting the Fluoride mg/L as the contaminant
b = a[a['ParameterCode'] == 950]

a = pd.read_csv('Woodbine_data.csv')
b = pd.read_csv('WellDepth1.csv')
z = b.groupby('StateWellNumber').mean()
z.columns

wellid = list(z.index.values)
Av_ppt = list(z.PRISMppt30y)
A = {'StateWellNumber': wellid, 'ppt': Av_ppt}
df_A = pd.DataFrame(A)

WB = pd.merge(a,df_A, on='StateWellNumber')
WB.to_csv('WB.csv')
