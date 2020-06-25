#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 13:20:35 2019

@author: zdaruwala
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df3 = pd.read_csv('MyExpt_cells_MAN2A_G2.txt', delimiter = '\t')

df3.columns = ['Image_number', 'Cell_number', 'PLA_count', 'Location_center_X', 'Location_center_Y', 'Location_center_Z', 'Cell_Number', 'Nuclei_Number']
print(df3.PLA_count.mean())
print(df3.PLA_count.std())
print(df3.PLA_count.max())
print(df3.PLA_count.median())

sns.boxplot(data=df3, x='PLA_count')

export_excel = df3.to_excel(r'/Users/zdaruwala/Documents/confocal images/06072019/cellprofiler data/MAN2A and G2 cell data.xlsx', index = None, header=True) 
