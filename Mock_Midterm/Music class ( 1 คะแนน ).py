"""[Mock Midterm] Music class ( 1 คะแนน )"""
class Song:

    def __init__(self, name, genre, durations):
        self.name = name
        self.genre = genre
        self.durations = durations

    def show_info(self):
         return f"{self.name} <|> {self.genre} <|> {self.durations // 60}.{self.durations % 60:02d}"

def main():
    Rickroll = Song(input(), input(), int(input()))
    print(Rickroll.show_info())
main()
