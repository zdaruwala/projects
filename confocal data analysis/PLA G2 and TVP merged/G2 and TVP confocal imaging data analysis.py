#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 23:59:11 2019

@author: zdaruwala
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df1 = pd.read_csv('MyExpt_Cells_g2_TVP.txt', delimiter = '\t')
df1.columns = ['Image_number', 'Cell_number', 'PLA_count', 'Location_center_X', 'Location_center_Y', 'Location_center_Z', 'Cell_Number', 'Nuclei_Number']
#print(df1.PLA_count.mean())
#print(df1.PLA_count.std())
#print(df1.PLA_count.max())
#print(df1.PLA_count.median())

df = pd.read_csv('MyExpt_cells_G0_TVP.txt', delimiter= '\t')
df.columns = ['Image_number', 'Cell_number', 'PLA_count', 'Location_center_X', 'Location_center_Y', 'Location_center_Z', 'Cell_Number', 'Nuclei_Number']
#print(df.PLA_count.mean())
#print(df.PLA_count.std())
#print(df.PLA_count.max())
#print(df.PLA_count.median())

PLA_count_less_than_70 = df.loc[(df['PLA_count'] >= 0) & (df['PLA_count'] <= 40)]

#df1.hist(column='PLA_count', range=(0,70), bins=70)
#sns.distplot(df1['PLA_count'])
#sns.distplot(PLA_count_less_than_70['PLA_count'])

sns.boxplot(data=df1, x='PLA_count')

export_excel = df1.to_excel(r'/Users/zdaruwala/Documents/confocal images/06072019/cellprofiler data/G2 and TVP cell data.xlsx', index = None, header=True) 
