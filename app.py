# This is the app.py file created using FastApi!!

# Run this file using uvicorn app:app --reload


from fastapi import FastAPI, File, UploadFile
import uvicorn
import pandas as pd
import pickle

app = FastAPI()

PATH = 'classifier.pkl'

with open(PATH, 'rb') as file:
    classifier = pickle.load(file)


@app.post("/predict/{variance,skewness,curtosis,entropy}")
def predict(variance: float, skewness: float, curtosis: float, entropy: float):
    labels = [variance, skewness, curtosis, entropy]
    features = [[variance, skewness, curtosis, entropy]]
    to_predict = pd.DataFrame(features, columns=labels)
    prediction = classifier.predict(to_predict)
    return {"predicted value:": int(prediction)}


@app.post("/predict_file")
async def predict_file(file: UploadFile = File(...)):
    dataframe = pd.read_csv(file.file)
    prediction = classifier.predict(dataframe)
    print(prediction)
    return {"prediction": str(prediction)}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)
