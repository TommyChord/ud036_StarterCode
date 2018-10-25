import fresh_tomatoes
import media

# Create a Movie instance for each of the movies
crossroads = media.Movie("Crossroads",
                         "Ralph Macchio is Lightning Boy. A kid who can make "
                         "a slide guitar sing. Blind Dog is an old pro who kno"
                         "ws it. Together, they're headed to a place where dea"
                         "ls are made. And legends are born.",
                         "https://upload.wikimedia.org/wikipedia/en/d/d8/Crossroadsposter1986.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=ntrCbhQw8yg")

risen = media.Movie("Risen",
                    "In 33 AD, a Roman Tribune in Judea is tasked to find the "
                    "missing body of Jesus Christ who rose from the dead.",
                    "https://upload.wikimedia.org/wikipedia/en/3/3c/Risen_2016_poster.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=OcTVLfn5i8g")

indiana_jones = media.Movie("Indiana Jones and the Kingdom of the Crystal Skull",
                            "In 1957, archaeologist and adventurer Dr. Henry "
                            "'Indiana' Jones, Jr. is called back into action"
                            " and becomes entangled in a Soviet plot to uncove"
                            "r the secret behind mysterious artifacts known as"
                            " the Crystal Skulls.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d5/Kingdomofthecrystalskull.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=WAdJf4wTC5Y")

only_imagine = media.Movie("I can only Imagine",
                           "The inspiring and unknown true story behind "
                           "MercyMe's beloved, chart topping song that brings "
                           "ultimate hope to so many is a gripping reminder "
                           "of the power of true forgiveness.",
                           "https://upload.wikimedia.org/wikipedia/commons/5/51/Lionsgate-I_Can_Only_Imagine.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=OsMyv9Q4_OU")

matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about "
                     "the true nature of his reality and his role in the war "
                     "against its controllers.",
                     "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=m8e-FF8MsqU")

silence_lambs = media.Movie("The Silence of the Lambs",
                            "A young FBI cadet must receive the help of an "
                            "incarcerated and manipulative cannibal killer to "
                            "help catch another serial killer, a madman who "
                            "skins his victims.",
                            "https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=W6Mm8Sbe__o")

# Create a list of the Movie instances
movies = [crossroads, risen, indiana_jones, only_imagine, matrix, silence_lambs]

# Generate the based on the instances in the list
fresh_tomatoes.open_movies_page(movies)


