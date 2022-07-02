from random import randint


class Gamble:
    def __init__(self, name, players):
        self.name = name
        self.prize = 0
        self.players = players  # 플레이어 리스트 ( 입장 순서대로 진행 )
        self.dice_result = {player.id: 0 for player in players}

    def bet(self):
        if self.prize > 0:
            return
        for player in self.players:
            while True:
                money = int(input(f"Player {player.id}님의 차례입니다. 얼마를 베팅하시겠습니까? >> "))
                if money > player.money:
                    print("돈이 부족합니다.")
                    continue
                player.money -= money
                self.prize += money
                break

    def roll_dice(self):
        for player in self.players:
            dice_number = player.roll_dice()
            print(f"Player {player.id}의 주사위 결과는 {dice_number}입니다.")
            self.dice_result[player.id] = dice_number

    def check_dice_result(self):
        odd = 0
        even = 0
        for dice_number in self.dice_result.values():
            if dice_number % 2 == 0:
                even += 1
            else:
                odd += 1
        if odd == 2:
            return 0
        elif even == 2:
            return 1
        else:
            return -1

    def win_the_prize(self, player_index):
        print(f"상금: {self.prize}")
        self.players[player_index].money += self.prize
        print(f"Player {self.players[player_index].id} 님이 이겼습니다.")
        print(f"{self.prize} 원을 얻었습니다.")
        self.prize = 0

    def check_winner(self, result):
        if result == -1:
            return False
        self.win_the_prize(player_index=result)
        return True

    def is_players_money_under_zero(self):
        for player in self.players:
            if player.money <= 0:
                return True
        return False

    def show_players_money(self):
        for player in self.players:
            print(f"Player {player.id}님의 돈은 {player.money}원입니다.")

    def play_dice(self):
        while True:
            self.bet()
            self.roll_dice()
            result = self.check_dice_result()
            if not self.check_winner(result):
                print("")
                continue
            self.show_players_money()
            if self.is_players_money_under_zero():
                break


class Player:
    def __init__(self, id, money=1000):
        self.id = id
        self.money = money
        self.dice_log = []

    def roll_dice(self):
        return randint(1, 6)


if __name__ == "__main__":
    player_1 = Player(1)
    player_2 = Player(2)
    gamble = Gamble("주사위게임", [player_1, player_2])
    gamble.play_dice()
