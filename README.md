# AB_NYC_Data_Analysis
Exploratory Data Analysis on the AB_NYC_2024 Airbnb dataset

## Run the analysis

1. Install dependencies:
   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
2. Run:
   ```bash
   python /home/runner/work/AB_NYC_Data_Analysis/AB_NYC_Data_Analysis/ab_nyc_2024_analysis.py --input /absolute/path/to/AB_NYC_2024.csv --output /absolute/path/to/output_dir
   ```

The script performs:
- data cleaning (duplicate removal, numeric conversion, null handling, and price outlier filtering),
- exploratory summary generation (`eda_summary.csv`),
- visualization output (`.png` charts),
- cleaned data export (`AB_NYC_2024_cleaned.csv`).
