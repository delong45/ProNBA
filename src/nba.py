import requests

class Stats(object):
    def __init__(self, url):
        self.url = url

    def request(self):
        response = requests.get(self.url)
        return response
