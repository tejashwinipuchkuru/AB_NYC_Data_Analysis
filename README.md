Airbnb NYC 2024 — End-to-End Data Analytics Project

An end-to-end data analytics project built during a Data Analyst Internship, applying a complete real-world workflow to the Airbnb NYC 2024 dataset — from raw data to business-ready insights.
Python Pandas NumPy Matplotlib Seaborn SQL SQLite Power BI

Table of Contents:
Overview
Objectives
Workflow
Week 1 — Data Cleaning & Preprocessing
Week 2 — EDA & Visualization
Week 3 — SQL Analysis
Week 4 — Power BI Dashboard & Insights
Key Insights
Tech Stack
Repository Structure
Learning Outcomes
Future Enhancements
Author

Overview:

This project follows an end-to-end data analytics pipeline that mirrors a real-world industry workflow:
Understand → Clean → Explore → Analyze → Visualize → Query → Dashboard → Generate Insights
It is structured across four major stages:
Data Cleaning & Preprocessing
Exploratory Data Analysis & Visualization
SQL Data Analysis
Interactive Power BI Dashboard & Insights Report

Objectives:

Analyze a real-world Airbnb dataset end to end
Improve data quality through systematic cleaning and preprocessing
Perform exploratory data analysis to identify patterns and trends
Build clear and purposeful visualizations
Use SQL to answer business-related questions
Create an interactive Power BI dashboard
Present analytical findings through an insights report
Strengthen practical, job-ready data analyst skills

Workflow:

Raw Dataset
     ↓
Data Understanding
     ↓
Data Cleaning & Preprocessing
     ↓
Exploratory Data Analysis
     ↓
Data Visualization
     ↓
SQL Analysis
     ↓
Power BI Dashboard
     ↓
Insights Report
     ↓
Business Insights

Week 1 — Data Cleaning & Preprocessing

Objective: Prepare the raw Airbnb dataset for analysis by identifying and resolving data quality issues.

Tasks Performed

1.Loaded and explored the raw dataset
2.Audited rows, columns, and data types
3.Identified and handled missing values
4.Removed duplicate records
5.Resolved inconsistent and invalid entries
6.Standardized column formats
7.Validated the cleaned data
8.Exported a clean, analysis-ready dataset

Skills Applied: Data Cleaning · Data Preprocessing · Data Validation · Pandas · NumPy

Week 2 — EDA & Visualization

Objective: Explore the cleaned dataset to identify meaningful patterns, relationships, distributions, and trends.

1.Univariate Analysis-
Distribution analysis
Frequency analysis
Statistical summaries

2.Bivariate Analysis-
Category-to-category comparisons
Correlation analysis
Trend identification

Visualizations Built-

#	Visualization	            Question It Answers
1	Price Distribution	      How are listing prices distributed across the market?
2	Room Type Distribution	      Which room types dominate the market?
3	Neighbourhood-wise Listings	Where is Airbnb supply concentrated across NYC?
4	Availability Trends	      How does availability vary across listings?
5	Review Patterns	            How do reviews relate to listing activity?

Skills Applied: Exploratory Data Analysis · Data Visualization · Matplotlib · Seaborn · Insight Generation

Week 3 — SQL Analysis

Objective: Analyze the structured Airbnb dataset using SQL to answer concrete business questions.

Tasks Performed-

1.Built a SQLite database
2.Imported the cleaned dataset into the database
3.Designed analytical SQL queries
4.Applied filtering and aggregation techniques
5.Analyzed listings, pricing, hosts, and availability
6.Saved and documented query outputs

SQL Concepts Used: SELECT · WHERE · ORDER BY · GROUP BY · HAVING · LIMIT · COUNT() · AVG() · MIN() · MAX() · SUM()

Skills Applied: SQL · SQLite · Data Aggregation · Business Question Analysis · Database Management

Week 4 — Power BI Dashboard & Insights

Objective: Transform the analytical findings from the previous weeks into an interactive Power BI dashboard and present the key findings through an insights report.

Tasks Performed-

