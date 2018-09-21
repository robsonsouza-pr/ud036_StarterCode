import media
import fresh_tomatoes

ironman = media.Movie("Ironman", "The first movie of MCU",
                        "https://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
                        "https://www.youtube.com/watch?v=byQpcN78UjQ")

cap = media.Movie("Captain America: The first Avenger", "The story of a weak man that became strong",
                        "https://upload.wikimedia.org/wikipedia/pt/d/d8/Capit%C3%A3o_Am%C3%A9rica_O_Primeiro_Vingador_-_Poster.jpg",
                        "https://www.youtube.com/watch?v=vlO0cX8lK88")

spiderman = media.Movie("Spiderman: homecoming", "The first movie of Spiderman at MCU",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcT4O7xrHjQ1NMu_9kg6E9HUO4X7KtB9lVpVLglQfWH2BJIke3IB",
                        "https://www.youtube.com/watch?v=U0D3AOldjMU")

movies = [ironman, cap, spiderman]

fresh_tomatoes.open_movies_page(movies)
