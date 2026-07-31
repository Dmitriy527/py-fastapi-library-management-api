from fastapi import FastAPI


app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"Hello": name}