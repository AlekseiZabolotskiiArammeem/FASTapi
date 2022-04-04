
# 1. Library imports

import pandas as pd 
import RFClass
import uvicorn
from fastapi import FastAPI
from RFClass import Predict

# 2. Create app and model objects
#app = FastAPI()
#datasetttt = Predict.read_data()
#model = Predict.predictions()
app = FastAPI()
model = Predict()
datasetttt = model.read_data
# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted flower species with the confidence
@app.post('/predict')
def pred():
    #data = datasetttt
    #prediction = model.predictions
    arrayd = model.save_data
    return {
        'array': arrayd  
    }


# 4. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8002)