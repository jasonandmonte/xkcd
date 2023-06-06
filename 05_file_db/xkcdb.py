import json
import os
from typing import List

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

    def get(self, id) -> dict:
        for x in self.existing_data:
            if x["num"] == int(id):
                return x
        # No match
        return {}

    def list_keyword(self, kw):
        # ref: https://stackoverflow.com/a/26008208
        filtered_data = [d for d in self.existing_data if kw in d["transcript"] or kw in d["alt"] or kw in d["title"]]
        return filtered_data

    def insert(self, data: dict) -> bool:
        result = False
        id = data["num"]
        if not self.check_id_exists(id):
            self.existing_data.append(data)
            self.overwrite()
            result = True
        return result

    def load(self) -> List[dict]:
        if not os.path.exists(self.filename):
            self.create_empty_file()

        with open(self.filename, "r") as infile:
            existing_data = json.load(infile)
        return existing_data

    def overwrite(self) -> None:
        with open(self.filename, "w") as outfile:
            json.dump(self.existing_data, outfile, indent=4)
    


