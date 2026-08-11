import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ===========================
# Movie Dataset
# ===========================

movies_data = [
    {"title": "Toy Story", "genres": "Adventure Animation Children Comedy Fantasy"},
    {"title": "Jumanji", "genres": "Adventure Children Fantasy"},
    {"title": "Grumpier Old Men", "genres": "Comedy Romance"},
    {"title": "Waiting to Exhale", "genres": "Comedy Drama Romance"},
    {"title": "Father of the Bride Part II", "genres": "Comedy"},
    {"title": "Heat", "genres": "Action Crime Thriller"},
    {"title": "Sabrina", "genres": "Comedy Romance"},
    {"title": "Tom and Huck", "genres": "Adventure Children"},
    {"title": "Sudden Death", "genres": "Action Thriller"},
    {"title": "GoldenEye", "genres": "Action Adventure Thriller"},
    {"title": "Batman Begins", "genres": "Action Adventure Crime"},
    {"title": "The Dark Knight", "genres": "Action Crime Drama"},
    {"title": "The Dark Knight Rises", "genres": "Action Adventure"},
    {"title": "Avengers: Endgame", "genres": "Action Adventure Sci-Fi"},
    {"title": "Iron Man", "genres": "Action Adventure Sci-Fi"},
    {"title": "Captain America: Civil War", "genres": "Action Adventure Sci-Fi"},
    {"title": "Spider-Man: No Way Home", "genres": "Action Adventure Fantasy"},
    {"title": "Doctor Strange", "genres": "Action Adventure Fantasy"},
    {"title": "Interstellar", "genres": "Adventure Drama Sci-Fi"},
    {"title": "Inception", "genres": "Action Adventure Sci-Fi Thriller"},
    {"title": "The Matrix", "genres": "Action Sci-Fi"},
    {"title": "John Wick", "genres": "Action Crime Thriller"},
    {"title": "The Shawshank Redemption", "genres": "Drama"},
    {"title": "Forrest Gump", "genres": "Comedy Drama Romance"},
    {"title": "Titanic", "genres": "Drama Romance"},
    {"title": "The Conjuring", "genres": "Horror Mystery Thriller"},
    {"title": "Annabelle", "genres": "Horror Mystery"},
    {"title": "It", "genres": "Horror Thriller"},
    {"title": "The Nun", "genres": "Horror Mystery"},
    {"title": "Frozen", "genres": "Animation Adventure Fantasy"},
    {"title": "Moana", "genres": "Animation Adventure Comedy Fantasy"},
    {"title": "Finding Nemo", "genres": "Animation Adventure Comedy"},
    {"title": "Cars", "genres": "Animation Comedy Adventure"},
    {"title": "Kung Fu Panda", "genres": "Animation Action Adventure Comedy"},
    {"title": "Shrek", "genres": "Animation Adventure Comedy Fantasy"},
]

# Convert to DataFrame
movies = pd.DataFrame(movies_data)

# ===========================
# Machine Learning Part
# ===========================

vectorizer = CountVectorizer()
feature_matrix = vectorizer.fit_transform(movies["genres"])

similarity = cosine_similarity(feature_matrix)

# ===========================
# Recommendation Function
# ===========================

def recommend(movie_name):
    movie_name = movie_name.lower()

    matched = movies[movies["title"].str.lower().str.contains(movie_name)]

    if matched.empty:
        print("\nMovie not found.")
        return

    movie_index = matched.index[0]

    print("\nSelected Movie:", movies.iloc[movie_index]["title"])

    distances = list(enumerate(similarity[movie_index]))
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    print("\nTop 5 Recommended Movies:\n")

    count = 0
    for movie in distances:
        index = movie[0]

        if index != movie_index:
            print(f"{count+1}. {movies.iloc[index]['title']}")
            count += 1

        if count == 5:
            break

# ===========================
# Main Program
# ===========================

print("=" * 45)
print("      MOVIE RECOMMENDATION SYSTEM")
print("=" * 45)

while True:

    print("\nAvailable Movies:\n")
    for title in movies["title"]:
        print("-", title)

    choice = input("\nEnter a movie name (or type 'exit'): ")

    if choice.lower() == "exit":
        print("\nThank you for using Movie Recommendation System!")
        break

    recommend(choice)