#!/usr/bin/env python

import requests
from os.path import exists
#from Plot_Data import plot_data, save_to_pdf
import jenkins
from Create_csv_file import create_csv, append_to_csv
from datetime import datetime

#get latest build number

j = jenkins.Jenkins('http://localhost:8080/', username='admin', password='6e20684db6224d459ad9837901a1e8cd')
latest_build = j.get_job_info('python')['lastCompletedBuild']['number']

time_stamp = j.get_build_info('python', latest_build, depth=0)['timestamp']/1000
date_time = datetime.fromtimestamp(time_stamp)
print(latest_build, str(date_time)[:10])

##get the runtime of a certain job

response_API = requests.get('http://localhost:8080/job/python/{}/timestamps/?elapsed='
                            'HH:mm:ss.S&appendLog'.format(latest_build),
                            auth=('admin', '6e20684db6224d459ad9837901a1e8cd'))
content = response_API.content

#convert from bytes to string

output = str(content, 'UTF-8')
run_time = output[len(output)-33:len(output)-20]
print(run_time)

#check if text file is present

path = r'C:\Users\rabel\Documents'

file_exists = exists(path+'\execution_log1.csv')
print(file_exists)

# create csv file
if file_exists:
    append_to_csv([latest_build, str(date_time)[:10], run_time])
else:
    create_csv([latest_build, str(date_time)[:10], run_time,])


''''
## create plot and save to archives

graph = plot_data(path + '\job_execution_log.txt')
save_to_pdf('test132.pdf', graph)

#send pdf to Teams or ms access'''

