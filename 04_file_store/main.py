import requests
import pprint
import json
import os
from typing import List

class RequestXKCD:
    def __init__(self) -> None:
        self.url = "https://xkcd.com"

    def query_by_id(self, id: int):
       r = requests.get(f'{self.url}/{id}/info.0.json')
       return r.json()


class XKCDb:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.existing_data = self.load()

    def check_id_exists(self, id: int) -> bool:
        # ref: https://stackoverflow.com/a/46136685
        return any(obj.get('id') == id for obj in self.existing_data)

    def create_empty_file(self) -> None:
        with open(self.filename, "w") as outfile:
            outfile.write("[]")

    def insert(self, data: dict) -> bool:
        result = False
        id = data["num"]
        if not self.check_id_exists(id):
            self.existing_data.append(data)
            self.overwrite()
            result = True
        return result

    def load(self) -> List[dict]:
        # guard against missing file
        if not os.path.exists(self.filename):
            self.create_empty_file()

        with open(self.filename, "r") as infile:
            existing_data = json.load(infile)
        return existing_data

    def overwrite(self) -> None:
        with open(self.filename, "w") as outfile:
            json.dump(self.existing_data, outfile, indent=4)


def prompt() -> str:
    another = input("Would you like to enter another? (y/n): ")
    while another != "y" and another != "n":
        print("Invalid input. Please enter 'y' or 'n'.")
        another = input("Would you like to enter another? (y/n): ")
    return another


def main():
    req_xkcd = RequestXKCD()
    db = XKCDb("xkcd.json")
    next = 1
    while next:
        id = int(input("Enter an xkcd comic number: "))
        data = req_xkcd.query_by_id(id)

        db.insert(data)

        print()
        pprint.pprint(data)
        print("\n\n-----------------\n\n")
        
        another = prompt()
        next = 1 if another == "y" else 0

if __name__ == "__main__":
    main()
