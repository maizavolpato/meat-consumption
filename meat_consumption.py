#first let's import all necessery libraries for this analysis
import pandas as pd
import numpy as np

#using pandas library and 'read_csv' function to read amazon.csv file
df = pd.read_csv('meat_consumption.csv')

#before continue using data it's important to check the information that we have
# df.isna().sum()

# df.info()

#unique valeus as well
df['LOCATION'].unique()
df['SUBJECT'].unique()
df['MEASURE'].unique() #there're two measures here, for a better analysis I'll use only Kg per person
df['TIME'].unique() #there're many years that I'll del, because I don't have sure if it's complete
df.rename(columns = {'LOCATION':'Country', 'SUBJECT': 'Type_meat', 'MEASURE': 'Measure','TIME':'Year', 'Value': 'Total'}, inplace = True)

#Selecting only row with kg per capita and del years before 2000 and after 2017
dfKgCap = df.loc[(df['Measure'] == 'KG_CAP') & (df['Year'] >= 2000) & (df['Year'] <= 2017)]

#let's start to explore our data
print("""\n The people around the world are trying to change their food consumption.
They are replacing the consumption of some foods such as meat with foods with the same nutritional value, but less aggressive to their body.
Let's see some information abou the meat consumption in diferents countries in 2000 until 2017.""")
#the total consumption per year
total_kg_year = dfKgCap.groupby(by = ['Year'])['Total'].sum().round(3).reset_index()
print("\n This is the total meat consuption per year:\n")
print(total_kg_year)

#the total consumption per country
total_kg_country = dfKgCap.groupby(by = ['Country'])['Total'].sum().round(3).sort_values(ascending = False).reset_index()
print("\n This is the total meat consuption per country:\n")
print(total_kg_country)

#exploring a little more the 3 highest countries
print("""\n The country that most consumption is United States, following by Autralia and Israel.
Let's explore a little about these countries.""")
dfUSA = dfKgCap.loc[(df['Country'] == 'USA')
