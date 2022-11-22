import csv


def create_csv(data):

    header = ['job_id', 'date_built', 'execution_time', 'result', 'cause', 'in_progress']
    with open(r'C:\Users\rabel\Documents\execution_log1.csv', 'a',newline='', encoding='UTF8') as f:
        writer = csv.writer(f)

        writer.writerow(header)
        writer.writerow(data)


def append_to_csv(data):
    with open(r'C:\Users\rabel\Documents\execution_log1.csv', 'a', newline='', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(data)
