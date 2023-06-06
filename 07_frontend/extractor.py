from request_xkcd import RequestXKCD
from xkcdb import XKCDb


def extractor():
    req_xkcd = RequestXKCD()
    db = XKCDb("xkcd.json")

    last_comic_id = 2783
    for id in range(1, last_comic_id+1):
            # ha!
            if id == 404:
                  continue
            data = req_xkcd.query_by_id(id)
            db.insert(data)
            print(f'Added comic {id} data')

    print("Extraction complete")

extractor()