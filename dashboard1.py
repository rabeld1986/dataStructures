#!/usr/bin/env python

import requests
import json
from Create_csv_file import create_csv, append_to_csv
from os.path import exists
from datetime import datetime

# Your jenkins URL and credentials goes here
path = r'C:\Users\rabel\Documents'
url = 'http://192.168.1.9:8080/job/dashboard_test/api/json'
console_url = 'http://localhost:8080/job/dashboard_test/{}/timestamps/?elapsed=HH:mm:ss.S&appendLog'
username = 'admin'
password = '6e20684db6224d459ad9837901a1e8cd'

progress = {True: 'YES', False: 'NO'}
# Use the 'auth' parameter to send requests with HTTP Basic Auth:
# Accessing the Job page to get the latest Build ran.
response = requests.get(url, auth=(username, password), verify=False)

try:
    buildnumberJson = json.loads(response.text)
except:
    print("Failed to parse json")

if "lastBuild" in buildnumberJson:
    total_builds = buildnumberJson["lastBuild"]
    runs = total_builds["number"]

else:
    print("Failed to get build")

# Iterate over the job build runs to get the build status for each

total_success = total_failure = total_missing = 0

for build in range(1, runs):
    build_url = 'http://192.168.1.9:8080/job/dashboard_test/' + str(build) + '/api/json'

    print(build_url)
    build_status = []

    try:
        response = requests.get(build_url, auth=(username, password), verify=False)
        console_response = requests.get(console_url.format(build), auth=(username, password), verify=False)

        content = console_response.content
        output = str(content, 'UTF-8')
        run_time = output[len(output) - 33:len(output) - 25]

        build_status = json.loads(response.text)
        timestamp = build_status['timestamp']/1000
        build_date = datetime.fromtimestamp(timestamp)
        build_date = str(build_date)[:10]

        build_progress = build_status["inProgress"]
        job_trigger = build_status['actions'][0]['causes'][0]['shortDescription']
        data = [build, build_date, run_time, build_status["result"], job_trigger, progress[build_progress]]

        file_exists = exists(path + '\execution_log1.csv')

        # create csv file
        if file_exists:
            append_to_csv(data)
        else:
            create_csv(data)
    except Exception as e:
        total_missing = total_missing + 1

    if "result" in build_status:
        if build_status["result"] == "SUCCESS":
            total_success = total_success + 1
        if build_status["result"] == "FAILURE":
            total_failure = total_failure + 1

# Generate Output numbers
print("")
print(f"total builds:{runs}")
print(f"total succeeded builds:{total_success}")
print(f"total failed builds:{total_failure}")
print(f"total skipped builds:{total_missing}")
