import ray
from datetime import datetime
from random import randint, shuffle
from collections import defaultdict

cores = 6
dataset_length = 6

arr = [randint(1, 300) for _ in range(10000000)]
dataset = []
for i in range(dataset_length):
  dataset.append(arr.copy())
  shuffle(dataset[i])

ray.init(num_cpus=cores)

begin = datetime.now()
print(begin)

@ray.remote
def func(arr):
  count = 0
  limit = len(arr)
  while count < limit:
    temp = sum(arr[count:count+2])/2
    arr.append(temp)
    count += 2
  print(f"Sub Process Done >> {datetime.now()-begin}")
  return arr

epoch = 0
result = []

process_return = defaultdict()

for i in range(dataset_length):
  process_return[i] = func.remote(dataset[i])

result = ray.get([value for value in process_return.values()])
result = [_[-10:] for _ in result]
for i, _ in enumerate(result):
  print(f"{i}: {_}")


