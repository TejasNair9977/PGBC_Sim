from fastapi import FastAPI
from apis import apis as api
from models.block import Block

app = FastAPI()

@app.get("/")
async def root():
    api.initiate()
    return {"message": "Connection Complete"}


@app.get("/change")
async def root():
    print(api.change())
    return {"message": "There was a change in the database"}

@app.post("/remotechange")
async def root(block:Block):
    api.makechange(block)
    return 