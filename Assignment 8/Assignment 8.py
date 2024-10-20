import json
from pymongo import MongoClient

jsonpath = 'C://Users//Student//Documents//MSCAI-RG//Assignment 7//Untitled-1.json'
with open(jsonpath, 'r') as file:
    reference_data = json.load(file)

# Extract
visa_rates = reference_data['visa_rates']
airport_locations = reference_data['airports_location']

city_to_country_map = {
    "new_york": "usa",
    "dallas": "usa",
    "beijing": "china",
    "colombo": "sri_lanka",
    "hong_kong": "china",
    "kandy": "sri_lanka",
    "wuhan": "china",
    "chicago": "usa",
    "tokyo": "japan"
}

location_to_visa_rate = {
    location.lower(): visa_rates.get(city_to_country_map.get(location.lower(), ""), 0)
    for location in airport_locations
}
#print("Location to Visa Rate Mapping:", location_to_visa_rate)

client = MongoClient('mongodb://localhost:27017/')
db = client['Airline']
tickets_collection = db['Tickets']

def calculate_final_cost(ticket):
    last_city = ticket['visa_stamped_location'][-1].lower()
        
    visa_rate = location_to_visa_rate.get(last_city, 0)
        
    final_cost = ticket['ticket_price'] + visa_rate
    return final_cost

# Retrieve
tickets = tickets_collection.find()

print("\nTicket Final Prices:")
for ticket in tickets:
    final_cost = calculate_final_cost(ticket)
    print(f"Ticket ID: {ticket['ticket_id']} for {ticket['passenger_name']} with Ticket Price as {ticket['ticket_price']} and Final Cost = {final_cost}")