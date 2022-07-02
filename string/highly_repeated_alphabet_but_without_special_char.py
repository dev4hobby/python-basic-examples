import re
from collections import defaultdict

with open("message.txt", "r") as f:

    words = re.sub("[-=+,#/\?:^.@*\"※~ㆍ!』‘|\(\)\[\]`'…》\”\“\’·]", "", f.read()).split()

word_by_count = defaultdict(int)
for word in words:
    word_by_count[word] += 1

sorted_dict = dict(sorted(word_by_count.items(), key=lambda x: x[1], reverse=True))
for index, d in enumerate(sorted_dict.items()):
    if index > 9:
        break
    print(f"{d[0]}: {d[1]}")
