class Movie:
    
    """Class responsible to store movie information"""
    
    def __init__(self, title, storyline, poster_image, youtube_trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
