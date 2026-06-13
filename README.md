# AI Support Ticket Classification System

## Project Overview

This project was developed as part of the Future Interns Machine Learning Internship.

The AI Support Ticket Classification System uses Natural Language Processing (NLP) and Machine Learning techniques to automatically analyze customer support tickets and predict:

- Ticket Category
- Ticket Priority
- Customer Sentiment
- Automated Response Suggestions

The application is built using Streamlit and provides an interactive interface for support ticket analysis.

---

## Features

- Automatic Ticket Category Classification
- Ticket Priority Prediction
- Customer Sentiment Analysis
- Automated Response Generation
- Interactive Streamlit Dashboard
- Dataset Analytics and Visualization

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- TextBlob
- Streamlit
- Matplotlib

---

## Dataset

The project uses a customer support ticket dataset containing 8469 support tickets.

The dataset includes:

- Ticket Description
- Ticket Type
- Ticket Priority
- Customer Information
- Resolution Details
- Customer Satisfaction Rating

---

## Project Structure

```text
FUTURE_ML_02/
│
├── app.py
├── support_tickets.csv
├── requirements.txt
├── README.md
├── Task_2_of_Future_Interns.ipynb
│
├── models/
│   ├── category_model.pkl
│   └── vectorizer.pkl
│
└── screenshots/
    ├── home.png
    ├── prediction.png
    └── analytics.png
```

## Installation

Clone the repository:

```bash
git clone https://github.com/shaikkarishma23175-svg/FUTURE_ML_02.git
```

Move into the project directory:

```bash
cd FUTURE_ML_02
```

Install required packages:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Screenshots

### Home Page

![Home Page](screenshots/home.png)

### Prediction Results

![Prediction Results](screenshots/prediction.png)

### Dataset Analytics

![Analytics Dashboard](screenshots/analytics.png)

---

## Results

The system successfully classifies support tickets using machine learning and NLP techniques.

It provides:

- Ticket Category Prediction
- Ticket Priority Prediction
- Sentiment Analysis
- Automated Response Suggestions

through an easy-to-use Streamlit web interface.

---

## Author

Karishma Shaik

---

## Internship Details

Future Interns – Machine Learning Internship

Task 2: AI Support Ticket Classification System
