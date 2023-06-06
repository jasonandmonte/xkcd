import pprint
from request_xkcd import RequestXKCD
from xkcdb import XKCDb

def prompt() -> str:
    another = input("Would you like to enter another? (y/n):")
    while another != "y" and another != "n":
        print("Invalid input. Please enter 'y' or 'n'.")
        another = input("Would you like to enter another? (y/n):")
    return another


def main():
    req_xkcd = RequestXKCD()
    db = XKCDb("xkcd.json")
    next = 1
    while next:
        print("-- Menu --")
        print("1: Get Latest Comic")
        print("2: Get Comic by ID")
        print("3: Get Comics by Keyword")
        choice = int(input("Enter choice (1-3):"))
        
        data = None
        match choice:
            case 1:
                data = req_xkcd.query_latest()
            case 2:
                id = input("Enter an xkcd comic number:")
                data = db.get(id)
            case 3:
                kw = input("Enter keyword:")
                data = db.list_keyword(kw)
            case _:
                print("Please choose a valid number")

        if data:
            print()
            pprint.pprint(data)
            print("\n\n-----------------\n\n")
        
        another = prompt()
        next = 1 if another == "y" else 0

if __name__ == "__main__":
    main()
