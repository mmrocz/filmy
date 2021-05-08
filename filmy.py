class Movies:
    def __init__(self, title, year, genre):
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


class TV_Series:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre
        self.views_no = 1

    def __str__(self):
        return f' {self.title} {self.year}'

    def __repr__(self):
        return f" title = {self.title} year = {self.year}"

    def play(self, step=1):
        self.views_no += step

    def __init__(self, title, year, genre):
        super().__init__(title, year, genre)
        self.series_tracker.append(self)
        ##Variables
        self.episode_no = 0
        self.season_no = 0
        self.episodes_per_season = 10
        self.seasons_count = 5
        self.no_play = 100
        self.ms = ms

    def __str__(self):
        return f' {self.title} S{self.season_no}E{self.episode_no}'

    def __repr__(self):
        return f" title = title = {self.title} S, season_no = {self.season_no} E, episode_no = {self.episode_no}"

    def play(self, step=1):
        self.no_play += step
        self.season_no < 6
        if self.episode_no == 10:  ## zmienna
            self.season_no += step
            self.episode_no == 1
        else:
            self.episode_no += step
        "Ostatni odcinek lub zerować"

    @property
    def episode(self):
        return self._episode_no

    @episode.setter
    def episode(self, number):
        if number <= 250:
            self._episode_no = number
        else:
            raise ValueError(f"Please check epiode_no. {number}")

    def series(self, step=1):
        self.season_no += step