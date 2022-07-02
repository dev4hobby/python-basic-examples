from datetime import datetime

class CellPhone:
    def __init__(self, mynum):
        self.mynum = mynum
        self.lastcall = None
        self.lastcallnum = None

    def __str__(self):
        return f"내 번호: {self.mynum}\n마지막 송수신이력: {self.lastcall}\n 마지막 통화번호: {self.lastcallnum}"

    def call(self, num):
        self.lastcall = "called"
        self.lastcallnum = num
        print(f"'{num}'로 전화를 걸고있습니다.")
        with open("phonecalllist.txt", "a") as f:
            datetime_now = datetime.now().strftime("%Y-%m%d %H:%M:%S")
            f.write(f"[{datetime_now}] 발신:{self.mynum} 수신:{num}\n")

    def receive(self, num):
        self.lastcall = "received"
        self.lastcallnum = num
        print(f"'{num}'로부터 전화가 왔습니다.")
        with open("phonecalllist.txt", "a") as f:
            datetime_now = datetime.now().strftime("%Y-%m%d %H:%M:%S")
            f.write(f"[{datetime_now}] 발신:{num} 수신:{self.mynum}\n")

    def show_lastcall(self):
        print(f"마지막 통화는 {self.lastcall}이며, 번호는 {self.lastcallnum} 입니다.")


phone1 = CellPhone("010-1234-5678")
phone2 = CellPhone("010-9876-5432")
print(f"Phone 1 >> {phone1}")
print(f"Phone 2 >> {phone2}")

phone1.call("010-9876-5432")
phone2.receive("010-1234-5678")

phone2.call("010-1234-5678")
phone1.receive("010-9876-5432")
phone2.call("010-1234-5678")
phone1.receive("010-9876-5432")

phone1.call("010-9876-5432")
phone2.receive("010-1234-5678")
phone1.call("010-9876-5432")
phone2.receive("010-1234-5678")

print(f"Phone 1 >> {phone1}")
print(f"Phone 2 >> {phone2}")
