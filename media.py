import webbrowser


class Movie:
    """This Class contains a set of attributes for the Movies """
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        """ Initialise the Movie Class

        Args:
            movie_title (str): The title of the movie
            movie_storyline (str): A Short summary of the story
            poster_image (str): A URL to the poster image
            trailer_youtube (str): A URL toe the trailer on YouTube

        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """Open the trailer in the browser window"""
        webbrowser.open(self.trailer_youtube_url)
