import yaml


class Crime:

    def __init__(self, filename: str):
        with open(filename, 'r') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def __getattr__(self, key: str):
        return self.data[key]
