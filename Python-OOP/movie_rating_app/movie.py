class Movie:
    def __init__(self, title, year, director, genre):
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        self.rating = []
        

    def __repr__(self):
        return f"{self.title} in {self.year} by {self.director} by {self.genre} {str(self.rating)}"


