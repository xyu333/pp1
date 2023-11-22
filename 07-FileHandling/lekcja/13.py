movie_titles = ["Spirited away", "Bladerunner 2049", "Star Wars", "John Wick", "Drive"]

file = open("movies.txt", 'a')
file.writelines('\n'.join(movie_titles))