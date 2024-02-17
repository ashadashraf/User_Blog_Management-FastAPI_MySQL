from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

URL_DATABASE = 'mysql+pymysql://root:1234@localhost:3306/9xtechnologyapp'

engine = create_engine(URL_DATABASE)


# SQLALCHEMY_DATABASE_URL = 'sqlite:///./blog.db'

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()