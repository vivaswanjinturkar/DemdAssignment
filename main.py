import uvicorn
from fastapi import FastAPI, Request, File, UploadFile
import pickle
import scipy
import numpy as np
import pandas as pd

pkl_import=open('classifier.pkl','rb')
classifier=pickle.load(pkl_import)
from pydantic import BaseModel
app=FastAPI()
class request_body(BaseModel):
     campaign: int
     previous: int
     emp_var_rate: int

@app.post('/predict')
async def predict(data : request_body):

     test=[[data.campaign,data.previous,data.emp_var_rate]]
     classes=int(classifier.predict(test))
     return classes

if __name__ == "__main__":
     uvicorn.run(app)
