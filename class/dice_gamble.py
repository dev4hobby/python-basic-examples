from random import randint

print(
    """JUSAWI DOBAK에 오신 것을 환영합니다
      룰: 
      1.player1과 plyaer2는 각각 100000원의 시드 머니를 소지하며 게임을 시작하게됩니다.
      2.한턴마다 player1과 2에게는 배팅의 기회가 주어지고 배팅이 끝난뒤 Player1님의 주사위와 Player2님의 주사위가 굴려지게됩니다.
      3.만약 player1님의 주사위가 홀수이며 player2님의 주사위 또한 홀수일 경우 player1님이 player2님의 배팅 금액을 가져가게됩니다.
      4.만약 player2님의 주사위가 짝수이며 player1님의 주사위 또한 짝수일 경우 player2님이 player1님의 배팅 금액을 가져가게됩니다.
      5.만약 player1님의 주사위가 짝수이며 player2님의 주사위가 홀수일 경우 주사위는 룰 2 혹은 3의 상황이 나오면 주사위는 멈추며 다음 턴이 됩니다.
      6.Player중 한명이 돈을 모두 잃으면 게임은 종료되며 돈을 지니고 있는 player가 승리하게됩니다."""
)


class Gamble:
    def __init__(self, name, players):
        self.name = name
        self.prize = 0
        self.players = players
        self.dice_result = {player.id: 0 for player in players}

    def bet(self):
        if self.prize > 0:
            return
        for player in self.players:
            while True:
                money = int(input(f"Player {player.id}님의 차례입니다. 얼마를 베팅하시겠습니까? >> "))
                if money > player.money:
                    print("돈이 부족;;")
                    continue
                player.money -= money
                player.last_bet = money
                self.prize += money
                break

    def roll_dice(self):
        for player in self.players:
            dice_number = player.roll_dice()
            print(f"Player {player.id}의 주사위 결과는 {dice_number}입니다.")
            self.dice_result[player.id] = dice_number
            if dice_number == 1:
                print(
                    """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
                )
            elif dice_number == 2:
                print(
                    """

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠻⣿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠿⠟⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
                )
            elif dice_number == 3:
                print(
                    """
⠀⠀⠀⣠⣴⣦⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣾⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠻⠿⠿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡧⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠉⠁⠀⠀
"""
                )
            elif dice_number == 4:
                print(
                    """
⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀
⠀⠀⠀⣰⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⣿⣿⣿⣦⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠇⠀
⠀⠀⠀⠹⢿⣿⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⠟⠀⠀
⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀
⠀⠀⠀⣰⣾⣿⣿⣷⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣦⠀⠀
⠀⠀⠀⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡆⠀
⠀⠀⠀⠹⣿⣿⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⠟⠀⠀
⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀
"""
                )
            elif dice_number == 5:
                print(
                    """
⠀⠀⠀⠀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⡀⠀⠀⠀
⠀⠀⢠⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣧⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠈⠻⢿⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⠿⠋⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣿⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣤⣶⣶⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣶⣶⣦⡄⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠸⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⣿⣿⣿⡿⠀⠀
⠀⠀⠀⠈⠙⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠉⠀⠀⠀
"""
                )
            elif dice_number == 6:
                print(
                    """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⣴⣿⣿⣷⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⣷⡄⠀⠀
⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠈⢿⣿⣿⣿⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⠏⠀⠀
⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣄⠀⠀⠀
⠀⢰⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣷⠀⠀
⠀⠸⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⡿⠀⠀
⠀⠀⠈⠛⠛⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠋⠀⠀⠀
⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀
⠀⢀⣾⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣆⠀⠀
⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀
⠀⠀⠻⠿⣿⡿⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠻⣿⣿⠿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
                )

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
        self.players[player_index].money += self.players[player_index].last_bet
        print(f"Player {self.players[player_index].id} 님이 이겼습니다.")
        print(f"{self.prize + self.players[player_index].last_bet} 원을 얻었습니다.")
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
    def __init__(self, id, money=100000):
        self.id = id
        self.money = money
        self.dice_log = []
        self.last_bet = 0

    def roll_dice(self):
        return randint(1, 6)


if __name__ == "__main__":
    player_1 = Player(1)
    player_2 = Player(2)
    gamble = Gamble("주사위게임", [player_1, player_2])
    gamble.play_dice()
