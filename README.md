# Bengaluru HomeValue Predictor

A web application to predict house prices in Bengaluru using scraped real estate data and machine learning models.

## Project Overview
‘Bengaluru HomeValue Predictor’ is a web-based platform that allows users to estimate the price of houses in Bengaluru. The app scrapes property data from [MakaanBhai.com](https://www.makaanbhai.com) and predicts prices using **Linear Regression, Lasso Regression, and Decision Tree** models. The models achieve an overall accuracy of **81%**, providing data-driven insights for buyers, sellers, and real estate enthusiasts.

## Features
- **Web Interface:** User-friendly interface to input property details and get instant price predictions.  
- **Data Scraping:** Collects property details like area, BHK, location, and amenities from MakaanBhai.com.  
- **Multiple ML Models:** Linear Regression, Lasso Regression, and Decision Tree for prediction.  
- **Accuracy:** Achieved 81% prediction accuracy on test data.  
- **Interactive:** Allows users to explore market trends and estimate property prices.  

## Technologies Used
- **Frontend:** HTML, CSS, JavaScript  
- **Backend:** Flask (Python)  
- **Machine Learning:** Scikit-learn (Linear Regression, Lasso, Decision Tree)  
- **Web Scraping:** BeautifulSoup, Requests  
- **Data Handling:** Pandas, NumPy  

## Installation
1. Clone the repository:  
   ```bash
   git clone "https://github.com/Rishi-05/Bengaluru-HomeValue-Predictor"

2. Navigate to the project directory:
   ```bash
   cd bengaluru-homevalue-predictor
   
3. Install dependencies:
   ```bash
   pip install -r requirements.txt

4. Run the Flask app:
   ```bash
   python app.py

5. Open the web app in your browser:
   ```bash
   http://127.0.0.1:5000/
