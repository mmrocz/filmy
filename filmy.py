
from datetime import date
from random import randint

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
        return f' {self.title} ({self.year})'

    def play(self, step=1):
        self.viewes_no += step

movie1 = Movies(ser_mov = "m", title = "The Big", year = "1968", genre = "comedy")
movie2 = Movies(ser_mov = "m", title = "The Pretenders", year = "2002", genre = "thriller")
movie3 = Movies(ser_mov = "m", title = "The Mightinhk", year = "1933", genre = "comedy")
movie4 = Movies(ser_mov = "m", title = "Triple", year = "1970", genre = "comedy")
movie5 = Movies(ser_mov = "m", title = "Other side", year = "2007", genre = "Fantasy")

movies_series_list = [movie1, movie2, movie3, movie4, movie5]

class TV_Series(Movies):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode_no = 0
        self.season_no = 0



    def __str__(self):
        return f"'{self.title}': S{self.season_no:02d}E{self.episode_no:02d}"

    def __repr__(self):
        return f"'{self.title}': S{self.season_no:02d}E{self.episode_no:02d}"

    def play(self, step=1):
        self.viewes_no += step

series1 = TV_Series(ser_mov="s", title="The was", year="1965", genre = "comedy")
series2 = TV_Series(ser_mov="s", title="The Pretender", year="2005", genre="thriller")
series3 = TV_Series(ser_mov="s", title="The Mightin", year="1937", genre="comedy")
series4 = TV_Series(ser_mov="s", title="Trip", year="1970", genre="comedy")
series5 = TV_Series(ser_mov="s", title="Other", year="2009", genre="Fantasy")

movies_series_list += [series1, series2, series3, series4, series5]

def search(movies_series_list, title):
    for picture in movies_series_list:
        if picture.title == title:
            return picture
print(search(movies_series_list,"Trip"))
movies = []
def get_movies():
    for i in movies_series_list:
        if i.ser_mov == "m":
            movies.append(i)
        else:
            None
    return sorted(movies, key=lambda movie: movie.title)
get_movies()
series = []
def get_series():
    for i in movies_series_list:
        if i.ser_mov == "s":
           series.append(i)

        else:
           None
    return sorted(series, key=lambda series: series.title)
get_series()

def generate_views():
    picture = random.choice(movies_series_list)
    picture.views_no = random.randint(1, 100)
    return picture.views_no

def generate_views_x_10():
    for i in range(10):
        generate_views()

def top_titles(top):
    top_n_titles = []
    top_n_titles = sorted(movies_series_list, key = lambda film: film.views_no, reverse = True)[:top]
    return top_n_titles
print(f"The most popular films and series as of {date.today():%d.%m.%Y}:")
print(top_titles(3))
print(movies_series_list)