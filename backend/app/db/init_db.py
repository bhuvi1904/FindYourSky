from app.db.session import engine, Base, SessionLocal
from app.models.entities import *
from app.ingestion.seed_data import seed_database

def init_db(force: bool = False):
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        res = seed_database(db, force=force)
        print("Database initialized and seeded:", res)
    finally:
        db.close()

if __name__ == "__main__":
    init_db(force=True)
