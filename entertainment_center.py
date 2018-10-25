import fresh_tomatoes
import media


# toystory = media.Movie("Toy Story", "A story of a boy and his toys that come to life",
#                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
#                        "https://www.youtube.com/watch?v=tN1A2mVnrOM")
# avatar = media.Movie("Avatar", "A marine on an alien planet",
#                      "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
#                      "https://www.youtube.com/watch?v=-9ceBgWV8io")
# school_of_rock = media.Movie("School of Rock", "Storyline",
#                              "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
#                              "https://www.youtube.com/watch?v=3PsUJFEBC74")
# ratatouille = media.Movie("Ratatouille", "Storyline",
#                           "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
#                           "https://www.youtube.com/watch?v=c3sBBRxDAqk")
# midnight_in_paris = media.Movie("Midnight in Paris", "Storyline",
#                                 "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
#                                 "https://www.youtube.com/watch?v=FAfR8omt-CY")
# hunger_games = media.Movie("Hunger Games", "Storyline",
#                            "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
#                            "https://www.youtube.com/watch?v=7GcY6hwZF4M")
#
# movies = [toystory, avatar, school_of_rock, ratatouille, midnight_in_paris, hunger_games]

crossroads = media.Movie("Crossroads", "Storyline",
                         "https://upload.wikimedia.org/wikipedia/en/d/d8/Crossroadsposter1986.jpg",
                         "https://www.youtube.com/watch?v=ntrCbhQw8yg")

risen = media.Movie("Risen", "Storyline",
                    "https://upload.wikimedia.org/wikipedia/en/3/3c/Risen_2016_poster.jpg",
                    "https://www.youtube.com/watch?v=OcTVLfn5i8g")

indiana_jones = media.Movie("Indiana Jones and the Kingdom of the Crystal Skull", "Storyline",
                            "https://upload.wikimedia.org/wikipedia/en/d/d5/Kingdomofthecrystalskull.jpg",
                            "https://www.youtube.com/watch?v=WAdJf4wTC5Y")

only_imagine = media.Movie("I can only Imagine", "Storyline",
                           "https://upload.wikimedia.org/wikipedia/commons/5/51/Lionsgate-I_Can_Only_Imagine.jpg",
                           "https://www.youtube.com/watch?v=OsMyv9Q4_OU")

matrix = media.Movie("The Matrix", "Storyline",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")
silence_lambs = media.Movie("The Silence of the Lambs", "Storyline",
                            "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg",
                            "https://www.youtube.com/watch?v=W6Mm8Sbe__o")

movies = [crossroads, risen, indiana_jones, only_imagine, matrix, silence_lambs]
#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)
