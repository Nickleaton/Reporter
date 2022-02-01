import glob
import os

from EXIF import EXIF
from config import Config
from crime import Crime
from geocode_cache import GeocodeCache


class Directory:

    def __init__(self, dirname: str):
        self.dirname = dirname
        self.files = glob.glob(os.path.join(dirname, "*.jpg"))

    def process(self, cache: GeocodeCache):
        for filename in self.files:
            exif = EXIF(filename)
            if not exif.has_exif:
                print(f"{filename} has no meta data")
                continue
            print(f"\n{filename}")
            address = cache.reverse_geocode(exif.latitude, exif.longitude)
            print(filename, exif.link, exif.latitude, exif.longitude, address[0]['formatted_address'])


config = Config()
crime = Crime('crime.yaml')
print(crime.role)
print(crime.details)
with GeocodeCache("cache.json", config.GOOGLE_API_KEY) as gc:
    d = Directory("photos")
    d.process(gc)
