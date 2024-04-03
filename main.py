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

@app.get('/egg3Hunt/{lake}')
def beeAPI(lake: str):
    if lake == 'lake_bee':
        return {"message": "I accidentally sent the bee (API) to the wrong lake, {lake}... It needs to be at lake_goldenEgg. Could you correct the parameter and run the API again?" }
    elif lake == 'lake_goldenEgg':
        return {"message": "🐝: The golden egg will reach you at time 16:24!"}
    else:
        return {"message": "🐝: Umm what are you on? Give me the correct params bruh 😡"}
