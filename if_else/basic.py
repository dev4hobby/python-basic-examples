id1 = "hello"
id2 = "world"
input_id = input(f"Input ID [{id1}, {id2}] : ")
print(f"Your ID: {input_id}")
if input_id == id1:
    print("welcome")
elif input_id == id2:
    print("welcome")
else:
    print("what?")
