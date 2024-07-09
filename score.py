import json
import joblib
import numpy as np
from azureml.core.model import Model

# Called when the service is loaded
def init():
    global model
    # Load the model from the model registry
    model_path = Model.get_model_path(model_name='sklearn-stroke')
    model = joblib.load(model_path)

# Called when a request is received
def run(data):
    try:
        # Parse the input data
        data = json.loads(data)
        input_data = np.array(data['data'])
        
        # Perform prediction
        predictions = model.predict(input_data)
        
        # Return the predictions as JSON
        return json.dumps({"predictions": predictions.tolist()})
    except Exception as e:
        error = str(e)
        return json.dumps({"error": error})

