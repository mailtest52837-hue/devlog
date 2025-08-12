from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "postgresql://devlogdb_2umy_user:zC8l3ifKGOxOunJBbhaNAvYKhlQnTZPz@dpg-d2d9on3e5dus73fogkr0-a.oregon-postgres.render.com/devlogdb_2umy"

engine = create_engine(DATABASE_URL)

Base = declarative_base()

SessionLocal = sessionmaker(bind = engine)
