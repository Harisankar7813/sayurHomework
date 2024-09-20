#Ask your friend all the movies s/he watched recently. List all the movies that you both have watched,
#only the movies you watched, and only the movies your friend  watched.
movie_watched_me=['shinchan','pokemon','doremon','naruto','attack on titans']
movie_watched_frd=['naruto','demon slayers','attack on titans','boruto']
both_watched=(set(movie_watched_me)-(set(movie_watched_me)-set(movie_watched_frd)))
print("movies watched by both:",both_watched)
me_only=set(movie_watched_me)
print("movie watched by me only:",me_only)
friends_only=set(movie_watched_frd)
print("movie watched by friends only",friends_only)