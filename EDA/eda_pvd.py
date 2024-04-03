import pandas as pd
import numpy as np
import seaborn as sns
import plotly.express as plt

df = pd.read_csv('pvd-data.csv')
df.head()

import plotly.express as px

df['businessDayTimestampLocal'] = pd.to_datetime(df['businessDayTimestampLocal'])

daily_data = df.resample('D', on='businessDayTimestampLocal').agg({
    'ticket_net_sales': 'sum',
    'tip_pct': 'median'
}).reset_index()

# plot Daily Total Net Sales
fig1 = px.line(daily_data, x='businessDayTimestampLocal', y='ticket_net_sales', title='Daily Total Net Sales')
fig1.show()

# plot Daily Tip Percent Median
fig2 = px.line(daily_data, x='businessDayTimestampLocal', y='tip_pct', title='Daily Tip Percent Median')
fig2.show()

df['businessDayTimestampLocal'] = pd.to_datetime(df['businessDayTimestampLocal'])

daily_data = df.resample('D', on='businessDayTimestampLocal').agg({
    'ticket_net_sales': 'sum',
    'tip_pct': 'mean'  # Changed from 'median' to 'mean'
}).reset_index()

# plot Daily Tip Percent Mean
fig2 = px.line(daily_data, x='businessDayTimestampLocal', y='tip_pct', title='Daily Tip Percent Mean')
fig2.show()