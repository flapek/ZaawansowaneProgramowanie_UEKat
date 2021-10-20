import json
import requests

class Browar:
    def __init__(self, j):
        self.id = j.get('id'),
        self.name = j.get('name'),
        self.brewery_type = j.get('brewery_type'),
        self.street = j.get('street'),
        self.address_2 = j.get('address_2'),
        self.address_3 = j.get('address_3'),
        self.city = j.get('city'),
        self.state = j.get('state'),
        self.county_province = j.get('county_province'),
        self.postal_code = j.get('postal_code'),
        self.country = j.get('country'),
        self.longitude = j.get('longitude'),
        self.latitude = j.get('latitude'),
        self.phone = j.get('phone'),
        self.website_url = j.get('website_url'),
        self.updated_at = j.get('updated_at'),
        self.created_at = j.get('created_at')

    def __str__(self):
        print(f'{self.id}, {self.name}, {self.brewery_type}')

response = requests.get("https://api.openbrewerydb.org/breweries?page=20")

result = Browar(response.json()[1])
print(result)