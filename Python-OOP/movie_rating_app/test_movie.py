import pytest

from  movie import Movie
from movie_rating import MovieRating

class TestMovie:
    def test_movie(self):
        Movie("koto aye", "2000", "Azeez",  "horror")


class TestRating:

    def setup(self):
        self.mvr = MovieRating()

    def test_add_movie(self):
        # self.mvr = MovieRating()
        assert len(self.mvr.movies) == 0
        self.mvr.add_movie("koto aye", 200, "Azeez", "horror")
        assert len(self.mvr.movies) == 1


    def test_rate_movie(self):
        # mvr = MovieRating()
        # assert len(self.mvr.movies) == 0
        # self.mvr.add_movie("koto aye", "2000", "Azeez", "horror")
        assert len(self.mvr.get_rating()) == 0
        self.mvr.rate_movie("koto aye", 5)
        assert len(self.mvr.get_rating()) == 1
        self.mvr.rate_movie("koto aye", 5)
        assert len(self.mvr.get_rating()) == 2

