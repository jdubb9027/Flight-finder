import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Sheety
SHEETY_END = os.environ['SHEETY_POINT']
SHEETY_TOKEN = os.environ['SHEETY_BEAR']

BEAR_HEAD = {
    'Authorization': SHEETY_TOKEN
}

#This class is responsible for talking to the Google Sheet.
class DataManager:

    def get_data(self):
        data = requests.get(url=SHEETY_END, headers=BEAR_HEAD).json()
        return data

    def update_data(self, city_id, iata, price):
        updated_data = {
            'price': {
                'iataCode': iata,
                'lowestPrice': price
            }
        }
        update_sheet = requests.put(url=f"{SHEETY_END}/{city_id}", json=updated_data, headers=BEAR_HEAD)
        return update_sheet.raise_for_status()
