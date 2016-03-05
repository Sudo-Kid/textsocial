# intent.py
import csv
import json
import sys

from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine


def round_street_numbers(street_number):
    if street_number > 100:
        pass

engine = IntentDeterminationEngine()

keywords = [
    'service',
    'med',
]

for key in keywords:
    engine.register_entity(key, "KeyWords")

with open('addresses.csv', 'rb') as csvfile:
    records = csv.reader(csvfile, delimiter=',')
    full_address = []
    street_number = []
    rounded_street_number = []
    street_dir_prefix = []
    street_name = []
    street_type = []
    locality = []

    for row in records:
        full_address.append(row[6])
        street_number.append(row[8])
        rounded_street_number.append(row[8])
        street_dir_prefix.append(row[10])
        street_name.append(row[11])
        street_type.append(row[12])
        locality.append(row[14])

for key in full_address:
    engine.register_entity(key, "FullAddress")

for key in street_number:
    engine.register_entity(key, "StreetNumber")

for key in street_dir_prefix:
    engine.register_entity(key, "StreetDirPrefix")

for key in street_name:
    engine.register_entity(key, "StreetName")

for key in street_type:
    engine.register_entity(key, "StreetType")

for key in locality:
    engine.locality(key, "Locality")

address_intent = IntentBuilder("AddressIntent")\
    .require("Locality")\
    .optionally("FullAddress")\
    .optionally("StreetNumber")\
    .optionally("StreetDirPrefix")\
    .optionally("StreetName")\
    .optionally("StreetType")\
    .build()

engine.register_intent_parser(address_intent)

if __name__ == "__main__":
    for intent in engine.determine_intent(' '.join(sys.argv[1:])):
        if intent.get('confidence') > 0:
            print(json.dumps(intent, indent=4))
