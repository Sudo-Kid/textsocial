from django.views.generic import View
from django.http import HttpResponse

import csv
import os

from adapt.intent import IntentBuilder
from adapt.engine import IntentDeterminationEngine


class Index(View):
    def post(self, request, *args, **kwargs):
        engine = IntentDeterminationEngine()

        keywords = [
            'service',
            'med',
        ]

        for key in keywords:
            engine.register_entity(key, "KeyWords")

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
        intent = engine.determine_intent(request.POST['message'])
        return HttpResponse(intent)
