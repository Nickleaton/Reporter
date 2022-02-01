import yaml


class Config:

    def __init__(self):
        with open('config.yaml', 'r') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)

    def __getattr__(self, key: str):
        return self.data[key]
