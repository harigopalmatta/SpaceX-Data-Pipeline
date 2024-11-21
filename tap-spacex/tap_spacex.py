import singer
import pandas as pd

LOGGER = singer.get_logger()

schema = {
    'properties':{
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'date-utc': {'type': 'string', 'format': 'date-time'}
    }
}

def main():
    url = "https://api.spacexdata.com/v5/launches"
    launch_data = pd.read_json(url)
    launch_data = launch_data.fillna('')

    records = launch_data.to_dict(orient='records')
    singer.write_schema('launches',schema,'id')
    singer.write_records('launches', records)

if __name__ == '__main__':
    main()