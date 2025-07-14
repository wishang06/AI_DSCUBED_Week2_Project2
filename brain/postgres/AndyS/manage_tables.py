import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from tabulate import tabulate

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")
engine = create_engine(DATABASE_URL)

def run_ddl():
    with open('brain/postgres/AndyS/DDL/AndyS.sql', 'r') as f:
        ddl = f.read()
    with engine.connect() as conn:
        for statement in ddl.split(';'):
            if statement.strip():
                conn.execute(text(statement))
        conn.commit()

def run_dml():
    with open('brain/postgres/AndyS/DML/AndyS.sql', 'r') as f:
        dml = f.read()
    with engine.connect() as conn:
        for statement in dml.split(';'):
            if statement.strip():
                conn.execute(text(statement))
        conn.commit()

def view_table():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM project_two.Global_Exchange_Universities;"))
        rows = result.fetchall()
        headers = list(result.keys())
        print(tabulate(rows, headers, tablefmt="grid"))

def run_top5_ddl():
    with open('brain/postgres/AndyS/DDL/top_5_universities.sql', 'r') as f:
        ddl = f.read()
    with engine.connect() as conn:
        for statement in ddl.split(';'):
            if statement.strip():
                conn.execute(text(statement))
        conn.commit()

def view_top5():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM project_two.Top_5_Universities;"))
        rows = result.fetchall()
        headers = list(result.keys())
        print(tabulate(rows, headers, tablefmt="grid"))

def run_best_uni_ddl():
    with open('brain/postgres/AndyS/DDL/best_university_per_country.sql', 'r') as f:
        ddl = f.read()
    with engine.connect() as conn:
        for statement in ddl.split(';'):
            if statement.strip():
                conn.execute(text(statement))
        conn.commit()

def view_best_uni():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM project_two.Best_University_Per_Country;"))
        rows = result.fetchall()
        headers = list(result.keys())
        print(tabulate(rows, headers, tablefmt="grid"))

if __name__ == "__main__":
    run_ddl()
    run_dml()
    view_table()
    run_top5_ddl()
    view_top5()
    run_best_uni_ddl()
    view_best_uni()