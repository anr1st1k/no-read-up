from sqlalchemy import text
from backend.app.db import eng

with eng.connect() as connection:
    result = connection.execute(text("SELECT 1")).scalar_one()

print(result)
