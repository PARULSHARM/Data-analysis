import pandas as pd
import datetime
from pandas_datareader import data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
start = datetime.datetime(2010, 1, 1)
end = datetime.datetime(2018, 1, 1)
df = web.DataReader('XOM', 'google', start, end)
print(df.head())
df['Close'].plot()
plt.show()