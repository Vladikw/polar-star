import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://polar:polar_dev_2026@127.0.0.1:5433/polar"
)
