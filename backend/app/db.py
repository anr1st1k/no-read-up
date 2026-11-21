from dotenv import dotenv_values
from pathlib import Path
from sqlalchemy import URL, create_engine
from sqlalchemy.orm import Session

project_root = Path(__file__).resolve().parents[2]
settings = dotenv_values(project_root / ".env")

url = URL.create("postgresql+psycopg",
                 username=settings["POSTGRES_USER"],
                 password=settings["POSTGRES_PASSWORD"],
                 host="127.0.0.1",
                 port=5433,
                 database=settings["POSTGRES_DB"])

eng = create_engine(url)

def get_db():
    with Session(eng) as session:
        yield session


