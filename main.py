from fastapi import FastAPI
from completion import justModelsIds, requestCompletion, requestChatCompletion
from pydantic import BaseModel

class Body(BaseModel):
    text: str


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/models")
async def models():
    ids = justModelsIds()
    return { "ids": ids}

@app.post("/complete")
async def complete(body: Body):
    res = requestCompletion(body.text)
    return { "res": res}

@app.post("/chat")
async def chat(body: Body):
    res = requestChatCompletion(body.text)
    return { "res": res}