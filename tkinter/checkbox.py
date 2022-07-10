from tkinter import *

def animal():
  c1= chk1.get()
  c2 = chk2.get()

  if (c1 == 1) and (c2 == 1):
    lbl2.configure(text ="토끼 거북이")
  elif (c1 == 1) and (c2 == 0):
    lbl2.configure(text ="토끼")
  elif (c1 == 0) and (c2 == 1):
    lbl2.configure(text ="거북이")
  else:
    lbl2.configure(text ="")


root = Tk()
root.title("체크박스")
root.geometry("230x120")

chk1 = IntVar()
chk2 = IntVar()

lbl1 = Label(root,text="- 좋아하는 동물을 모두 선택하시오 -")
lbl1.pack()

chb1 = Checkbutton(root, text="토끼", variable = chk1, command = animal)
chb1.pack()

chb2 = Checkbutton(root, text="거북이", variable = chk2, command = animal)
chb2.pack()

lbl2= Label(root, text="내가 좋아하는 동물")
lbl2.pack()

root.mainloop()