# Mini Data Pipeline

Learning data cleaning and analysis by building small Python projects. This repo has three pipelines I built while practicing pandas.

## What's Here

### Student Data Pipeline
My first real data cleaning project. Takes messy student CSV data and cleans it up — drops missing values, fills blanks, removes duplicates, calculates grades, and saves a summary report.

**What I learned:** dropna, fillna, drop_duplicates, apply, basic error handling

[Code](data_pipeline.py)

---

### Sales Pipeline  
Cleaned sales data and did some analysis. Worked with groupby to calculate revenue by region and find the best-selling products.

**What I learned:** groupby, value_counts, boolean filtering, handling duplicates properly

[Code](sales%20pipeline/sales_pipeline.py)

---

### Movies Rating Pipeline
Merged two datasets (movies and ratings), cleaned them, and analyzed average ratings by movie, genre, and director. Also added a rating category column.

**What I learned:** pd.merge (like SQL JOIN), more complex groupby, using apply with functions

[Code](movies%20rating%20pipeline/movies_rating.py)

---

## Running the Code

You need Python 3.10+ and pandas installed.

```bash
pip install pandas
python data_pipeline.py
```

Each script reads a CSV, cleans it, and saves the output.

## License
MIT — use however you want.
