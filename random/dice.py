# random 모듈 사용
from random import randint

if __name__ == "__main__":
  # 입력 - input()
  count = int(input("주사위를 몇번 던질까요 => "))  

  # 리스트 사용
  dice_log = list()

  # 반복문: for in range
  for i in range(count):
    dice_log.append(randint(1, 6))

  # 출력 - print()
  print(f"{count} 번 던진 주사위 수 => {dice_log}")
  
  # 내장함수 써서 끝내도 되지만..
  # print(f"6이 나온 횟수 => {dice_log.count(6)}")

  # 세부 평가항목 참조하여 작성
  count_6 = 0
  for number in dice_log:
    # 연산자 사용, if문 사용
    if number == 6:
      count_6 += 1
  print(f"6이 나온 횟수 => {count_6}")
