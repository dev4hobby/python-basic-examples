text = "aaabbbccccdddeeeeeeeeeefga"

text = text.lower()
import string

alpha_list = list(string.ascii_lowercase)


def get_from_list():
    alpha_count = [0] * 26
    for i in range(0, 26):
        c = text.count(alpha_list[i])
        alpha_count[i] = c

    # max_count = max(alpha_count)
    # if alpha_count[i] == max_count:
    #     print(f"가장 많이 사용된 알파벳은 {alpha_list[i]}이며 모두 {alpha_count[i]}번 사용되었습니다.")

    max_count = max(alpha_count)
    max_index = alpha_count.index(max_count)
    print(f"가장 많이 사용된 알파벳은 {alpha_list[max_index]}이며 모두 {max_count}번 사용되었습니다.")


get_from_list()
