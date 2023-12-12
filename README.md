# Twilio-CPS-Monitor

# Overview 
Python script designed to evaluate Calls-per-Second (CPS) for Outbound-API calls made via Twilio for a dynamic time range.

### Context
Twilio has a limit on the rate at which you can make outbound calls. API requests for calls that exceed the CPS rate limit will be queued, and executed as capacity is available.  

The data from this script aims to inform of CPS trends over time and subsequent needs, so the [CPS Threshold in the Twilio Console](https://www.twilio.com/console/voice/settings) can be adjusted as needed. 

## Setup Requirements
In order to follow along, you’ll need:

- Twilio Account: find this in the [console here](https://console.twilio.com/?frameUrl=/console) 
- Download and Install Python - https://www.python.org/downloads/

## Instructions to set up and execute the script:

### Step 1
- Download the script file from the repository 
- Copy or move the file to a folder name **CPS_Count** 

### Step 2
- Sign in to your Twilio account and head to the "[Calls](https://console.twilio.com/us1/monitor/logs/calls)" section within "**Monitor**" tab to gather call logs in CSV format for the specific timeframe you want to analyze CPS
  
  <img width="223" alt="image" src="https://code.hq.twilio.com/storage/user/3964/files/c325a63c-8dfa-48fc-80b1-72c6d46967fb">
  
- After downloading the file, rename the CSV file to **call_logs.csv**
- Place the CSV file in the same directory **CPS_Count**

### Steps 3
- Launch the terminal and install the pandas library 
```js
pip install pandas
```
### Step 4
- Navigate to the CPS_Count folder where you have the files 
```js
cd CPS_Count
```
- Execute the Python script within the directory to retrieve the top 10 highest CPS values, accompanied by the timestamps of the call creation 
```js
python3 calculate_cps.py
```

## The output will appear as follows:
![image](https://code.hq.twilio.com/storage/user/3964/files/fb359e32-6679-4e25-b7f7-b2cd0529d25e)

