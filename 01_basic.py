# Requests readthedocs: https://requests.readthedocs.io/en/latest/
# type hints: https://docs.python.org/3/library/typing.html

import requests

def request_xkcd(id: int):
    r = requests.get(f'https://xkcd.com/{id}/info.0.json')
    return r.json()

def main():
    print(request_xkcd(353))

# ref: https://stackoverflow.com/a/419185
if __name__ == "__main__":
    main()

