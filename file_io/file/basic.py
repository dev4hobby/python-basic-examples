# read 'test.txt'
with open("file/test.txt", "r") as f:
    line_1 = f.readline().replace("\n", "")
    line_2 = f.readline().replace("\n", "")
    numbers = f.readlines()

print(f"1번 {line_1}")
print(f"2번 {line_2}")
total = 0
for number in numbers:
    total += int(number)
    print(number.replace("\n", ""))
print(f"합계: {total}")
print(f"평균: {total/len(numbers)}")
