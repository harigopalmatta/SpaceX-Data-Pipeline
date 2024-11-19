import requests
import pandas as pd

url = "https://api.spacexdata.com/v5/launches"
launch_data = pd.read_json(url)

launch_df = pd.DataFrame(launch_data)

print(launch_df['rocket'])
print(launch_df['name'])
print(launch_df['flight_number'])
print(launch_df['success'])
print(launch_df.dtypes)