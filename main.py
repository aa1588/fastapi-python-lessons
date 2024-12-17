from fastapi import FastAPI

app = FastAPI()

dogs = ['beagle','golden retriever', 'poodle','chihuahua']

@app.get("/")
def hello_world():
    return {"msg": "Hello world!"}

@app.get("/dogs")
def get_dogs():
    return dogs

