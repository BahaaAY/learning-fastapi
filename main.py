from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int): # the : int defines the type of the param (this will provide builtin validation by pydantic :))))))
    return {"item_id": item_id}

