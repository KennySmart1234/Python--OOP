from movie import Movie

class MovieRating:
    def __init__(self):
        self.movies = []

    def add_movie(self , title:str, year, director, genre):
        title = title.lower()

        mv = Movie(title, year, director, genre)
        self.movies.append(mv)

    # def __repr__(self):
    #     return f"{self.movies}"


    def get_movies(self):
        return self.movies

    def rate_movie(self , title: str , rating: int): #-> None:
        if 0 > rating > 5:
            raise ValueError("rating must be between 0 and 5")
        for movie in self.movies:
            if movie.title == title.lower():
                movie.rating.append(rating)


    def get_rating(self ):
        for movie in self.movies:
            return movie.rating
        return None



mvr = MovieRating()
mvr.add_movie("koto aye", "2000", "Kenny", "")

mvr.add_movie("koto aye", "2000", "Kenny", "")
print(mvr.get_movies())