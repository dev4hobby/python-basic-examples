class MP3:
    def __init__(self):
        self.music = [
            "Dynamite.mp3",
            "다시 여기 바닷가.mp3",
            "마리아 (Maria).mp3",
            "When We Disco.mp3",
            "How You Like That.mp3",
            "눈누난나.mp3",
            "그 여름을 틀어줘.mp3",
        ]

    def add_song(self, song):
        print(f"--곡 추가: {song}")
        self.music.append(song)

    def remove_song(self, song):
        print(f"--곡 제거: {song}")
        self.music.remove(song)

    def show_playlist(self):
        print("--곡 리스트 출력--")
        for song in self.music:
            print(song)

    def play(self):
        print("--일반 재생 모드--")

    def shuffle(self):
        from random import shuffle

        print("--셔플 모드--")
        shuffle(self.music)


if __name__ == "__main__":
    mp3 = MP3()
    mp3.add_song("아리랑~.mp3")
    mp3.play()
    mp3.show_playlist()
    print("-----------------")
    mp3.shuffle()
    mp3.remove_song("눈누난나.mp3")
    mp3.show_playlist()
