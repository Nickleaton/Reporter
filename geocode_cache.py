import json
import os

import googlemaps


class GeocodeCache:

    def __init__(self, filename: str, key: str):
        self.filename = filename
        self.key = key
        self.gmaps = googlemaps.Client(key)
        if os.path.exists(filename):
            self.data = json.load(open(filename, 'r'))
        else:
            self.data = {}

    def reverse_geocode(self, latitude: float, longitude: float) -> str:
        key = f"{latitude},{longitude}"
        if key in self.data:
            return self.data[key]
        result = self.gmaps.reverse_geocode((latitude, longitude))
        self.data[key] = result
        return result

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        with open(self.filename, 'w') as f:
            f.write(json.dumps(self.data))