1.Imported the Airbnb dataset into Power BI
2.Prepared the data for dashboard analysis
3.Created KPI cards to highlight important metrics
4.Built interactive charts and visualizations
5.Added filters and slicers for dynamic exploration
6.Configured dashboard interactions
7.Designed a user-friendly analytical dashboard
8.Saved the completed .pbix Power BI dashboard file
9.Created an insights report based on the dashboard findings
10.Presented project insights in a business-oriented format

Dashboard Components-

The Power BI dashboard focuses on presenting important Airbnb marketplace metrics and patterns, including:

1.Listing performance
2.Pricing patterns
3.Room type distribution
4.Neighbourhood-level trends
5.Availability
6.Review-related metrics
7.Host/listing performance

Dashboard Outcome-

The dashboard presents project insights in an interactive, easy-to-understand format, allowing users to explore Airbnb listing patterns and identify key business trends using filters and visual interactions.

Skills Applied: Power BI · Data Visualization · Dashboard Design · KPI Analysis · Slicers · Interactive Reporting · Business Intelligence · Insight Generation

Key Insights-

The complete analysis generated insights related to:

Distribution of Airbnb listings across NYC neighbourhoods
Supply concentration across different areas
Pricing patterns across room types
Availability patterns across listings
Host performance based on listing activity
Review volume and listing characteristics
Differences in Airbnb offerings across neighbourhoods
Key marketplace patterns presented through the Power BI dashboard

The Power BI dashboard and insights report provide a consolidated view of these findings, making the results easier to interpret for business decision-making.

Tech Stack
Technology	      Purpose
Python	      Core data analysis
Pandas	      Data manipulation & cleaning
NumPy	            Numerical operations
Matplotlib	      Data visualization
Seaborn	      Statistical visualization
SQL	            Structured data analysis
SQLite       	Database management
Power BI	      Interactive dashboard & reporting
Jupyter Notebook	Development environment
VS Code	      Code editing & project management
Git & GitHub	Version control

Repository Structure:

AB_NYC_Data_Analysis/
│
├── .venv/                              # Virtual environment
│
├── dashboard/
│   └── Airbnb_Dashboard.pbix           # Power BI dashboard
│
├── data/
│   ├── AB_NYC_2024.csv                 # Raw Airbnb dataset
│   └── AB_NYC_cleaned.csv              # Cleaned dataset
│
├── images/
│   └── dashboard.png                   # Dashboard screenshot
│
├── notebooks/
│   ├── Week1_Data_Cleaning.ipynb       # Data cleaning & preprocessing
│   ├── Week2_EDA.ipynb                 # Exploratory data analysis
│   ├── Week3_SQL_Analysis.sql          # SQL analysis
│   ├── outputs/                        # SQL query outputs
│   ├── airbnb.db.sqbpro                # SQLite database project
│   ├── sql.queries                     # SQL queries
│   └── SQLite.sql                      # SQLite scripts
│
├── reports/
│   └── Insights_Report.pdf             # Business insights report
│
├── README.md                           # Project documentation
└── requirements.txt                    # Python dependencies

Learning Outcomes-

Through this project, practical experience was gained in:
1.Preparing real-world datasets for analysis
2.Identifying and resolving data quality issues
3.Performing exploratory data analysis
4.Building meaningful, purpose-driven visualizations
5.Writing SQL queries to solve business questions
6.Working with relational databases
7.Designing interactive Power BI dashboards
8.Creating KPI-based reports
9.Using filters and slicers for interactive analysis
10.Translating analytical results into business insights
11.Documenting analytics projects professionally
12.Using GitHub for project and version management

Future Enhancements-

Build more advanced interactive dashboards using Power BI
Add advanced SQL techniques such as CTEs and Window Functions
Perform predictive analysis using Machine Learning
Develop price prediction models
Analyze customer/review sentiment
Automate the complete data analysis workflow
Deploy the analytics dashboard for public/live access
Add real-time or regularly updated Airbnb data

Author-

Tejashwini Puchkuru B.Tech CSE — Artificial Intelligence & Machine Learning Aspiring AI Engineer | Data Analyst

Technical Skills: Python · SQL · Data Analytics · Machine Learning · Data Visualization · Power BI