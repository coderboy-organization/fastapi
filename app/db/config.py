import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.configs.loadenv import env
env()

DATABASE_URL= os.environ.get("DATABASE_URL")
if not DATABASE_URL:
    print("Please enter DATABASE_URL in .env file")

engine = create_engine(DATABASE_URL)
LocalSession = sessionmaker(bind=engine, autocommit=False,autoflush=False)
Base = declarative_base()
def get_db():
    db = LocalSession()
    try:
        yield db
    except:
        print("Fail to get DB!")
    finally:
        db.close()