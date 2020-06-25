#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:28:18 2019

@author: zdaruwala
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('MyExpt_cells_G0_TVPmutAB.txt', delimiter = '\t')

df.columns = ['Image_number', 'Cell_number', 'PLA_count', 'Location_center_X', 'Location_center_Y', 'Location_center_Z', 'Cell_Number', 'Nuclei_Number']
print(df.PLA_count.mean())
print(df.PLA_count.std())
print(df.PLA_count.max())
print(df.PLA_count.median())

sns.boxplot(data=df, x='PLA_count')

export_excel = df.to_excel(r'/Users/zdaruwala/Documents/confocal images/06072019/cellprofiler data/G0 and TVPmutAB cell data.xlsx', index = None, header=True) 
