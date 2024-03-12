


# filter out EU countries as per list of EU countries (UK Government, 2014)
#%%
import pandas as pd

df = pd.read_csv('CO2_Dataset.csv')

eu_countries = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Republic of Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary', 'Ireland', 'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden']
eu_df = df[df['Country Name'].isin(eu_countries)]
eu_df.to_csv('eu_countries.csv')
#%%
import pandas as pd


# use pandas to group data into useful categories
# use matplotlib to plot data

