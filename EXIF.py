from exif import Image


class EXIF:

    def __init__(self, filename: str):
        self.filename = filename
        with open(filename, 'rb') as f:
            self.image = Image(f)
            self.has_exif = self.image.has_exif
            if not self.has_exif:
                return
            latitude_sign = 1 if self.image.gps_latitude_ref == 'N' else -1
            longitude_sign = 1 if self.image.gps_longitude_ref == 'E' else -1
            self.latitude = (self.image.gps_latitude[0] + self.image.gps_latitude[1] / 60 + self.image.gps_latitude[
                2] / 3600) * latitude_sign
            self.longitude = (self.image.gps_longitude[0] + self.image.gps_longitude[1] / 60 + self.image.gps_longitude[
                2] / 3600) * longitude_sign
            self.link = f"https://maps.google.com/?q={self.latitude},{self.longitude}"