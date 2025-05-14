from http.client import HTTPException
from fastapi import FastAPI

app = FastAPI()


items=[]
@app.get("/items/{item_id}")
async def get_item(item_id: int, q: str = None):
   if item_id < len(items):
       return items[item_id]
   else:
       raise HTTPException(status_code=404, detail="Item not found")
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items")
async def create_items(item: str):
    items.append(item)
    return items

@app.put("/")
async def put():
    return {"message": "Hello World from PUT"}

@app.delete("/")
async def delete():
    return {"message": "Hello World from DELETE"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    