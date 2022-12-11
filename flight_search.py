import requests
from flight_data import FlightData
import os
from dotenv import load_dotenv

load_dotenv()

KIWI_TOKEN = os.environ['KIWI_KEY']
KIWI_POINT = os.environ['KIWI_API']

#This class is responsible for talking to the Flight Search API.
class FlightSearch():

    def iata_search(self, city_name):
        location_endpoint = f"{KIWI_POINT}locations/query"
        location_key = {"apikey": KIWI_TOKEN}
        kiwi_header = {
            "term": city_name,
            "location_types": "city"
        }
        location_response = requests.get(url=location_endpoint, params=kiwi_header, headers=location_key)
        location_results = location_response.json()["locations"]
        iata = location_results[0]["code"]
        return iata

    def flight_search(self, flying_from, flying_to, depart_min_date, depart_max_date, min_stay, max_stay):
        search_endpoint = f"{KIWI_POINT}search"
        search_key = {"apikey": KIWI_TOKEN}
        search_header = {
            "fly_from": flying_from,
            "fly_to": flying_to,
            "flight_type": "round",
            "one_for_city": 1,
            "date_from": depart_min_date,
            "date_to": depart_max_date,
            "nights_in_dst_from": min_stay,
            "nights_in_dst_to": max_stay,
            "max_stopovers": 0,
            "curr": "USD"

        }
        search_response = requests.get(url=search_endpoint, params=search_header, headers=search_key)

        try:
            search_results = search_response.json()["data"][0]
        except IndexError:
            print(f"No flights found from {flying_from} to {flying_to}")
            return None

        flight_data = FlightData(
            price=search_results["price"],
            depart_city=search_results["cityFrom"],
            arrival_city=search_results["cityTo"],
            nights_in_dest=search_results["nightsInDest"],
            departure_date=depart_min_date
        )
        print(f"{flight_data.arrival_city}: ${flight_data.price}")
        return flight_data.price
