class MovieNotFoundError(Exception):
    """Exception handling when moview not found"""
    def __init__ (self, movie_name):
        self.movie_name = movie_name

    def __str__ (self):
        return f"{self.movie_name.title()} is not found. Please read your bible instead."

class TooManyRequestsError(Exception):
    """Exception handling for too many requests"""
    def __init__ (self, movie_name, available):
        self.movie_name = movie_name
        self.available = available
    def __str__ (self):
        return f"You made too many requests. We only have {self.available} copies of {self.movie_name.title()}"

movie_inventory = {
    "the chosen": 5,
    "lion king" : 3,
    "the lion and the lamb": 2,
    "war room": 4,
    "the forge" : 5
}

def get_movie(name, copies):
    if name not in movie_inventory or movie_inventory[name] == 0:
        raise MovieNotFoundError(name)
    elif copies > movie_inventory[name]:
        raise TooManyRequestsError(name, movie_inventory[name])
    else:
        movie_inventory[name] -= copies
        return f"{name.title()} rented successful. Go thee, watch, get inspired and preach the gospel of Christ"

def request_movie():
    user_movie = input("Enter a movie to rent: ").lower()
    user_copies = int(input("Enter number of copies to rent: "))
    try:
        print(get_movie(user_movie, user_copies))
    except (TooManyRequestsError, MovieNotFoundError) as e:
        print(e)
    
request_movie()


          
