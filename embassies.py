#!/usr/bin/env python
# vim: set fileencoding=utf8 :
from pygeocoder import Geocoder
import re
import sys
from bunch import Bunch

pins = {}

def generate_embassy_addresses():
    countries = []
    embassies_raw = []
    embassies = {}

    country_file = open("country_stems.txt")
    country_line = clean_text(country_file.readline())
    while(country_line != ""):
        countries.append(country_line)
        country_line = clean_text(country_file.readline())

    print("Loaded " + str(len(countries)) + " countries.")

    embassy_file = open("embassies.txt")
    embassy_line = clean_text(embassy_file.readline())

    while(embassy_line != ""):
        embassies_raw.append(embassy_line)
        embassy_line = clean_text(embassy_file.readline())

    for i in range(len(embassies_raw)):
        country_matches = [c for c in countries if c in embassies_raw[i]]
        for country in country_matches:
            for j in range(i, len(embassies_raw)):
                if (looks_like_address(embassies_raw[j]) and
                not embassies.has_key(country)):
                    embassies[country] = embassies_raw[j]

    print("Detected " + str(len(embassies)) + " countries in embassy file.")
    return embassies

def looks_like_address(text_line):
    postcode_regex = re.compile("[A-Z]+[0-9]+[A-Z]? ?[0-9][A-Z][A-Z]")
    postcodes = postcode_regex.findall(text_line)
    return len(postcodes) > 0

def clean_text(source):
    return source.replace("\n", "").replace("\r", "").replace("\0", "")

def geocode(embassy_address_map):
    for country in embassy_address_map.keys():
        results = Bunch()
        results.coordinates = {0: 'null', 1: 'null'}
        #results = Geocoder.geocode(embassy_address_map[country])
        pins[country] = [results[0].coordinates[0], results[0].coordinates[1], "allflags/" + country.lower() + ".gif"]

if __name__ == '__main__':
    args = sys.argv
    embassy_address_map = generate_embassy_addresses()
    geocode(embassy_address_map)
    print(str(len(pins)))
    print('\n\n\n')
    print(pins)
