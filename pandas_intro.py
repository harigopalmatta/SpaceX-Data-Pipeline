import pandas as pd
data = { 
    'rockets' : [ 'Falcon', 'Falcon 9', 'Faclon Heavy'],
'launches': [5,100,3]
}

#Convert json data to pandas dataframe
df = pd.DataFrame(data)
#Print dataframe
print(df)

#Print rocket column info
print(df['rockets'])

#Print rockets which have >5 launches
filtered_df=df.query("launches > 5")
print(filtered_df['rockets'])

#Add new column to existing df
success_rate= [0.96,0.91,0.95]
df['success_rate'] = success_rate
print(df)

