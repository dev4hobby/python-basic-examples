import csv
import pandas as pd
from datetime import datetime
from collections import defaultdict

data = pd.read_csv("./data_.csv", encoding="cp949")

sex_dict = defaultdict(int)
move_dict = defaultdict(int)
snack_dict = defaultdict(int)
for sex in data["성별"]:
    sex_dict[sex] += 1

print(f"남자: {sex_dict['남자']}")
print(f"여자: {sex_dict['여자']}")

for info in data["등교에 걸리는 시간"]:
    move_dict[info] += 1

max_time_info = ""
max_value = -1
for key, value in move_dict.items():
    if value > max_value:
        max_time_info = key

print(f"가장 많이 투표한 등교시간: {max_time_info}")

for info in data["가장 좋아하는 과자는?"]:
    snack_dict[info] += 1
max_snack_info = ""
max_value = -1
for key, value in snack_dict.items():
    if value > max_value:
        max_snack_info = key

print(f"가장 좋아하는 과자: {max_snack_info}")
