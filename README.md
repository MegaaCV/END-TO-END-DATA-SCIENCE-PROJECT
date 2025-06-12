# END-TO-END-DATA-SCIENCE-PROJECT
*COMPANY NAME* : CODETECH IT SOLUTIONS

*NAME*         : MEGAA C V

*INTERN ID*    : CT06DN683

*DOMAIN*       : DATA SCIENCE

*DURATION*     : 6 WEEKS

*MENTOR*       : NEELA SANTHOSH

# Description of my task

Car Selling Price Prediction

This is a Flask-based web application that predicts the resale price of a used car based on various inputs such as purchase year, kilometers driven, fuel type, transmission, and more. The prediction is powered by a Random Forest Regression model trained on historical car data.

🔍 Features

Simple and attractive user interface

Predicts car resale value in lakhs of rupees

Handles categorical inputs like fuel type and transmission

Uses machine learning (Random Forest) model

Built with Python, Flask, HTML/CSS

🛠️ Tech Stack

Frontend: HTML5, CSS3 (with Google Fonts and responsive design)

Backend: Flask (Python)

Machine Learning: Scikit-learn (RandomForestRegressor)

Model Serialization: Pickle

🚀 How to Run the Project Locally
1. Clone the Repository

git clone https://github.com/MegaaCV/END-TO-END-DATA-SCIENCE-PROJECT.git

cd END-TO-END-DATA-SCIENCE-PROJECT
3. Create a Virtual Environment 
python -m venv venv
venv\Scripts\activate  # On Windows

4. Install Required Packages
pip install -r requirements.txt

5. Place Your Model
Ensure you have the trained model file random_forest.pkl in your project directory (or update the path in app.py accordingly).

6. Run the App
python app.py

Visit http://127.0.0.1:5000 in your browser.

🧪 Example Inputs
Year: 2015

Present Price: 5.6 (Lakhs)

Kms Driven: 35000

Owner: 0

Fuel Type: Petrol

Seller Type: Individual

Transmission: Manual

📌 Future Improvements


Add support for more car features (engine size, power, etc.)

Upload dataset and re-train model from the app

Deploy on cloud (e.g., Heroku, AWS, or Vercel)

**Deployed Model in Vercel Cloud**

https://end-to-end-data-science-project-git-main-megaa-c-vs-projects.vercel.app

Add logging and form validation

🙌 Acknowledgments

Dataset: https://www.kaggle.com/datasets/mbsoroush/cara-price-dataset

