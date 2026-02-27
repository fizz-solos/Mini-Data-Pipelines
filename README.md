
# Mini Data Pipeline

A Python project for cleaning student data, assigning grades, and generating summary reports using pandas.

## Features
- Cleans raw student CSV data (removes missing values, fills blanks, drops duplicates)
- Assigns grades based on scores
- Calculates summary statistics (average, highest score, pass count)
- Saves cleaned data and report to files
- Robust error handling for file operations

## Requirements
- Python 3.10+
- pandas

## Setup
1. Clone the repository:
	```sh
	git clone https://github.com/fizz-solos/Mini-Data-Pipeline.git
	cd Mini-Data-Pipeline
	```
2. (Optional) Create a virtual environment:
	```sh
	python -m venv venv
	venv\Scripts\activate  # On Windows
	```
3. Install dependencies:
	```sh
	pip install pandas
	```

## Usage
1. Place your raw student CSV file in the project folder (default: `students.csv`).
2. Run the pipeline:
	```sh
	python data_pipeline.py
	```
3. Outputs:
	- `students_clean.csv`: Cleaned student data
	- `report.txt`: Summary statistics

## File Structure
```
Mini-Data-Pipeline/
├── data_pipeline.py
├── students.csv
├── students_clean.csv
├── report.txt
├── .gitignore
├── LICENSE
└── README.md
```

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author
- fizz-solos

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## Acknowledgements
- Built with [pandas](https://pandas.pydata.org/)
- Inspired by real-world data cleaning needs
