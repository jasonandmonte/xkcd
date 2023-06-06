import requests

class RequestXKCD:
    def __init__(self) -> None:
        self.url = "https://xkcd.com"

    def query_by_id(self, id: int):
       r = requests.get(f'{self.url}/{id}/info.0.json')
       return r.json()

    def query_latest(self) -> dict:
        r = requests.get(f'{self.url}/info.0.json')
        return r.json()