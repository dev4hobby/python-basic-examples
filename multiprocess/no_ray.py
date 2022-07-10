from datetime import datetime
from random import randint
arr = [randint(1, 300) for _ in range(100000000)]
count = 0

limit = len(arr)
begin = datetime.now()
print(begin)
while count < limit:
  temp = sum(arr[count:count+2])/2
  arr.append(temp)
  # print(f"({arr[count]} + {arr[count+1]}) / 2 = {temp}")
  count += 2

print(f"Done >> {datetime.now()-begin}")
print(f"...{arr[-10:]}")