import streamlit as st
import time
import random
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from AutoregModel import fetch_stocks, fetch_periods_intervals, fetch_stock_info, fetch_stock_history, \
    generate_stock_prediction, get_predictions, plot_stock_data, get_bg_color

# Set page configuration
st.set_page_config(layout="wide")

# App title
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
                <span style="font-size: 16px;">{stock}</span>
                <div style="background-color: {color}; padding: 5px; border-radius: 5px; width: 80px; text-align: center; display: inline-block; margin-right: 10px;">
                    <p style="color: white; margin: 0; font-size: 12px;">{data["prediction"]}</p>
                </div>
                <span style="font-size: 12px;">Accuracy: {accuracy}%</span>
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

        # Integrate stock prediction functionality
        st.write("Welcome to the Stock Prediction App. Please select a stock to view its information and predictions.")

        # Fetch the stocks
        stock_dict = fetch_stocks()

        # Fetch the periods and intervals
        periods_intervals = fetch_periods_intervals()

        # Create sidebar options for stock selection
        stock_ticker = st.sidebar.selectbox("Select a stock", list(stock_dict.keys()))
        period = st.sidebar.selectbox("Select period", list(periods_intervals.keys()))
        interval = st.sidebar.selectbox("Select interval", periods_intervals[period])

        # Fetch stock info and display
        st.header(f"Stock Information for {stock_ticker}")
        stock_info = fetch_stock_info(stock_ticker)
        for section, info in stock_info.items():
            st.subheader(section)
            for key, value in info.items():
                st.write(f"**{key}**: {value}")

        # Fetch stock history and display
        st.header(f"Stock History for {stock_ticker}")
        stock_history = fetch_stock_history(stock_ticker, period, interval)
        st.write(stock_history.tail())

        # Generate stock prediction and display
        st.header(f"Stock Prediction for {stock_ticker}")
        train_df, test_df, forecast, predictions = generate_stock_prediction(stock_ticker)
        if train_df is not None:
            st.write("Train Data")
            st.line_chart(train_df)
            st.write("Test Data")
            st.line_chart(test_df)
            st.write("Forecast")
            st.line_chart(forecast)
            st.write("Predictions")
            st.line_chart(predictions)

        # Display stock chart
        st.header(f"{stock_ticker} Stock Chart")
        plot_stock_data(stock_ticker)

        # Display a tip based on the model's prediction
        st.header(f"Trading Tip for {stock_ticker}")
        tip = predictions[-1]  # Assuming the last prediction is the latest
        st.markdown(f"### Tip: {tip['prediction']}")
        st.markdown(f"**Model Accuracy**: {tip['accuracy']}%")

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

    # Example plot
    stock = yf.Ticker('AAPL')
    st.write(f"Showing data for {stock.ticker}")
    plot_stock_data(stock, title=f"{stock.ticker} Stock Price Over Time")
