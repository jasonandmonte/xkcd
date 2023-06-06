import requests
import pprint

class RequestXKCD:
    def __init__(self) -> None:
        self.url = "https://xkcd.com"

    def query_by_id(self, id: int) -> dict:
       r = requests.get(f'{self.url}/{id}/info.0.json')
       return r.json()


def prompt() -> str:
    another = input("Would you like to enter another? (y/n): ")
    while another != "y" and another != "n":
        print("Invalid input. Please enter 'y' or 'n'.")
        another = input("Would you like to enter another? (y/n): ")
    return another

def main():
    req_xkcd = RequestXKCD()
    next = 1
    while next:
        id = int(input("Enter an xkcd comic number: "))
        print()
        pprint.pprint(req_xkcd.query_by_id(id))
        print("\n\n-----------------\n\n")
        
        another = prompt()
        next = 1 if another == "y" else 0

if __name__ == "__main__":
    main()
