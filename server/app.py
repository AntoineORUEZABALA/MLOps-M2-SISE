import numpy as np
import pickle
from fastapi import FastAPI
from pymongo import MongoClient
from fastapi import FastAPI
from pydantic import BaseModel
from bson import ObjectId
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

# Charger le jeu de données Iris
data = load_iris()
X, y = data.data, data.target

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Entraîner un modèle de classification
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Sauvegarder le modèle dans un fichier .pkl
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

app = FastAPI()
client = MongoClient('mongo', 27017)
db = client.test_database
collection = db.test_collection

# Charger le modèle sauvegardé
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Définir le format des données d'entrée
class PredictRequest(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.get("/")
async def root():
    return {"message": "Vive la Kcorp !"}

@app.get("/liste")
async def list_iris():
    documents = list(collection.find({}, {"_id": False})) 
    return {"predis": documents}

@app.delete("/vider_liste")
async def vider_liste():
    result = collection.delete_many({})  
    return {"message": f"La collection a été vidée. {result.deleted_count} documents supprimés."}

@app.post("/add_fleur")
async def add_fleur(request: PredictRequest):
    features = np.array([[request.sepal_length, request.sepal_width, request.petal_length, request.petal_width]])
    prediction = model.predict(features)[0]

    document = {
        "sepal_length": request.sepal_length,
        "sepal_width": request.sepal_width,
        "petal_length": request.petal_length,
        "petal_width": request.petal_width,
        "prediction": int(prediction)
    }
    insert_result = collection.insert_one(document)
    
    document["_id"] = str(insert_result.inserted_id)  
    return {"message": "Fleur ajoutée avec succès !", "data": document}

@app.post("/predict")
def predict(request: PredictRequest):
    features = np.array([[request.sepal_length, request.sepal_width, request.petal_length, request.petal_width]])
    prediction = model.predict(features)
    return {"predicted_class": int(prediction[0])}