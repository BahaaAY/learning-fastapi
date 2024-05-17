from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

@app.get("/")
async def root():
    return {"message" : "Hello World!"}


@app.get("/items")
async def get_items(skip: int=0, limit: int=10):
    return fake_items_db [skip : skip + limit]

@app.get("/items/{item_id}")
async def get_item(item_id: int, q : int):
     item = fake_items_db[item_id]
     if item is None:
         return {"message" : "Item Not Found!"}
     return {"item": item, "quantity":q}

