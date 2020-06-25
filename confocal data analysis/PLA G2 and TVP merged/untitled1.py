#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 18:29:29 2019

@author: zdaruwala
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('MyExpt_cells.txt', delimiter = '\t')

df.columns = ['Image_number', 'Cell_number', 'PLA_count', 'Location_center_X', 'Location_center_Y', 'Location_center_Z', 'Cell_Number', 'Nuclei_Number']
print(df.PLA_count.mean())
print(df.PLA_count.std())
print(df.PLA_count.max())
print(df.PLA_count.median())

sns.boxplot(data=df, x='PLA_count')

export_excel = df.to_excel(r'/Users/zdaruwala/Documents/confocal images/07022019/CELL PROFILER DATA G0 AND MAN2A/G0 and TVP cell data.xlsx', index = None, header=True) 
