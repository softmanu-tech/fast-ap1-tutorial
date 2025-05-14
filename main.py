from fastapi import FastAPI

app = FastAPI()


items=[]
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/items")
async def create_items(item: str):
    items
    return {"message": "Hello World from POST"}

@app.put("/")
async def put():
    return {"message": "Hello World from PUT"}

@app.delete("/")
async def delete():
    return {"message": "Hello World from DELETE"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
    