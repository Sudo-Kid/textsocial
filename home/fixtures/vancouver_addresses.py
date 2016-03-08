import os
import csv


civic_id = []
latitude = []
longitude = []
full_address = []
street_number_prefix = []
street_number = []
street_number_suffix = []
street_dir_prefix = []
street_name = []
street_type = []
street_dir_suffix = []
street_locality = []
last_modified_date = []
street_name = []

with open(os.getcwd() + '/fixtures/vancouver_addresses.csv', 'rb') as csvfile:
    records = csv.reader(csvfile, delimiter=',')

    for row in records:
        civic_id.append(row[0])
        latitude.append(row[2])
        longitude.append(row[3])
        full_address.append(row[6])
        street_number_prefix.append(row[7])
        street_number.append(row[8])
        street_number_suffix.append(row[9])
        street_dir_prefix.append(row[10])
        street_name.append(row[11])
        street_type.append(row[12])
        street_dir_suffix.append(row[13])
        street_locality.append(row[14])
        last_modified_date.append(row[23])
