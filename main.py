import fastapi
from fastapi import FastAPI


app=FastAPI()


@app.get("/")
def read_root():
    return {"Hello, FastAPI"}

@app.get("/greet/{name}")
def read_item(name: str, q: str = None): 
    return {"name": name, "q": q} 
