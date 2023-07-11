import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.themoviedb.org/t/p/original/9KXhBcEutPbWLJK7VylUzYWwQlp.jpg")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/d/d6/Avatar_%282009_film%29_poster.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

late_spring = media.Movie("Late Spring",
                          "A story exploring the complexities of familial love and societal expectations",
                          "https://www.themoviedb.org/t/p/original/9KXhBcEutPbWLJK7VylUzYWwQlp.jpg",
                          "https://www.youtube.com/watch?v=_4Ul10BSzRw")

spirited_away = media.Movie("Spirited Away",
                            "A young girl's enchanting journey in a mysterious spirit world",
                            "https://upload.wikimedia.org/wikipedia/zh/0/09/Spirited_away_poster.jpg",
                            "https://youtu.be/ByXuk9QqQkk")

movies = [toy_story, avatar, late_spring, spirited_away]
fresh_tomatoes.open_movies_page(movies)
# print(media.Movie.valid_rating)
# print(media.Movie.__name__)
# print(media.Movie.__doc__)