def prepare_country_stats(oecd_bli, gdp_per_capita):
    # Select the column of interest (Life satisfaction) from OECD data
    oecd_bli = oecd_bli[oecd_bli["INEQUALITY"]=="TOT"]
    oecd_bli = oecd_bli.pivot(index="Country", columns="Indicator", values="Value")
    
    # Rename GDP column and set the index to Country
    gdp_per_capita.rename(columns={"2015": "GDP per capita"}, inplace=True)
    gdp_per_capita.set_index("Country", inplace=True)
    
    # Merge the two datasets on the Country column
    full_country_stats = pd.merge(left=oecd_bli, right=gdp_per_capita,
                                  left_index=True, right_index=True)
    
    # Sort by GDP per capita
    full_country_stats.sort_values(by="GDP per capita", inplace=True)
    
    return full_country_stats[["GDP per capita", "Life satisfaction"]]


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model
# Load the data
oecd_bli = pd.read_csv("Learning ml/BLI_27102023090237081.csv", thousands=',')
gdp_per_capita = pd.read_csv("Learning ml/GDP.csv",thousands=',',delimiter='/t',
encoding='latin1', na_values="n/a")

print(gdp_per_capita.head())
print(gdp_per_capita)
# Prepare the data
country_stats =prepare_country_stats(oecd_bli, gdp_per_capita)
