# FastAPI tutorial: https://realpython.com/fastapi-python-web-apis/

from xkcdb import XKCDb
from fastapi import FastAPI


app = FastAPI()
db = XKCDb("xkcd.json")

@app.get("/")
# base path "home page"
async def root() -> dict:
    return {"message": "/comics/<id>"}

@app.get("/comics/{id}")
# get comic by id
async def get_comic(id: int) -> dict:
    return db.get(id)

