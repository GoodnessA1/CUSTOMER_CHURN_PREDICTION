from flask import Flask, render_template
from keras._tf_keras.keras.models import load_model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if '__main__' == __name__:
    app.run(host='0.0.0.0', debug=True, port=8080)


'''
Gender: Male, Female
SeniorCitizen: 0, 1
Partner: Yes, No
Dependents: Yes, No
Tenure: integer
PhoneService, Yes, No
MultipleLines: Yes, No
InternetService: DSL, Fiber optic, No
OnlineSecurity: Yes, No
OnlineBackup: Yes, No
DeviceProtection: Yes, No
TechSupport: Yes, No
StreamingTV: Yes, No
StreamingMovies: Yes, No
Contract: Monthly, One year, Two year
PaperlessBilling: Yes, NO	
PaymentMethod: Manual, Bank transfer(automatic), Credit card (automatic)
MonthlyCharges: float
'''