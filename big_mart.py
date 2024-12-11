# import streamlit as st
# import numpy as np
# import pandas as pd
# import joblib

# # Load the trained model
# model = joblib.load('bigmart_model')

# # Title of the app
# st.title("Big Mart Sales Prediction")
# st.write("### Predict the sales of products across different outlets.")

# # Create input fields for user input
# st.sidebar.header("Input Features")

# Item_Weight = st.sidebar.number_input("Item Weight", min_value=0.0, max_value=50.0, step=0.1, value=10.0)
# Item_Fat_Content = st.sidebar.selectbox("Item Fat Content", ["Low Fat", "Regular"])
# Item_Visibility = st.sidebar.slider("Item Visibility", min_value=0.0, max_value=0.5, step=0.01, value=0.05)
# Item_Type = st.sidebar.selectbox("Item Type", ["Dairy", "Soft Drinks", "Meat", "Fruits and Vegetables", "Household", "Others"])
# Item_MRP = st.sidebar.number_input("Item MRP", min_value=0.0, max_value=500.0, step=0.1, value=100.0)
# Outlet_Identifier = st.sidebar.selectbox("Outlet Identifier", ["OUT049", "OUT018", "OUT010", "OUT013", "OUT027"])
# Outlet_Establishment_Year = st.sidebar.number_input("Outlet Establishment Year", min_value=1985, max_value=2020, step=1, value=2000)
# Outlet_Size = st.sidebar.selectbox("Outlet Size", ["Small", "Medium", "High"])
# Outlet_Location_Type = st.sidebar.selectbox("Outlet Location Type", ["Tier 1", "Tier 2", "Tier 3"])
# Outlet_Type = st.sidebar.selectbox("Outlet Type", ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"])

# # Convert categorical inputs to numerical values (assumes preprocessing is consistent with training)
# def preprocess_input():
#     input_data = {
#         'Item_Weight': Item_Weight,
#         'Item_Fat_Content': 0 if Item_Fat_Content == "Low Fat" else 1,
#         'Item_Visibility': Item_Visibility,
#         'Item_Type': ["Dairy", "Soft Drinks", "Meat", "Fruits and Vegetables", "Household", "Others"].index(Item_Type),
#         'Item_MRP': Item_MRP,
#         'Outlet_Identifier': ["OUT049", "OUT018", "OUT010", "OUT013", "OUT027"].index(Outlet_Identifier),
#         'Outlet_Establishment_Year': Outlet_Establishment_Year,
#         'Outlet_Size': ["Small", "Medium", "High"].index(Outlet_Size),
#         'Outlet_Location_Type': ["Tier 1", "Tier 2", "Tier 3"].index(Outlet_Location_Type),
#         'Outlet_Type': ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"].index(Outlet_Type)
#     }
#     return pd.DataFrame([input_data])

# # Preprocess user input
# input_df = preprocess_input()

# # Predict button
# if st.button("Predict Sales"):
#     prediction = model.predict(input_df)[0]
#     st.success(f"Predicted Sales: ${prediction:.2f}")

















import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('bigmart_model')

# Title of the app
st.title("Big Mart Sales Prediction")
st.write("### Predict the sales of products across different outlets.")

# Sidebar inputs
st.sidebar.header("Input Features")

# Ensure inputs match the model's expected features
Item_Visibility = st.sidebar.slider("Item Visibility", min_value=0.0, max_value=0.5, step=0.01, value=0.05)
Item_MRP = st.sidebar.number_input("Item MRP", min_value=0.0, max_value=500.0, step=0.1, value=100.0)
Outlet_Identifier = st.sidebar.selectbox("Outlet Identifier", ["OUT049", "OUT018", "OUT010", "OUT013", "OUT027"])
Outlet_Size = st.sidebar.selectbox("Outlet Size", ["Small", "Medium", "High"])
Outlet_Type = st.sidebar.selectbox("Outlet Type", ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"])
Outlet_age = st.sidebar.slider("Outlet Age", min_value=0, max_value=40, step=1, value=15)  # Replace Establishment Year with Age

# Preprocess user input (ensure consistency with model training)
def preprocess_input():
    input_data = {
        'Item_Visibility': Item_Visibility,
        'Item_MRP': Item_MRP,
        'Outlet_Identifier': ["OUT049", "OUT018", "OUT010", "OUT013", "OUT027"].index(Outlet_Identifier),
        'Outlet_Size': ["Small", "Medium", "High"].index(Outlet_Size),
        'Outlet_Type': ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"].index(Outlet_Type),
        'Outlet_age': Outlet_age
    }
    return pd.DataFrame([input_data])

# Preprocess input
input_df = preprocess_input()

# Predict button
if st.button("Predict Sales"):
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Sales: ${prediction:.2f}")
