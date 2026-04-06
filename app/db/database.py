from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL n'est pas définie. Vérifie le fichier .env")

engine = create_engine(DATABASE_URL)