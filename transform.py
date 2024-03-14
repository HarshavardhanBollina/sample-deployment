import pandas as pd

df = pd.read_csv("streaming_data.csv")

df['time'] = pd.to_datetime(df['timestamp']).dt.time
df['day'] = pd.to_datetime(df['timestamp']).dt.day_name()

df = df.drop('timestamp', axis=1)
# Ensure these headers match your CSV file exactly
df.columns = ['City', 'Temperature', 'Day', 'Time'] 

df.to_csv('processed_data.csv', index=False)
