import tmdbsimple as tmdb

tmdb.API_KEY = tmdb.API_KEY = '454b6ca4172e455fe7a7d8395c10d6d9'

# http get request:

search = tmdb.Search()
response = search.movie(query="Alien", year=1979)['results']

movie = tmdb.Movies(response[0]["id"])
print(response[0])  # <-- .json file ban jön le!!!
print(movie.credits())


""" 30 perc """