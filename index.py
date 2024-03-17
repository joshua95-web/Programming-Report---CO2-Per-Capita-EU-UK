


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

# import pandas again

import pandas as pd

# set display options to show all columns and rows

pd.set_option('display.max_columns', None)
pd.set_option('display.max_columns', None)

# put CO2 data into a pandas dataframe

df_co2 = pd.read_csv('eu_and_UK_countries.csv')

# filter out unneeded columns

co2_per_year = df_co2.select_dtypes(include=['number'])

# get the average of each year

average_co2_per_year = co2_per_year.mean()

# get rid of empty columns

print(average_co2_per_year)



# %%
