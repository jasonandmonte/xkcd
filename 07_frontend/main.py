# FastAPI tutorial: https://realpython.com/fastapi-python-web-apis/

from xkcdb import XKCDb
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# uvicorn main:app --reload
app = FastAPI()
db = XKCDb("xkcd.json")

# NOTE: Hack to allow me to use fetch from a different "origin".
# We are just on localhost though so its not a big deal.
# ref: https://stackoverflow.com/a/66460861/7582783
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
# base path "home page"
async def root() -> dict:
    return {"message": "/comics/<id>"}

@app.get("/comics/{id}")
# get comic by id
async def get_comic(id: int) -> dict:
    return db.get(id)

