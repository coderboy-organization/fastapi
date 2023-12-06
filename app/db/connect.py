from app.db.config import Base, engine

def db_connect():
    try:
        Base.metadata.create_all(bind=engine)
        print("🎉 DB connection successfull!")
    except Exception as err:
        print("Fail to connect!")
        print(err)
