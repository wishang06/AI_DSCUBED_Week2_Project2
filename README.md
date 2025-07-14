# Table for Global Exchange Universities (AndyS)

Built with PostgreSQL and Python, this project presents a structured database of top global universities, demonstrating data engineering techniques such as data modeling, querying, and presentation.

## Overview

- **Main Table:** `project_two.Global_Exchange_Universities` — Contains information about top global universities, including their QS rankings and website links.
- **Bonus Tables:**
  - `project_two.Top_5_Universities` — The top 5 universities by overall QS rank.
  - `project_two.Best_University_Per_Country` — The best-ranked university in each country.

## Folder Structure

```
brain/postgres/AndyS/
├── DDL/
│   ├── AndyS.sql                      # DDL for main table
│   ├── top_5_universities.sql         # DDL for Top 5 table
│   └── best_university_per_country.sql# DDL for Best per Country table
├── DML/
│   └── AndyS.sql                      # DML for main table
├── view_main_table.py                 # View the main table
├── view_top5.py                       # View the Top 5 table
├── view_best_uni.py                   # View the Best per Country table
└── README.md                          # This file
```

## Setup

1. **Install dependencies:**
   - Python 3.8+
   - Install required packages:
     ```sh
     pip install sqlalchemy psycopg2-binary python-dotenv tabulate
     ```
2. **Configure your database connection:**
   - Create a `.env` file in the project root (or in this folder) with:
     ```
     DATABASE_URL=postgresql://username:password@host:port/dbname
     ```

3. **Create and populate the tables:**
   - Use the provided DDL and DML scripts to create and populate the main table. You can use a script like the original `manage_table.py` or run the SQL manually.
   - To create the bonus tables, run the DDL scripts in `DDL/top_5_universities.sql` and `DDL/best_university_per_country.sql` after the main table is populated.

## Viewing the Tables

Run the following scripts to view each table in a formatted grid:

- **Main Table:**
  ```sh
  python brain/postgres/AndyS/view_main_table.py
  ```
- **Top 5 Universities:**
  ```sh
  python brain/postgres/AndyS/view_top5.py
  ```
- **Best University Per Country:**
  ```sh
  python brain/postgres/AndyS/view_best_uni.py
  ```

Each script will print the corresponding table in a readable format using `tabulate`.