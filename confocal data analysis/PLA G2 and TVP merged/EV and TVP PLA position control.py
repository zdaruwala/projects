#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 15:34:12 2019

@author: zdaruwala
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df5 = pd.read_csv('MyExpt_cells_TVP_poscontrol.txt', delimiter = '\t')

df5.columns = ['Image_number', 'Cell_number', 'PLA_count', 'Location_center_X', 'Location_center_Y', 'Location_center_Z', 'Cell_Number', 'Nuclei_Number']
print(df5.PLA_count.mean())
print(df5.PLA_count.std())
print(df5.PLA_count.max())
print(df5.PLA_count.median())

sns.boxplot(data=df5, x='PLA_count')

export_excel = df5.to_excel(r'/Users/zdaruwala/Documents/confocal images/06072019/cellprofiler data/TVP positive control cell data.xlsx', index = None, header=True) 
