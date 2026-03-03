import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
movies = pd.read_csv(os.path.join(script_dir, "movies.csv"))
ratings = pd.read_csv(os.path.join(script_dir, "ratings.csv"))


# =============================================
# TASK 1: Load both CSVs
# =============================================
# Load movies.csv into a DataFrame called movies
# Load ratings.csv into a DataFrame called ratings
# Print head() of both
print(movies.head())
print(ratings.head())
print(movies.shape)
print(ratings.shape)

# =============================================
# TASK 2: Inspect and find issues
# =============================================
# Print isnull().sum() for ratings
# Print ratings.describe() to spot any weird values
# Look for:
#   - Missing ratings
#   - Invalid ratings (rating should be between 0 and 10)
#   - Duplicate rows
print("\n")
print(ratings.isnull().sum())
print(ratings.describe())
print(ratings.duplicated(subset=["movie_id", "user", "rating", "review_date"]).sum())


# =============================================
# TASK 3: Clean the ratings DataFrame
# =============================================
# - Drop rows where rating is missing
# - Remove rows where rating > 10 (invalid)
# - Drop duplicate rows
# Print shape before and after each step

ratings = ratings.drop_duplicates(subset=["movie_id", "user", "rating", "review_date"])
ratings = ratings.dropna(subset = ["rating"])
ratings = ratings[ratings["rating"] <= 10]
print(f"Rows after removing invalid ratings: {len(ratings)}")
print(ratings.shape)

# =============================================
# TASK 4: Merge the two DataFrames
# =============================================
# Merge ratings with movies on movie_id
# Use an inner join (only keep ratings that have a matching movie)
# Call the result df
# Print df.head() and df.shape
# Hint: pd.merge(ratings, movies, on="movie_id", how="inner")

df = pd.merge(ratings, movies, on="movie_id", how="inner")
print(df.head())
print(df.shape)
print(df)

# =============================================
# TASK 5: GroupBy analysis
# =============================================
# Using the merged df:
# - Find the average rating per movie (groupby title, mean of rating)
#   Sort by average rating descending and print top 5
# - Find the average rating per genre (groupby genre, mean of rating)
# - Find the director with the highest average rating
#   Hint: groupby("director")["rating"].mean().idxmax()

average_rating = df.groupby("title")["rating"].mean().sort_values(ascending = False).head(5)
print(average_rating)
per_genre = df.groupby("genre")["rating"].mean()
print(per_genre)
best_director = df.groupby("director")["rating"].mean().idxmax()
print(best_director)




# =============================================
# TASK 6: Add a derived column
# =============================================
# Add a column called "rating_category":
#   - rating >= 9.0 → "Excellent"
#   - rating >= 7.0 → "Good"
#   - below 7.0 → "Average"
# Hint: use apply() with a function, just like get_grades() in your pipeline
def get_category (rating):
    if rating >= 9.0:
        return "Excellent"
    elif rating >= 7.0:
        return "Good"
    else:
        return "Average"

df["rating_category"] = df["rating"].apply(get_category)
print(df)



# =============================================
# TASK 7: Save cleaned merged data
# =============================================
# Save df to "movies_clean.csv" in the same folder
# Use index=False and wrap in try/except
def save_clean(df):
    try:
        df.to_csv(os.path.join(script_dir, "movies_clean.csv"), index = False)
        print("Cleaned Data saved Successfully")
    except Exception as e:
        print(f"Error: Failed to Save Cleaned Data{e}")

save_clean(df)


print("Done!")
