from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Load the model
model = pickle.load(open("churn_model.pkl", "rb"))


class CustomerData(BaseModel):
    Pclass: int
    Age: float
    Fare: float


@app.post("/predict")
def predict(customer: CustomerData):
    # Convert input to DataFrame
    df = pd.DataFrame([customer.dict()])
    prediction = model.predict(df)

    return {"prediction": "Will Churn" if int(prediction[0]) == 1 else "Will Stay"}