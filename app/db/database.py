from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:Mo43Cl42!@localhost:5432/attrition_db"

engine = create_engine(DATABASE_URL)