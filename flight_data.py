#This class is responsible for structuring the flight data.
class FlightData:
    def __init__(self, price, depart_city, arrival_city, nights_in_dest, departure_date):
        self.price = price
        self.depart_city = depart_city
        self.arrival_city = arrival_city
        self.nights_in_dest = nights_in_dest
        self.departure_date = departure_date
        # self.return_date = self.departure_date + self.nights_in_dest
        self.curr = "USD"
