from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/change")
async def root():
    return {"message": "There was a change in the database"}