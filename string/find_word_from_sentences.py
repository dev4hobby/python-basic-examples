string = "asdf qwer zxcv asdf qwer zxcv asdfjkl;zxcvuiop"
freq = {}
while True:
    word = input("Enter a word: (to quit, 'q')")
    if word == "q":
        break
    elif word in string:
        freq[word] = string.count(word)
        print(word, "is found - frequency", freq)
    else:
        print("Not found")
