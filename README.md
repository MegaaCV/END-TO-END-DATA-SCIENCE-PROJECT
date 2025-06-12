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
bash
Copy
Edit
git clone https://github.com/MegaaCV/END-TO-END-DATA-SCIENCE-PROJECT.git
cd END-TO-END-DATA-SCIENCE-PROJECT
2. Create a Virtual Environment 
bash
Copy
Edit
python -m venv venv
venv\Scripts\activate  # On Windows
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
4. Place Your Model
Ensure you have the trained model file random_forest.pkl in your project directory (or update the path in app.py accordingly).

5. Run the App
bash
Copy
Edit
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

📁 Project Structure
bash
Copy
Edit
car-price-prediction/
│
├── templates/
│   ├── index.html        # Main input form
│   └── result.html       # Output result page
│
├── random_forest.pkl     # Trained ML model
├── app.py                # Main Flask application
├── requirements.txt      # Dependencies
└── README.md             # Project documentation
📦 Dependencies
txt
Copy
Edit
Flask
numpy
scikit-learn
Generate with:

bash
Copy
Edit
pip freeze > requirements.txt
📌 Future Improvements
Add support for more car features (engine size, power, etc.)

Upload dataset and re-train model from the app

Deploy on cloud (e.g., Heroku, AWS, or Vercel)

Add logging and form validation

🙌 Acknowledgments
Kaggle Used Car Dataset

Scikit-learn documentation

Flask framework
