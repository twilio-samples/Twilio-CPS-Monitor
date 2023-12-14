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
  
  ![c325a63c-8dfa-48fc-80b1-72c6d46967fb](https://github.com/twilio-samples/Twilio-CPS-Monitor/assets/136878371/aac47d4e-4a06-4053-8e9f-4302d02af8df)
  
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
- Execute the Python script within the directory  
```js
python3 calculate_cps.py
```

### Output
- The output will consist of highest CPS values, accompanied by the timestamps of the call creation and will appear as follows:
  
  <img width="450" alt="Screenshot 2023-12-14 at 4 33 26 PM" src="https://github.com/twilio-samples/Twilio-CPS-Monitor/assets/136878371/d8f90651-cd20-4762-a287-3fcd7c140a40">
