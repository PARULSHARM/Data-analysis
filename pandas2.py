import pandas as pd
import datetime
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
style.use('ggplot')
stats = {
    'Day' : [1,2,3,4],
    'Viewers' : [22,33,44,55],
    'Bounce Rate' : [2,4,5,6]
}
df = pd.DataFrame(stats)
# print(df.head(6))
#seperate data frame.
df.set_index('Day', inplace=True)
print(df.head(4))
print(df['Viewers'])
print(df[['Viewers','Bounce Rate']])
#df to list
print(np.array(df[['Viewers','Bounce Rate']]))
print(df.Viewers.tolist())
df['Viewers'].plot()
df2 = pd.DataFrame(np.array(df[['Viewers','Bounce Rate']]))
print(df2)
plt.show()
