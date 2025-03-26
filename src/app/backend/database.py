from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


class Database:
    engine = create_engine(f'sqlite:///app/backend/database.db', echo=False)
    Session = sessionmaker(bind=engine)
    BASE = declarative_base()

    def __init__(self):
        self.BASE.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()


def run_back() -> None:
    from .models import User

    db = Database()
    try:
        db.BASE.metadata.create_all(db.engine)
        print("Таблицы успешно созданы!")
    except Exception as e:
        print(f"Ошибка при создании таблиц: {e}")
