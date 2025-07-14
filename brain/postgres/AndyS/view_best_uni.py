import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from tabulate import tabulate

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in the environment variables")
engine = create_engine(DATABASE_URL)

def view_best_uni():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM project_two.Best_University_Per_Country;"))
        rows = result.fetchall()
        headers = list(result.keys())
        print(tabulate(rows, headers, tablefmt="grid"))

if __name__ == "__main__":
    view_best_uni() 