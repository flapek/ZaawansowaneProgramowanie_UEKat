import json
from collections import namedtuple
import requests

URL = 'https://api.openbrewerydb.org/breweries'


class Browar(object):
    def __init__(self, json: str):
        self.id = json['id'],
        self.name = json['name'],
        self.brewery_type = json['brewery_type'],
        self.street = json['street'],
        self.address_2 = json['address_2'],
        self.address_3 = json['address_3'],
        self.city = json['city'],
        self.state = json['state'],
        self.county_province = json['county_province'],
        self.postal_code = json['postal_code'],
        self.country = json['country'],
        self.longitude = json['longitude'],
        self.latitude = json['latitude'],
        self.phone = json['phone'],
        self.website_url = json['website_url'],
        self.updated_at = json['updated_at'],
        self.created_at = json['created_at']

    def __str__(self):
        return f'{self.id}, {self.name}, {self.brewery_type}'


def customBrowarDecoder(browarDict):
    return namedtuple('X', browarDict.keys())(*browarDict.values())


params = {'by_city': None, 'per_page': 20}
response = requests.get(URL, params=params)

browar = json.loads(response.json()[0], object_hook=customBrowarDecoder)

print(browar)

# data = response.json()
# print(data)

# result = Browar(response.json()[0])
# print(result)
