import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error, r2_score 

import pandas as pd  
  
# Load the dataset  
housing_df = pd.read_csv('C:\\Users\\ADMIN\\Desktop\\VS code programs\\Housing.csv', encoding='ascii')  
# One-hot encode categorical variables  
df_encoded = pd.get_dummies(housing_df, drop_first=True)  
y = df_encoded['price']  
X = df_encoded.drop('price', axis=1)  

#Split data into train and test set
  
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   
# Model training
lr = LinearRegression()  
lr.fit(X_train, y_train)   

  
y_pred = lr.predict(X_test)  
mse = mean_squared_error(y_test, y_pred)  
r2 = r2_score(y_test, y_pred)  
  
print("\nModel Performance:")  
print("Mean Squared Error:", mse)  
print("R^2 Score:", r2)  
print("Root Mean Squared Error:", np.sqrt(mse))  
def predict_house_price(area, bedrooms, bathrooms, stories, parking,   
                       mainroad='yes', guestroom='no', basement='no',   
                       hotwaterheating='no', airconditioning='no',   
                       prefarea='no', furnishingstatus='furnished'):  
    input_data = {  
        'area': area,  
        'bedrooms': bedrooms,  
        'bathrooms': bathrooms,  
        'stories': stories,  
        'parking': parking,  
        'mainroad': mainroad,  
        'guestroom': guestroom,  
        'basement': basement,  
        'hotwaterheating': hotwaterheating,  
        'airconditioning': airconditioning,  
        'prefarea': prefarea,  
        'furnishingstatus': furnishingstatus  
    }  
    input_df = pd.DataFrame([input_data])  
    input_encoded = pd.get_dummies(input_df, drop_first=True)  
    for col in X.columns:  
        if col not in input_encoded.columns:  
            input_encoded[col] = 0  
    input_encoded = input_encoded[X.columns]  
    predicted_price = lr.predict(input_encoded)[0]  
    return predicted_price  
  
# Example prediction  
example_price = predict_house_price(  
    area=8000,   
    bedrooms=4,   
    bathrooms=3,   
    stories=2,   
    parking=2,  
    mainroad='yes',  
    airconditioning='yes',  
    furnishingstatus='furnished'  
)  
print("\nExample prediction for a house with area=8000, 4 bedrooms, 3 bathrooms, 2 stories, 2 parking, mainroad, airconditioning, furnished:")  
print("Predicted price: $", int(example_price))  

import pickle  
  
# Save the model  
with open('housing_price_model.pkl', 'wb') as f:  
    pickle.dump(lr, f)  
  
# Save the feature columns  
with open('feature_columns.pkl', 'wb') as f:  
    pickle.dump(X.columns.tolist(), f)  
  
print("\nModel and feature columns saved as 'housing_price_model.pkl' and 'feature_columns.pkl'.")  