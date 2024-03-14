


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
 
# import matplotlib and pandas
import pandas as pd
import matplotlib.pyplot as plt


# put the data into a new dataframe

df_eu_UK = pd.read_csv('eu_and_UK_countries.csv')

# Transpose the data so it can be plotted efficiently

df_transposed = df_eu_UK.set_index('Country Name').T[35:]

#Plot the data for each country

plt.figure(figsize=(25, 15))

#for country in df_transposed.columns:
#    plt.plot(df_transposed.index, df_transposed[country], label=country)

for index, row in df_eu_UK.iterrows():
    country = row['Country Name']
    co2_data = row.loc['1990':'2020']
    plt.plot(range(1990, 2021), co2_data.values, label=country)


plt.title('CO2 Emissions Over Time')
plt.xlabel('Year')
plt.ylabel('CO2 emissions (metric tons per capita)')
plt.legend()
plt.grid(True)
plt.xticks(range(1990, 2021, 2))  # Adjust the x-axis ticks for better readability
plt.show()


# use pandas to group data into useful categories
# use matplotlib to plot data


# %%
