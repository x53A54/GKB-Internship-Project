# Import pandas for data manipulation
import pandas as pd
# Load movies and ratings CSV files
movies = pd.read_csv("movies.csv",encoding='ISO-8859-1')
ratings = pd.read_csv("ratings.csv",encoding='ISO-8859-1')
#converting genres string from dataset to a list
movies['genres'] = movies['genres'].str.split('|')
movies_exploded = movies.explode('genres')
# Merge movies and ratings on 'movieId'
merged_df = pd.merge(movies_exploded, ratings, on='movieId')
valid_genres = merged_df['genres'].unique()
# Prompt user to enter a genre
print("Available genres:", ", ".join(valid_genres))
genre_input = input("Enter a genre (e.g., Action, Comedy, Drama): ")
genre_input = genre_input.title()
# Validate user input genre
if genre_input not in valid_genres:
    print(f"⚠️ Sorry, '{genre_input}' is not a valid genre. Please try one of these:\n{', '.join(valid_genres)}")
    genre_valid = False
else: 
    genre_valid = True
if genre_valid:     
    filtered_movies = merged_df[merged_df['genres'] == genre_input]


    selected_genre_stats = filtered_movies.groupby('title')['rating'].agg(['mean','count']).reset_index()
    selected_genre_stats.columns = ['title', 'avg_rating', 'num_ratings']
    selected_genre_stats = selected_genre_stats[selected_genre_stats['num_ratings'] >= 10]
    top_movies = selected_genre_stats.sort_values(by=['avg_rating', 'num_ratings'], ascending=False).head(5)
# Display top 5 movies of selected genre
    i = 1
    for row in top_movies.values:
        title = row[0]
        avg_rating = row[1]
        num_ratings = row[2]
        
        print(str(i) + ". " + title + " — ⭐ " + str(round(avg_rating, 2)) + " (" + str(num_ratings) + " ratings)")
        i += 1