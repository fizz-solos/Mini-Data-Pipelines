import pandas as pd
import os

# This makes sure the file is found regardless of where you run the script from
script_dir = os.path.dirname(os.path.abspath(__file__))
df = pd.read_csv(os.path.join(script_dir, "students.csv"))

print("Raw Data")
print(df)

print("\nShape(rows, colums)")
print(df.shape)

print("\nMissing Vales per column")
print(df.isnull().sum())

def get_grades(Score):
    if Score >= 80:
        return "A"
    elif Score >= 60:
        return "B"
    elif Score >= 50:
        return "C"
    else:
        return "F"

df["Grade"] = df["Score"].apply(get_grades)

df = df.dropna(subset = ["Name"])

df = df.dropna(subset =  ["Score"])

df["Age"] = df["Age"].fillna(df["Age"].mean())


df = df.drop_duplicates()


print("\nCleaned Data")
print(df)

print("\nMissing Values After Cleaning")
print(df.isnull().sum())

avg_score = df["Score"].mean()
print(avg_score)
highest_score = df["Score"].max()
print(highest_score)
Highest_scorer = df[df["Score"] == df["Score"].max()]["Name"].values[0]
print(Highest_scorer)
passed = df[df["Score"] >= 50]
print(len(passed))

def save_clean_data(df):
    try:
        df.to_csv(os.path.join(script_dir, "students_clean.csv"), index = False)
        print("Clean data saved succesfully")
    except Exception as e:
        print(f"Failed to save Cleaned data: {e}")

def save_report(avg_score, highest_score, Highest_scorer, passed, filename):
    try:
        with open (filename, "w") as f:
            stats = [
               ("Average Score", avg_score),
               ("Highest Score", highest_score),
               ("Top Student", Highest_scorer),
               ("Students Passed", len(passed))
            ]
            for label, value in stats:
                f.write(f"{label}: {value}\n") 
        print("Report Created") 
        
    except Exception as e:
        print(f"Error: Report creation failed")


save_clean_data(df)
save_report(avg_score, highest_score, Highest_scorer, passed, os.path.join(script_dir, "report.txt"))