from data_manager import DataManager
from flight_search import FlightSearch
from pprint import pprint

#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_data()["prices"]

for city in sheet_data:
    flights_data = flight_search.flight_search("PHL", city["iataCode"], "01/01/2022", "04/01/2022", 7, 14)

    if flights_data is None:
        continue
    elif len(city["iataCode"]) == 0 or flights_data < city["lowestPrice"]:
        data_manager.update_data(city["id"], flight_search.iata_search(city["city"]), flights_data)
