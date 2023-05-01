import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.write("""  PREF SITE """)


ticker = 'tsla'

data = yf.Ticker(ticker)
tickerDf = data.history(period= '1d', start='2022-05-01', end='2023-05-01')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)                      
