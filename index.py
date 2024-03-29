


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

# calculating and defining the maximum emissions to ensure highest number is shown on graph

max_co2_emissions = df_year_average_co2.max()[0]

y_axis_limit = max_co2_emissions + 0.7

#plot this dataframe onto a graph

plt.figure(figsize=(25, 12))
plt.plot(df_year_average_co2.index, df_year_average_co2[0], color='red', marker='o', linestyle='-')
plt.title('Average CO2 Emissions per Year in UK and EU countries')
plt.xlabel('Year')
plt.ylabel('Average CO2 Emissions (metric tons per capita)')
# make sure Y axis starts from 0
plt.xticks(rotation='vertical')
plt.ylim(0, y_axis_limit)
plt.tick_params(axis='y', labelsize=20)
plt.grid(True)
plt.show()



# %%


# import pandas and matplotlib.pyplot for this cell, as well as sklearn for linear regression

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np

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

# create a linear regression model

x = df_year_average_co2.index.values.reshape(-1, 1).astype(float)
y = df_year_average_co2[0].values.reshape(-1, 1).astype(float)

fit = LinearRegression().fit(x, y)

m = round(fit.coef_.flatten()[0], 6)
c = round(fit.intercept_.flatten()[0], 6)

yp1 = m * x + c

# create a linear regression model for the future, spacing out the lines to 2050

xp2 = np.linspace(2021, 2050, 29)

yp2 = m * xp2 + c

# calculating and defining the maximum emissions to ensure highest number is shown on graph

max_co2_emissions = df_year_average_co2.max()[0]

y_axis_limit = max_co2_emissions + 0.7

plt.figure(figsize=(12, 10))
plt.plot(x, y, color='red', marker='o', linestyle='-', label='CO2 Emissions')
plt.plot(xp2, yp2, 'r-', color='blue', label='Linear Regression')
plt.title('Average CO2 Emissions per Year in UK and EU countries')
plt.xlabel('Year')
plt.ylabel('Average CO2 Emissions (metric tons per capita)')
plt.ylim(0, y_axis_limit)
plt.grid(True)
plt.xticks(rotation='vertical')
plt.legend()
plt.show()


# %%

