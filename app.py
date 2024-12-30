from flask import Flask, render_template, request
from keras._tf_keras.keras.models import load_model
import pandas as pd
import nbimporter
from main import scaler
from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler

#datasets stuffs
dataset = pd.read_csv('TelecomCustomerChurn.csv')
le_g = LabelEncoder()
le_p = LabelEncoder()
le_d = LabelEncoder()
le_P = LabelEncoder()
le_o = LabelEncoder()
le_O = LabelEncoder()
le_D = LabelEncoder()
le_T = LabelEncoder()
le_s = LabelEncoder()
le_S = LabelEncoder()
le_paper = LabelEncoder()
le_payment = LabelEncoder()
le_churn = LabelEncoder()
le_m = LabelEncoder()
le_i = LabelEncoder()
le_contract = LabelEncoder()

dataset['Contract'] = le_contract.fit_transform(dataset['Contract'])
dataset['PaymentMethod'] = le_payment.fit_transform(dataset['PaymentMethod'])

dataset['MultipleLines'] = le_m.fit_transform(dataset['MultipleLines'])
dataset['InternetService'] = le_i.fit_transform(dataset['InternetService'])
dataset['Gender'] = le_g.fit_transform(dataset['Gender'])
dataset['Partner'] = le_p.fit_transform(dataset['Partner'])
dataset['Dependents'] = le_d.fit_transform(dataset['Dependents'])
dataset['PhoneService'] = le_P.fit_transform(dataset['PhoneService'])
dataset['OnlineBackup'] = le_o.fit_transform(dataset['OnlineBackup'])
dataset['OnlineSecurity'] = le_O.fit_transform(dataset['OnlineSecurity'])
dataset['DeviceProtection'] = le_D.fit_transform(dataset['DeviceProtection'])
dataset['TechSupport'] = le_T.fit_transform(dataset['TechSupport'])
dataset['StreamingTV'] = le_s.fit_transform(dataset['StreamingTV'])
dataset['StreamingMovies'] = le_S.fit_transform(dataset['StreamingMovies'])
dataset['PaperlessBilling'] = le_paper.fit_transform(dataset['PaperlessBilling'])
dataset['Churn'] = le_churn.fit_transform(dataset['Churn'])


#model wahala
model = load_model('model.keras')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
    # Retrieve individual form values
        gender = le_g.transform(request.form.get("gender"))
        senior_citizen = request.form.get("seniorCitizen")
        partner = le_p.transform(request.form.get("partner"))
        dependents = le_d.transform(request.form.get("dependents"))
        tenure = request.form.get("tenure")
        phone_service = le_P.transform(request.form.get("phoneService"))
        multiple_lines = le_m.transform(request.form.get("multipleLines"))
        internet_service = le_i.transform(request.form.get("internetService"))
        online_security = le_O.transform(request.form.get("onlineSecurity"))
        online_backup = le_o.transform(request.form.get("onlineBackup"))
        device_protection = le_D.transform(request.form.get("deviceProtection"))
        tech_support = le_T.transform(request.form.get("techSupport"))
        streaming_tv = le_s.transform(request.form.get("streamingTV"))
        streaming_movies = le_S.transform(request.form.get("streamingMovies"))
        contract = le_contract.transform(request.form.get("contract"))
        paperless_billing = le_paper.transform(request.form.get("paperlessBilling"))
        payment_method = le_payment.transform(request.form.get("paymentMethod"))
        monthly_charges = request.form.get("monthlyCharges")
        prediction = model.predict(scaler[gender, senior_citizen, partner, dependents, tenure, phone_service, multiple_lines,
                                          internet_service, online_security, online_backup, device_protection, tech_support,
                                          streaming_tv, streaming_movies, contract, paperless_billing, payment_method,
                                          monthly_charges])
        print(prediction)

        return ('''<p>This is the predicton {{prediction}}</p>''')

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