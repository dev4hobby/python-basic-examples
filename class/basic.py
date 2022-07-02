class Song:
    def __init__(self, lyrics=[]):
        self.lyrics = lyrics

    def sing(self):
        try:
            print(self.lyrics[0])
            self.lyrics = self.lyrics[1:]
        except IndexError:
            print("No more lyrics")


aSong = Song(
    [
        "first line",
        "second line",
        "third line",
        "fourth line",
    ]
)

aSong.sing()
aSong.sing()
aSong.sing()
aSong.sing()
aSong.sing()
