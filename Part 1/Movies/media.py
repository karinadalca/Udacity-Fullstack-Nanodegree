import webbrowser

class Movie():
  #Triple quotes for ducumentation and can be access using media.Movie.__doc__
  """This class provides a way to store movie related informtion"""
  
  #This is a class variable and can be acess using media.Movie.valid_ratings, all instances have access to it
  valid_ratings = ["G","PG","PG-13","NC-16", "R"]

  def __init__(self, movie_title, movie_storyline, movie_poster, movie_trailer):
    self.title = movie_title
    self.storyline = movie_storyline
    self.poster_image_url = movie_poster
    self.trailer_youtube_url = movie_trailer

  def show_trailer(self):
    webbrowser.open(self.trailer_youtube_url)