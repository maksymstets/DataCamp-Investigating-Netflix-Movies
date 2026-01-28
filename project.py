import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv")
print(netflix_df.head())
print(netflix_df.shape)

# See column names and types
print(netflix_df.info())

# Check unique values in key columns
print(netflix_df['type'].unique())
print(netflix_df['genre'].unique())

movies_df = netflix_df[netflix_df['type'] == 'Movie']
movies_1990s = movies_df[(movies_df['release_year'] >= 1990) & (movies_df['release_year'] < 2000)]
duration = movies_1990s['duration'].mode()[0]
short_movies = movies_1990s[movies_1990s['duration'] < 90]
short_action = short_movies[short_movies['genre'] == 'Action']
short_movie_count = len(short_action)
print(f"Number of short action movies: {short_movie_count}")
# Verify duration
print(f"Most frequent duration: {duration}")
print(f"Type: {type(duration)}")  # Should be int

# Verify short_movie_count
print(f"Short action movie count: {short_movie_count}")
print(f"Type: {type(short_movie_count)}")  # Should be int

# Optional: View some examples
print("\nExample short action movies:")
print(short_action[['title', 'duration', 'genre', 'release_year']].head())
# 1. Top 5 Genres
all_genres = movies_1990s['genre'].str.split(', ').explode()
top_5_genres = all_genres.value_counts().head(5)
print("Top 5 Genres:")
print(top_5_genres)

# 2. Duration trend over time
avg_duration_by_year = movies_1990s.groupby('release_year')['duration'].mean()
print("\nAverage Duration by Year:")
print(avg_duration_by_year)

# 3. Top countries
top_countries = movies_1990s['country'].value_counts().head(10)
print(f"\nMost productive country: {top_countries.index[0]} ({top_countries.iloc[0]} movies)")

# Create all three visualizations
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

# Genre bar chart
top_5_genres.plot(kind='bar', ax=axes[0], color='coral', edgecolor='black')
axes[0].set_title('Top 5 Genres')
axes[0].set_xlabel('Genre')
axes[0].set_ylabel('Count')
axes[0].tick_params(axis='x', rotation=45)

# Duration trend line chart
avg_duration_by_year.plot(kind='line', ax=axes[1], marker='o', color='green')
axes[1].set_title('Average Duration Over Time')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('Minutes')
axes[1].grid(True, alpha=0.3)

# Country bar chart
top_countries.head(5).plot(kind='barh', ax=axes[2], color='steelblue', edgecolor='black')
axes[2].set_title('Top 5 Countries')
axes[2].set_xlabel('Number of Movies')

plt.tight_layout()
plt.show()
