from flask import Flask, render_template, request
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('C:\\Users\\ADMIN\\Desktop\\VS code programs\\Task3\\random_forest.pkl', 'rb'))

standard_to = StandardScaler()

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel = 0
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Present_Price = float(request.form['Present_Price'])
        Kms_Driven = int(request.form['Kms_Driven'])
        Kms_Driven2 = np.log(Kms_Driven)
        Owner = int(request.form['Owner'])

        Fuel_Type_Petrol = request.form['Fuel_Type_Petrol']
        if Fuel_Type_Petrol == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif Fuel_Type_Petrol == 'Diesel':
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0  # CNG or unknown

        Year = 2020 - Year

        Seller_Type_Individual = request.form['Seller_Type_Individual']
        Seller_Type_Individual = 1 if Seller_Type_Individual == 'Individual' else 0

        Transmission_Mannual = request.form['Transmission_Mannual']
        Transmission_Mannual = 1 if Transmission_Mannual == 'Mannual' else 0

        prediction = model.predict([[Present_Price, Kms_Driven2, Owner, Year,
                                     Fuel_Type_Diesel, Fuel_Type_Petrol,
                                     Seller_Type_Individual, Transmission_Mannual]])
        output = round(prediction[0], 2)

        if output < 0:
            return render_template('result.html', prediction="Sorry, you cannot sell this car.")
        else:
            return render_template('result.html', prediction=f"{output}")
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)


