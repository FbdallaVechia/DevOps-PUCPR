from fastapi import FastAPI
import random
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/teste")
async def funcaoteste():
    return {"teste": True, "numero aleatório: ": random.randint(0, 1000)}