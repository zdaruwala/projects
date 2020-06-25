#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 10:00:54 2020

@author: zdaruwala
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# creating dataframes using pandas
df_deaths_boro_age = pd.read_csv('deaths-by-boro-age.csv', delimiter= ',')
df_deaths_race_age = pd.read_csv('deaths-by-race-age.csv', delimiter= ',')
df_deaths_underlying_conditions = pd.read_csv('deaths-by-underlying-conditions.csv', delimiter= ',')
df_probable_confirmed_age = pd.read_csv('probable-confirmed-by-age.csv', delimiter= ',')
df_probable_confirmed_boro = pd.read_csv('probable-confirmed-by-boro.csv', delimiter= ',')
df_probable_confirmed_location = pd.read_csv('probable-confirmed-by-location.csv', delimiter= ',')
df_probable_confirmed_race = pd.read_csv('probable-confirmed-by-race.csv', delimiter= ',')
df_probable_confirmed_sex = pd.read_csv('probable-confirmed-by-sex.csv', delimiter= ',')
df_probable_confirmed_dod = pd.read_csv('probable-confirmed-dod.csv', delimiter= ',')


print(df_deaths_boro_age)



df_deaths_boro_age.plot(kind='bar',x='BOROUGH_GROUP',y='AGE_65_74_YRS')

