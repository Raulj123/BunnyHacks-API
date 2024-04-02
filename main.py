from typing import Union
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/egg2Hunt')
def message():
    return {
        "message": "Oh no! It seems that watering the eggs accidentally washed the code into Local Storage! Look for a key that rhymes with 'gloom' – the value of that key is your code!",
        "secretCode": "🌊"
    }
