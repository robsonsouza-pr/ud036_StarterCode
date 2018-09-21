class Movie:
    
    """Class responsible to store movie information"""
    
	#__init__ method is the constructor of the class and self seems like 'this' in Java
    def __init__(self, title, storyline, poster_image, youtube_trailer):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
