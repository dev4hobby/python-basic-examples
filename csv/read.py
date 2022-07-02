import csv
from datetime import datetime

with open("data.csv", "r") as f:
    reader = csv.reader(f)
    filtered_data = [
        row
        for row in reader
        if datetime.strptime(row[0], "%Y-%m-%d") > datetime(2018, 12, 31)
        and datetime.strptime(row[0], "%Y-%m-%d") < datetime(2022, 1, 1)
    ]


for row in filtered_data:
    print(row)
