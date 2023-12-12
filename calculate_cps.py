import pandas as pd
from datetime import datetime, timedelta

# Load the CSV file into a DataFrame
df = pd.read_csv('call_logs.csv')

# Convert the 'date created' column into a standardized datetime format
df['Date Created'] = pd.to_datetime(df['Date Created'])

# Filter data for calls with direction equal to 'outbound API'
df = df[df['Direction'] == 'Outgoing API']

# Count calls for each second
cps_per_second = df.resample('S', on='Date Created').size()

top_10_cps_values = cps_per_second.nlargest(10)

print("Top 10 CPS values:")
print('\n'.join(top_10_cps_values.to_string(index=True, header=False).splitlines()[:-1]))


