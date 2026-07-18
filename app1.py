import streamlit as st 
import pandas as pd
import numpy as np
import joblib 


@st.cache_resource
def load_model():
    return joblib.load("models/house_price_model.pkl")

model = load_model()


@st.cache_resource
def load_feature_names():
    return joblib.load("models/feature_names.pkl")

feature_names = load_feature_names()



def yes_no_to_binary(value):
    return 1 if value == "Yes" else 0


def furnishing_to_dummies(status):

    if status == "Semi-Furnished":
        return 1, 0

    elif status == "Unfurnished":
        return 0, 1

    else:      
        return 0, 0
    



st.set_page_config(page_title="House Price Predictor", page_icon=":house:", layout="wide")

st.title("🏡 House Price Prediction")

st.subheader("Enter House Details")

st.write(
    "Fill in the property information below and click **Predict House Price** to estimate its market value."
)

with st.form("house_form"):

    col1, col2 = st.columns(2)

    with col1:
            
            area = st.number_input(
            "Area (sq. ft.)",
            min_value=500,
            max_value=20000,
            value=5000,
            step=100,
            help="Enter the total built-up area of the house in square feet."
            )

            bedrooms = st.selectbox(
                "Number of Bedrooms",
                options=range(1, 7),
                help="Select the total number of bedrooms in the house."
            )

            bathrooms = st.selectbox(
                "Number of Bathrooms",
                options=range(1, 5),
                help="Select the total number of bathrooms available."
            )

            stories = st.selectbox(
                "Number of Stories",
                options=range(1, 5),
                help="Select the number of floors (stories) in the house."
            )

            parking = st.selectbox(
                "Number of Parking Spaces",
                options=range(0, 4),
                help="Select the number of parking spaces available with the property."
            )
    
    with col2:

        mainroad = st.selectbox(
            "Main Road",
            options=["Yes", "No"],
            help="Select whether the house has direct access to a main road."
            )

        guestroom = st.selectbox(
            "Guest Room",
            options=["Yes", "No"],
            help="Select whether the house includes a guest room."
            )

        basement = st.selectbox(
            "Basement",
            options=["Yes", "No"],
            help="Select whether the house has a basement."
            )

        hotwaterheating = st.selectbox(
            "Hot Water Heating",
            options=["Yes", "No"],
            help="Select whether the house has a hot water heating system."
            )

        airconditioning = st.selectbox(
            "Air Conditioning",
            options=["Yes", "No"],
            help="Select whether the house has air conditioning."
            )

        prefarea = st.selectbox(
            "Preferred Area",
            options=["Yes", "No"],
            help="Select whether the house is located in a preferred residential area."
            )
        
    furnishingstatus = st.selectbox(
    "Furnishing Status",
    options=["Furnished", "Semi-Furnished", "Unfurnished"],
    help="Select the furnishing condition of the house."
    )

    
    submit = st.form_submit_button("Predict House Price")


if submit:
    mainroad = yes_no_to_binary(mainroad)
    guestroom = yes_no_to_binary(guestroom)
    basement = yes_no_to_binary(basement)
    hotwaterheating = yes_no_to_binary(hotwaterheating)
    airconditioning = yes_no_to_binary(airconditioning)
    prefarea = yes_no_to_binary(prefarea)

    furnishingstatus_semi_furnished, furnishingstatus_unfurnished = furnishing_to_dummies(furnishingstatus)

    input_df = pd.DataFrame({
        "area": [area],
        "bedrooms": [bedrooms],
        "bathrooms": [bathrooms],
        "stories": [stories],
        "mainroad": [mainroad],
        "guestroom": [guestroom],
        "basement": [basement],
        "hotwaterheating": [hotwaterheating],
        "airconditioning": [airconditioning],
        "parking": [parking],
        "prefarea": [prefarea],
        "furnishingstatus_semi-furnished": [furnishingstatus_semi_furnished],
        "furnishingstatus_unfurnished": [furnishingstatus_unfurnished]
    })
    input_df = input_df[feature_names]

    prediction = model.predict(input_df)

    st.success("Prediction Successful!")

    st.subheader("🏠 Estimated House Price")

    st.metric(
        label="Predicted Price",
        value=f"₹ {prediction[0]:,.0f}"
    )


st.caption(
    "Developed by Darshan Panchal | Python • Scikit-Learn • Streamlit | "
    "Gmail: darshanpanchal151102@gmail.com | "
    "GitHub: https://github.com/DarshaN131521"
)




