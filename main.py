from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/egg2Hunt')
def message():
    return {
        "message": "Oh no! It seems that watering the eggs accidentally washed the code into Local Storage! Look for a key that rhymes with 'gloom' – the value of that key is your code!",
        "secretCode": "🌊"
    }
