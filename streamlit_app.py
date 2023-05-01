import yfinance as yf
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

st.write("""  PREF SITE """)


def get_stock_returns(tickers, start_date, end_date, interval):
    data = yf.download(tickers, start=start_date, end=end_date, interval=interval)['Adj Close']
    returns = data.pct_change().dropna()
    return returns

def plot_returns(returns, title):
    corr_matrix = returns.corr()
    
    plt.figure(figsize=(24, 12))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, linewidths=0.5)
    plt.title(title)
    plt.xlabel('Tickers')
    plt.ylabel('Tickers')
    plt.show()

tickers = [ 'PFF', 'TLT', 'MS-PA', 'MS-PE', 'MS-PF', 'MS-PI', 'MS-PK', 'MS-PL', 'MS-PO', 'MS-PP']

start_date = '2022-05-01'
end_date = '2023-05-01'
interval = '1d'  # Use '1d' for daily or '1wk' for weekly

returns = get_stock_returns(tickers, start_date, end_date, interval)
plot_returns(returns, f'Stock Returns Correlation ({start_date} to {end_date})')
