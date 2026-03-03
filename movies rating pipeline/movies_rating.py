import pandas as pd
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
movies = pd.read_csv(os.path.join(script_dir, "movies.csv"))
ratings = pd.read_csv(os.path.join(script_dir, "ratings.csv"))

print(movies.head())
print(ratings.head())
print(movies.shape)
print(ratings.shape)

print("\n")
print(ratings.isnull().sum())
print(ratings.describe())
print(ratings.duplicated(subset=["movie_id", "user", "rating", "review_date"]).sum())


ratings = ratings.drop_duplicates(subset=["movie_id", "user", "rating", "review_date"])
ratings = ratings.dropna(subset = ["rating"])
ratings = ratings[ratings["rating"] <= 10]
print(f"Rows after removing invalid ratings: {len(ratings)}")
print(ratings.shape)

df = pd.merge(ratings, movies, on="movie_id", how="inner")
print(df.head())
print(df.shape)
print(df)

average_rating = df.groupby("title")["rating"].mean().sort_values(ascending = False).head(5)
print(average_rating)
per_genre = df.groupby("genre")["rating"].mean()
print(per_genre)
best_director = df.groupby("director")["rating"].mean().idxmax()
print(best_director)

def get_category (rating):
    if rating >= 9.0:
        return "Excellent"
    elif rating >= 7.0:
        return "Good"
    else:
        return "Average"

df["rating_category"] = df["rating"].apply(get_category)
print(df)

def save_clean(df):
    try:
        df.to_csv(os.path.join(script_dir, "movies_clean.csv"), index = False)
        print("Cleaned Data saved Successfully")
    except Exception as e:
        print(f"Error: Failed to Save Cleaned Data{e}")

save_clean(df)

print("Done!")
