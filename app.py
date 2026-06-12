import streamlit as st
import pandas as pd
import pickle
import re

from textblob import TextBlob

# -------------------------------
# Page Configuration
# -------------------------------

st.set_page_config(
    page_title="AI Support Ticket Classifier",
    page_icon="🤖",
    layout="wide"
)

# -------------------------------
# Load Models
# -------------------------------

category_model = pickle.load(
    open("models/category_model.pkl", "rb")
)

#priority_model = pickle.load(
 #   open("models/priority_model.pkl", "rb")
#)
def assign_priority(ticket):

    ticket = ticket.lower()

    high_keywords = [
        "payment", "refund", "deducted",
        "charged", "failed", "crash",
        "server", "locked", "error"
    ]

    medium_keywords = [
        "delay", "tracking",
        "password", "login", "otp"
    ]

    for word in high_keywords:
        if word in ticket:
            return "High"

    for word in medium_keywords:
        if word in ticket:
            return "Medium"

    return "Low"

vectorizer = pickle.load(
    open("models/vectorizer.pkl", "rb")
)

# -------------------------------
# Sidebar
# -------------------------------

with st.sidebar:

    st.title("📌 Project Information")

    st.markdown("""
    ### FUTURE_ML_02

    **Project Name**
    AI Support Ticket Classification System

    **Machine Learning Model**
    Logistic Regression

    **Feature Extraction**
    TF-IDF Vectorization

    **Additional Features**
    - Category Prediction
    - Priority Prediction
    - Sentiment Analysis
    - Automated Response Generation
    """)

    st.success("✅ Models Loaded Successfully")

# -------------------------------
# Header
# -------------------------------

st.markdown("""
# 🤖 AI Support Ticket Classification System

Analyze customer support tickets using Natural Language Processing and Machine Learning.

### Features
✅ Category Prediction  
✅ Priority Prediction  
✅ Sentiment Analysis  
✅ Automated Response Suggestion
""")

st.markdown("---")

# -------------------------------
# Input Ticket
# -------------------------------

ticket = st.text_area(
    "✍️ Enter Customer Support Ticket",
    height=150,
    placeholder="Example: My payment failed and money was deducted from my account."
)

# -------------------------------
# Auto Response Generator
# -------------------------------

def get_response(category):

    responses = {

        "Billing":
        """
        Our billing team will investigate the issue and contact you shortly.
        We apologize for the inconvenience caused.
        """,

        "Technical":
        """
        Our technical team is reviewing the issue.
        A resolution will be provided as soon as possible.
        """,

        "Account":
        """
        Our account support team will assist you regarding your account issue.
        Please wait while we investigate.
        """,

        "Delivery":
        """
        Our delivery team will check the shipment status and update you shortly.
        Thank you for your patience.
        """
    }

    return responses.get(
        category,
        "Support team will contact you shortly."
    )

# -------------------------------
# Prediction
# -------------------------------

if st.button("🚀 Analyze Ticket"):

    if ticket.strip() == "":
        st.error("Please enter a support ticket.")
    else:

        clean_text = re.sub(
            r'[^a-zA-Z ]',
            '',
            ticket.lower()
        )

        vector = vectorizer.transform(
            [clean_text]
        )

        category = category_model.predict(
            vector
        )[0]

        priority = assign_priority(ticket)

        sentiment_score = TextBlob(
            ticket
        ).sentiment.polarity

        if sentiment_score > 0:
            sentiment = "Positive 😊"
        elif sentiment_score < 0:
            sentiment = "Negative 😠"
        else:
            sentiment = "Neutral 😐"

        st.markdown("## Prediction Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.success(
                f"📂 Category\n\n{category}"
            )

        with col2:
            st.warning(
                f"⚡ Priority\n\n{priority}"
            )

        with col3:
            st.info(
                f"😊 Sentiment\n\n{sentiment}"
            )

        st.markdown("---")

        st.subheader("💬 Suggested Response")

        st.write(
            get_response(category)
        )

# -------------------------------
# Dataset Analytics
# -------------------------------

st.markdown("---")
st.subheader("📊 Dataset Analytics")

df = pd.read_csv("support_tickets.csv")

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="📄 Total Tickets",
        value=len(df)
    )

with col2:
    st.metric(
        label="📂 Categories",
        value=df['category'].nunique()
    )

with col3:
    st.metric(
        label="⚡ Priority Levels",
        value=df['priority'].nunique()
    )

st.markdown("")

# Category Distribution
col1, col2 = st.columns([2,1])

with col1:

    st.markdown("### 📈 Category Distribution")

    category_counts = (
        df['category']
        .value_counts()
        .rename_axis('Category')
        .reset_index(name='Count')
        .set_index('Category')
    )

    st.bar_chart(
        category_counts,
        height=250
    )

with col2:

    st.markdown("### 📋 Summary")

    st.dataframe(
    category_counts,
    width="stretch"
)

# -------------------------------
# Dataset Preview
# -------------------------------

st.markdown("### 🗂 Dataset Preview")

st.dataframe(
    df.head(10),
    width="stretch"
)
# -------------------------------
# Footer
# -------------------------------

st.markdown("---")

st.caption(
    "Developed for FUTURE_ML_02 | NLP Based Customer Support Ticket Classification System"
)
