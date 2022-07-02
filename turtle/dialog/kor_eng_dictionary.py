import turtle

# dictionary 자료형 사용
animal_dic = {
  '호랑이': 'Tiger',
  '사자': 'Lion',
  '코끼리': 'Elephant',
  '토끼': 'Rabbit',
  '거북이': 'Turtle',
}

if __name__ == "__main__":
  # turtle 모듈 사용
  screen = turtle.Screen()
  screen.setup(400, 300)

  # while 반복문
  while True:
    # 입력 - turtle.textinput() 사용
    korean = screen.textinput("동물입력", "호랑이, 사자, 코끼리, 토끼, 거북이 중 하나를 입력하세요: ")
    if korean not in animal_dic:
      continue
    screen.clear()
    # 출력 write()
    screen._write((0, -100), f"{korean} 영어 단어는 ==> {animal_dic[korean]}입니다", "center", "normal", "black")
