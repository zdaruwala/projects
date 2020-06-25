#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 11:46:38 2019

@author: zdaruwala
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df2 = pd.read_csv('MyExpt_cells_G0_MAN2A.txt', delimiter = '\t')

df2.columns = ['Image_number', 'Cell_number', 'PLA_count', 'Location_center_X', 'Location_center_Y', 'Location_center_Z', 'Cell_Number', 'Nuclei_Number']
print(df2.PLA_count.mean())
print(df2.PLA_count.std())
print(df2.PLA_count.max())
print(df2.PLA_count.median())

sns.boxplot(data=df2, x='PLA_count')

export_excel = df2.to_excel(r'/Users/zdaruwala/Documents/confocal images/06072019/cellprofiler data/MAN2A and G0 cell data.xlsx', index = None, header=True) 


