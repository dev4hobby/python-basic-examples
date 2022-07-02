import csv
import pandas as pd
from datetime import datetime

data = pd.read_csv("./csv/data.csv")

print(data.iloc[1, 1])
