# argparse: https://realpython.com/command-line-interfaces-python-argparse/

import requests
from argparse import ArgumentParser

def request_xkcd(id: int):
    r = requests.get(f'https://xkcd.com/{id}/info.0.json')
    return r.json()

def main():
    # allows `python3 02_cli_args.py 1234`
    parser = ArgumentParser()
    parser.add_argument('number', type=int, help='xkcd comic number')
    args = parser.parse_args()
    id = args.number

    print(request_xkcd(id))

if __name__ == "__main__":
    main()
