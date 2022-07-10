from random import sample

answer = sample(range(1, 10), 3)
attempt = 0

while attempt < 9:
  ball = 0
  strike = 0
  numbers = input("0에서 9까지 중복되지 않은 숫자 3개를 입력하세요: ").split()
  if len(numbers) != 3:
    print("숫자 3개를 입력하세요.")
    continue
  if not all(n.isdigit() and (int(n) in range(10)) for n in numbers):
    print("0에서 9까지의 숫자만 입력하세요.")
    continue
  if len(set(numbers)) != 3:
    print("숫자는 중복되지 않아야 합니다.")
    continue

  numbers = [int(n) for n in numbers]

  for i in range(3):
    if numbers[i] == answer[i]:
      strike += 1
    elif numbers[i] in answer:
      ball += 1
  
  attempt += 1
  print(f"{strike}S {ball}B")
  if strike == 3:
    print(f"축하합니다. {attempt}이닝 만에 숫자를 맞추었습니다.")
    break

print("게임 오버")