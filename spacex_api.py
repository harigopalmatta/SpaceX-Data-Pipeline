import requests
import pandas as pd

response = requests.get("https://api.spacexdata.com/v5/launches")
launch_data = response.json()

launch_df = pd.DataFrame(launch_data)

print(launch_df.head(5))