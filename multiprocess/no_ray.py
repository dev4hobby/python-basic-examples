from datetime import datetime
from random import randint, shuffle

dataset_length = 6

arr = [randint(1, 300) for _ in range(10000000)]
dataset = []
for i in range(dataset_length):
  dataset.append(arr.copy())
  shuffle(dataset[i])


limit = len(arr)
begin = datetime.now()
result = []
print(begin)
for i in range(dataset_length):
  count = 0
  while count < limit:
    temp = sum(dataset[i][count:count+2])/2
    dataset[i].append(temp)
    # print(f"({arr[count]} + {arr[count+1]}) / 2 = {temp}")
    count += 2
  result.append(dataset[i])
  print(f"Epoch {i} Done >> {datetime.now()-begin}")

print(f"Done >> {datetime.now()-begin}")
for i, _ in enumerate(result):
  print(f"{i}: {_[-10:]}")