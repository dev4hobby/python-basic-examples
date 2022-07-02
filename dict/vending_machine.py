from collections import defaultdict

vending_machine = {
    "cocacola": {"price": 1500, "stock": 10},
    "pepsi": {"price": 1000, "stock": 5},
    "fanta": {"price": 1200, "stock": 3},
    "sprite": {"price": 1000, "stock": 5},
    "7up": {"price": 7777, "stock": 5},
}

my_items = defaultdict(int)


def print_stock(vending_machine):
    for key, value in vending_machine.items():
        print(f"{key}의 재고는 {value['stock']}개 입니다. [{value['price']}원]")


def print_my_items(my_items):
    for key, value in my_items.items():
        print(f"{key}를 {value}개 구매했어요.")


money = int(input("입금: "))
if money < 10000:
    print("입금액이 부족합니다.")
else:
    minimum_cost = min([x["price"] for x in vending_machine.values()])
    while money >= minimum_cost:
        print(f"현재 남은 돈: {money}")
        print_stock(vending_machine)
        user_input = input("상품명: ")
        if user_input in vending_machine:
            if vending_machine[user_input]["stock"] > 0:
                print(f"{user_input}을(를) 판매합니다.")
                vending_machine[user_input]["stock"] -= 1
                money -= vending_machine[user_input]["price"]
                my_items[user_input] += 1
            else:
                print(f"{user_input}은(는) 매진-☆")
        elif user_input == "exit":
            print("자판기 이용을 종료합니다")
            break
        else:
            print("없어요 ㅜㅠ")

print_my_items(my_items)
