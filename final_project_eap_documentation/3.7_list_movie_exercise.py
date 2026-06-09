fav_movies = ["Dark Knight","Interstellar","Groundhog's Day","Inception"]
print("Favorite movies are: ",fav_movies)

new_movie = input("Insert new moview title: ")

if new_movie in fav_movies:
    print("Movie already exists in the list.")

fav_movies.append(new_movie)
fav_movies.sort()
print(fav_movies)
print("The number of your list is: ",len(fav_movies))