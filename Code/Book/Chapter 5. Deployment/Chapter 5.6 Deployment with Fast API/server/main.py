from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model_loader import ModelLoader
from train_parameters import TrainParameters
from penguin_sample import PenguinSample

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000/predict",
    "http://127.0.0.1:8000/load",
    "http://localhost:4200"
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initially load SVM Model.
app.model = ModelLoader('svm')

@app.post("/load")
async def load(params: TrainParameters):
    '''API Route for loading defined model into memory.'''
    print("Model Loading Started")
    app.model =  ModelLoader(params.model.lower())
    return True

@app.post("/predict")
async def predict(data:PenguinSample):
    '''API Route for making predictions based on the entered information.'''
    print("Predicting")
    spicies_map = {0: 'Adelie', 1: 'Chinstrap', 2: 'Gentoo'}
    species = app.model.predict(data)
    return spicies_map[species[0]]