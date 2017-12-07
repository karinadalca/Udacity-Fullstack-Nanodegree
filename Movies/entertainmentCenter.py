import media
import fresh_tomatoes

home_alone = media.Movie("Home Alone", 
"An eight-year-old troublemaker must protect his house from a pair of burglars when he is accidentally left home alone by his family during Christmas vacation.", 
"http://www.lunalowell.com/wp-content/uploads/2016/06/A1srz798CtL._RI_.jpg", 
"https://www.youtube.com/watch?v=IsOlj-xpK9Q")

the_grinch_who_stole_christmas = media.Movie("The Grinch Who Stole Christmas", 
"On the outskirts of Whoville, there lives a green, revenge-seeking Grinch who plans on ruining the Christmas holiday for all of the citizens of the town.", 
"https://images-na.ssl-images-amazon.com/images/I/911wL8nnXqL._SL1500_.jpg", 
"https://www.youtube.com/watch?v=DD0m9t4WHEQ")

a_christmas_carol = media.Movie("A Christmas Carol", 
"An animated retelling of Charles Dickens' classic novel about a Victorian-era miser taken on a journey of self-redemption, courtesy of several mysterious Christmas apparitions.", 
"https://chasness.files.wordpress.com/2009/09/christmas_carol1.jpg", 
"https://www.youtube.com/watch?v=VZ3lr3urgDU")

polar_express = media.Movie("Polar Express", 
"A young boy embarks on a magical adventure to the North Pole on the Polar Express. During his adventure he learns about friendship, bravery, and the spirit of Christmas.", 
"http://img.moviepostershop.com/the-polar-express-movie-poster-2004-1010245395.jpg",
"https://www.youtube.com/watch?v=TQhRqtt-Fpo")

the_holiday = media.Movie("The Holiday", 
"Two women troubled with guy-problems swap homes in each other's countries, where they each meet a local guy and fall in love.", 
"https://images-na.ssl-images-amazon.com/images/I/51BwEnFkE8L.jpg", 
"https://www.youtube.com/watch?v=BDi5zH18vxUn")

the_nightmare_before_christmas = media.Movie("The Nightmare Before Christmas", 
"Jack Skellington, king of Halloween Town, discovers Christmas Town, but his attempts to bring Christmas to his home cause confusion.", 
"https://images-na.ssl-images-amazon.com/images/I/51dcxcKen2L._SY300_.jpg", 
"https://www.youtube.com/watch?v=wr6N_hZyBCk")

christmas_movies = [home_alone, the_grinch_who_stole_christmas, a_christmas_carol, polar_express, the_holiday, the_nightmare_before_christmas]

fresh_tomatoes.open_movies_page(christmas_movies)

#printing class variables
#print(media.Movie.valid_ratings)
#print(media.Movie.__doc__)
#print(media.Movie.__name__)
#print(media.Movie.__module__)