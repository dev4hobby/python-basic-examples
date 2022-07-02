import turtle
from random import randint

dice = ["./imagesimages/1.gif", "./images2.gif", "./images3.gif", "./images4.gif", "./images5.gif", "./images6.gif"]

if __name__ == "__main__":
  # turtle 모듈 사용
  screen = turtle.Screen()
  t1 = turtle.Turtle()
  t2 = turtle.Turtle()

  t1.up()
  t1.setpos(0, -100)  
  t1.down()
  
  t2.up()
  t2.setpos(0, 100)
  t2.down()

  screen.setup(800, 600)
  
  count = 0
  # while 반복문
  while True:
    # 입력 - turtle.textinput() 사용
    proceed = screen.textinput("주사위 게임", "주사위 게임을 시작하려면 y를 입력하시오")
    pen = t2.getpen()
    
    # if 조건, 논리연산자
    if not proceed.lower() == "y":
      # 출력: write()
      pen.write("게임을 진행하지 않습니다.", align="center", font=("Ariel", 20, "bold"))
      continue
    pen.clear()
    t2.hideturtle()
    # 연산자
    count += 1
    print(f"{count}: number")
    # random 모듈 사용: random.randint
    number = randint(0, 5)
    
    # 이미지 출력
    screen.addshape(dice[number])
    t1.shape(dice[number])
