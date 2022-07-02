def even_odd_sort(ary):
    n = len(ary)
    # odd first even last
    for end in range(n - 1, 0, -1):
        for cur in range(0, end):
            if ary[cur] > ary[cur + 1]:
                ary[cur], ary[cur + 1] = ary[cur + 1], ary[cur]
    return ary


dataAry = [3, 2, 1, 4, 6, 8, 7, 5, 3, 4, 5]
print("정렬 전-->", dataAry)
dataAry = even_odd_sort(dataAry)
print("정렬 후-->", dataAry)
