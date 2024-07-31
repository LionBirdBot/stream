import streamlit as st
import time
import random


# Function to simulate predictions and their accuracies
def get_predictions():
    stocks = ["Apple", "Amazon", "Nvidia", "Meta", "Netflix"]
    predictions = {}
    for stock in stocks:
        predictions[stock] = {
            "Buy": {"prediction": "Buy", "accuracy": random.randint(70, 100)},
            "Hold": {"prediction": "Hold", "accuracy": random.randint(70, 100)},
            "Sell": {"prediction": "Sell", "accuracy": random.randint(70, 100)}
        }
    return predictions


# Function to get background color based on prediction
def get_bg_color(prediction):
    if prediction == "Buy":
        return "green"
    elif prediction == "Hold":
        return "blue"
    elif prediction == "Sell":
        return "red"


st.set_page_config(layout="wide")
st.title("Trading App")

# Sidebar configuration
st.sidebar.header("Navigation")
pages = ["Home", "About", "Statistics"]
model_options = ["AUTOREG", "LSTM", "RANDOM FOREST"]

# Sidebar page selection
st.sidebar.header("PAGES")
select_page = st.sidebar.selectbox("Select page", pages)

# Sidebar model selection
st.sidebar.header("MODELS")
select_model = st.sidebar.selectbox("Select model", model_options)

# Page content
if select_page == "Home":
    st.title("Home")
    st.markdown("""
    We provide quick predictions for your favorite stocks. These predictions are updated every minute.
    """)

    predictions = get_predictions()

    for stock, prediction_data in predictions.items():
        st.markdown(f"<h3>{stock}</h3>", unsafe_allow_html=True)
        for prediction, data in prediction_data.items():
            color = get_bg_color(data["prediction"])
            accuracy = data["accuracy"]
            st.markdown(f"""
            <div style="margin-bottom: 10px;">
                <div style="background-color: {color}; padding: 5px; border-radius: 5px; width: 100px; text-align: center; display: inline-block; margin-right: 10px;">
                    <p style="color: white; margin: 0; font-size: 14px;">{data["prediction"]}</p>
                </div>
                <span style="font-size: 14px;">Accuracy: {accuracy}%</span>
            </div>
            """, unsafe_allow_html=True)

    # Refresh the page every minute
    time.sleep(60)
    st.experimental_rerun()

elif select_page == "About":
    st.title("About")
    if select_model == "AUTOREG":
        st.markdown("""
        ### About AUTOREG
        Autoregression (AR) is a representation of a type of random process; as such, it is used to describe certain time-varying processes in nature, economics, etc.
        """)
    elif select_model == "LSTM":
        st.markdown("""
        ### About LSTM
        Long Short-Term Memory (LSTM) is an artificial recurrent neural network (RNN) architecture used in the field of deep learning. Unlike standard feedforward neural networks, LSTM has feedback connections.
        """)
    elif select_model == "RANDOM FOREST":
        st.markdown("""
        ### About RANDOM FOREST
        Random Forest is a versatile machine learning method capable of performing both regression and classification tasks, as well as handling missing values and other complexities.
        """)

elif select_page == "Statistics":
    st.title("Statistics")
    st.markdown("""
    ### Model Comparisons
    Here we will display the comparisons of the selected models based on their performance metrics.
    """)

    # Sample comparison data
    st.markdown("""
    | Stock          | Model         | Accuracy | Precision | Recall | F1 Score |
    |----------------|---------------|----------|-----------|--------|----------|
    | Apple          | AUTOREG       | 85%      | 0.80      | 0.85   | 0.82     |
    | Apple          | LSTM          | 90%      | 0.88      | 0.90   | 0.89     |
    | Apple          | RANDOM FOREST | 88%      | 0.86      | 0.88   | 0.87     |
    | Amazon         | AUTOREG       | 80%      | 0.78      | 0.80   | 0.79     |
    | Amazon         | LSTM          | 85%      | 0.84      | 0.85   | 0.84     |
    | Amazon         | RANDOM FOREST | 89%      | 0.88      | 0.89   | 0.88     |
    | Nvidia         | AUTOREG       | 82%      | 0.80      | 0.82   | 0.81     |
    | Nvidia         | LSTM          | 88%      | 0.87      | 0.88   | 0.87     |
    | Nvidia         | RANDOM FOREST | 87%      | 0.85      | 0.87   | 0.86     |
    | Meta           | AUTOREG       | 78%      | 0.75      | 0.78   | 0.76     |
    | Meta           | LSTM          | 84%      | 0.83      | 0.84   | 0.83     |
    | Meta           | RANDOM FOREST | 86%      | 0.85      | 0.86   | 0.85     |
    | Netflix        | AUTOREG       | 81%      | 0.80      | 0.81   | 0.80     |
    | Netflix        | LSTM          | 86%      | 0.85      | 0.86   | 0.85     |
    | Netflix        | RANDOM FOREST | 90%      | 0.88      | 0.90   | 0.89     |
    """)

    st.markdown(f"""
    ### Details for {select_model}
    Here are some specific statistics and differentiation variables for the selected model.
    """)
    if select_model == "AUTOREG":
        st.markdown("""
        - **Parameter 1**: Value
        - **Parameter 2**: Value
        - **Differentiation Variable**: Explanation
        """)
    elif select_model == "LSTM":
        st.markdown("""
        - **Parameter 1**: Value
        - **Parameter 2**: Value
        - **Differentiation Variable**: Explanation
        """)
    elif select_model == "RANDOM FOREST":
        st.markdown("""
        - **Parameter 1**: Value
        - **Parameter 2**: Value
        - **Differentiation Variable**: Explanation
        """)
