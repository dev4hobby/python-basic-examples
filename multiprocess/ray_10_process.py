import ray
from datetime import datetime
from random import randint, shuffle
arr = [randint(1, 300) for _ in range(100000)]
ray.init(num_cpus=8)

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
while epoch < 10:
  dataset = arr.copy()
  shuffle(dataset)
  result.append(ray.get(func.remote(dataset))[-10:])
  epoch += 1
  print(f"Epoch >> {epoch}")

print(f"Done >> {datetime.now()-begin}")
for i, _ in enumerate(result):
  print(f"{i}: {_}")