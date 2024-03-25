


#%%
# import pandas

import pandas as pd

# put CO2 data into a pandas dataframe

df = pd.read_csv('CO2_Dataset.csv')

# filter out EU countries as per list of EU countries (UK Government, 2014) and United Kingdom

eu_and_UK_countries = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Republic of Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'United Kingdom']
eu_UK_df = df[df['Country Name'].isin(eu_and_UK_countries)]
eu_UK_df.to_csv('eu_and_UK_countries.csv')
#%%

# Get an average of each year column and plot that as an overall trend

# import pandas and matplotlib.pyplot for this cell

import pandas as pd
import matplotlib.pyplot as plt

# set display options to show all columns and rows

pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)

# put CO2 data into a pandas dataframe

df_co2 = pd.read_csv('eu_and_UK_countries.csv')

# filter out unneeded columns

co2_per_year = df_co2.select_dtypes(include=['number'])

# get the average of each year

average_co2_per_year = co2_per_year.mean()

# cut out empty columns

average_co2_per_year_filtered = average_co2_per_year['1990':].drop(['2021', '2022'])

# put this set of averages into a new dataframe

df_year_average_co2 = pd.DataFrame(average_co2_per_year_filtered)

#plot this dataframe onto a graph

plt.figure(figsize=(25, 15))
plt.plot(df_year_average_co2.index, df_year_average_co2[0], color='red', marker='o', linestyle='-')
plt.title('Average CO2 Emissions per Year in UK and EU countries')
plt.xlabel('Year')
plt.ylabel('Average CO2 Emissions (kt)')
# make sure Y axis starts from 0
plt.ylim(0)
plt.grid(True)
plt.show()



# %%

# predicting trends for 2050 with linear regression

# import pandas, numpy and matplotlib.pyplot for this cell

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# import sklearn for linear regression

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# set display options to show all columns and rows

pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)

# put CO2 data into a pandas dataframe

df_co2 = pd.read_csv('eu_and_UK_countries.csv')

# filter out unneeded columns

co2_per_year = df_co2.select_dtypes(include=['number'])

# get the average of each year

average_co2_per_year = co2_per_year.mean()

# cut out empty columns

average_co2_per_year_filtered = average_co2_per_year['1990':].drop(['2021', '2022'])

# put this set of averages into a new dataframe

df_year_average_co2 = pd.DataFrame(average_co2_per_year_filtered)

#plot this dataframe onto a graph

plt.figure(figsize=(25, 15))
plt.plot(df_year_average_co2.index, df_year_average_co2[0], color='red', marker='o', linestyle='-')
plt.title('Average CO2 Emissions per Year in UK and EU countries')
plt.xlabel('Year')
plt.ylabel('Average CO2 Emissions (kt)')
plt.grid(True)
plt.show()

# create linear regression model and fit it to the data

fit = LinearRegression().fit(np.array(df_year_average_co2.index).reshape(-1, 1), df_year_average_co2[0])







# %%
