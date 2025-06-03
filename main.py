from fastapi import FastAPI, Request, Form  
from fastapi.responses import HTMLResponse  
from fastapi.templating import Jinja2Templates  
import pandas as pd  
import pickle  
import numpy as np  
import os  
  
app = FastAPI(title="House Price Prediction Form")  
  
# Set up templates directory  
templates = Jinja2Templates(directory="C:\\Users\\ADMIN\\Desktop\\Templates")  
  
# Load model and feature columns  
with open(os.path.join(BASE_DIR, "C:\\Users\\ADMIN\\Desktop\\VS code programs\\housing_price_model.pkl"), "rb") as f:
    model = pickle.load(f)
with open(os.path.join(BASE_DIR, "C:\\Users\\ADMIN\\Desktop\\VS code programs\\feature_columns.pkl"), "rb") as f:
    model = pickle.load(f)
  
# Home page with form  
@app.get("/", response_class=HTMLResponse)  
async def form_get(request: Request):  
    return templates.TemplateResponse("form.html", {"request": request, "result": None})  
  
# Handle form submission  
@app.post("/", response_class=HTMLResponse)  
async def form_post(  
    request: Request,  
    area: int = Form(...),  
    bedrooms: int = Form(...),  
    bathrooms: int = Form(...),  
    stories: int = Form(...),  
    parking: int = Form(...),  
    mainroad: str = Form(...),  
    guestroom: str = Form(...),  
    basement: str = Form(...),  
    hotwaterheating: str = Form(...),  
    airconditioning: str = Form(...),  
    prefarea: str = Form(...),  
    furnishingstatus: str = Form(...)  
):  
    # Prepare input  
    input_dict = {  
        "area": area,  
        "bedrooms": bedrooms,  
        "bathrooms": bathrooms,  
        "stories": stories,  
        "parking": parking,  
        "mainroad": mainroad,  
        "guestroom": guestroom,  
        "basement": basement,  
        "hotwaterheating": hotwaterheating,  
        "airconditioning": airconditioning,  
        "prefarea": prefarea,  
        "furnishingstatus": furnishingstatus  
    }  
    input_df = pd.DataFrame([input_dict])  
    input_encoded = pd.get_dummies(input_df, drop_first=True)  
    for col in feature_columns:  
        if col not in input_encoded.columns:  
            input_encoded[col] = 0  
    input_encoded = input_encoded[feature_columns]  
    predicted_price = model.predict(input_encoded)[0]  
    formatted_price = "${:,.0f}".format(predicted_price)  
    return templates.TemplateResponse("form.html", {"request": request, "result": formatted_price, "input": input_dict})  
   
