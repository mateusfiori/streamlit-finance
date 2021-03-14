import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple stock price app

Data presented is from stock closing price and volume of Google

 """)

ticker_symbol = 'GOOGL'

ticker_data = yf.Ticker(ticker_symbol)

ticker_df = ticker_data.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(ticker_df.Close)
st.line_chart(ticker_df.Volume)
