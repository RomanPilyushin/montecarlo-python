from pandas_datareader import data
import pandas_montecarlo
import yfinance as yf
yf.pdr_override() # <== that's all it takes :-)

df = data.get_data_yahoo("SPY")
df['return'] = df['Adj Close'].pct_change().fillna(0)


mc = df['return'].montecarlo(sims=10, bust=-0.1, goal=1)

mc.plot(title="SPY Returns Monte Carlo Simulations")  # optional: , figsize=(x, y)