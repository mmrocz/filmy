class Movies:
    def __init__(self, ser_mov, title, year, genre):
        self.ser_mov = ser_mov
        self.title = title
        self.year = year
        self.genre = genre
        self.views_no = 1

    def __str__(self):
        return f' {self.title} {self.year}'

    def __repr__(self):
        return f' title = {self.title} year = {self.year}'

    def play(self, step=1):
        self.viewes_no += step

movie1 = Movies(ser_mov = "m", title = "The Big", year = "1968", genre = "comedy", )
movie2 = Movies(ser_mov = "m", title = "The Pretenders", year = "2002", genre = "thriller", ms = "m")
movie3 = Movies(ser_mov = "m", title = "The Mightinhk", year = "1933", genre = "comedy", ms = "m")
movie4 = Movies(ser_mov = "m", title = "Triple", year = "1970", genre = "comedy", ms = "m")
movie5 = Movies(ser_mov = "m", title = "Other side", year = "2007", genre = "Fantasy", ms = "m")

movies_list = [movie1, movie2, movie3, movie4, movie5]

class TV_Series:

    def __init__(self, s, title, year, genre):
        super().__init__(title, year, genre)
        self.ser_mov = s
        self.episode_no = 0
        self.season_no = 0
        self.episodes_per_season = 10
        self.seasons_count = 5
        self.no_play = 100


    def __str__(self):
        return f' {self.title} S{self.season_no}E{self.episode_no}'

    def __repr__(self):
        return f" title = title = {self.title} S, season_no = {self.season_no} E, episode_no = {self.episode_no}"

    def play(self, step=1):
        self.no_play += step
        self.season_no < 6
        if self.episode_no == 10:
            self.season_no += step
            self.episode_no == 1
        else:
            self.episode_no += step

movie1 = Movies(ser_mov="m", title="The Big", year="1968", genre="comedy", )
movie2 = Movies(ser_mov="m", title="The Pretenders", year="2002", genre="thriller", ms="m")
movie3 = Movies(ser_mov="m", title="The Mightinhk", year="1933", genre="comedy", ms="m")
movie4 = Movies(ser_mov="m", title="Triple", year="1970", genre="comedy", ms="m")
movie5 = Movies(ser_mov="m", title="Other side", year="2007", genre="Fantasy", ms="m")





    def series(self, step=1):
        self.season_no += step