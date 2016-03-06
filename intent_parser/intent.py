# intent.py
from flask import Flask, Response, request
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

# for key in full_address:
#    engine.register_entity(key, "FullAddress")

for key in street_number:
    engine.register_entity(key, "StreetNumber")

# for key in street_dir_prefix:
#     engine.register_entity(key, "StreetDirPrefix")

for key in street_name:
    engine.register_entity(key, "StreetName")

# for key in street_type:
#    engine.register_entity(key, "StreetType")

# for key in locality:
    # engine.locality(key, "Locality")
    # .optionally("Locality")\
    # .optionally("FullAddress")\
    # .optionally("StreetDirPrefix")\

address_intent = IntentBuilder("AddressIntent")\
    .optionally("StreetNumber")\
    .optionally("StreetName")\
    .optionally("StreetType")\
    .build()

engine.register_intent_parser(address_intent)

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def get_address():
    print(request.form.to_dict())
    intent = engine.determine_intent(' '.join(request.form['message']))
    return Response(intent, mimetype='application/json', headers={'Cache-Control': 'no-cache', 'Access-Control-Allow-Origin': '*'})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
