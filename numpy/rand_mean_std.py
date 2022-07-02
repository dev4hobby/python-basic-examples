import numpy as np

# 3x3 난수
arr = np.random.rand(3, 3)
print(arr)

# 정규화: 평균
print(np.mean(arr))

# 정규화: 표준 편차
print(np.std(arr))
