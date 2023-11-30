# importing the module
import imdb
# creating an instance of the IMDB()
ia = imdb.IMDb()
# Using the Search movie method
items = ia.search_movie('spider man')
for i in items:
    print(i)