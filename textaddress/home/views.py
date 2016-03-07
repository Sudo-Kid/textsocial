from django.http import JsonResponse
from django.views.generic import View

import csv
import os
import json

from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine


def get_intent(message):
    engine = IntentDeterminationEngine()

    keywords = [
        'service',
        'med',
        'clinic',
        'walk in',
    ]

    for key in keywords:
        engine.register_entity(key, "KeyWords")
    print(os.getcwd())
    with open(os.getcwd() + '/home/addresses.csv', 'rb') as csvfile:
        records = csv.reader(csvfile, delimiter=',')
        street_number = []
        street_name = []

        for row in records:
            street_number.append(row[8])
            street_name.append(row[11])

    for key in street_number:
        engine.register_entity(key, "StreetNumber")

    for key in street_name:
        engine.register_entity(key, "StreetName")

    address_intent = IntentBuilder("AddressIntent")\
        .require("KeyWords")\
        .optionally("StreetNumber")\
        .optionally("StreetName")\
        .build()

    engine.register_intent_parser(address_intent)
    for intent in engine.determine_intent(''.join(message)):
        return intent


class Index(View):
    def post(self, request, *args, **kwargs):
        message = json.loads(request.body).get('message')
        intent = get_intent(message)
        print(intent)
        return JsonResponse(intent, safe=False)
