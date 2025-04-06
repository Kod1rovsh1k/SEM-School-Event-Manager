from colorama import init, Fore

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

init(autoreset=True)


class Database:
    engine = create_engine(f'sqlite:///app/backend/database.db', echo=False)
    Session = sessionmaker(bind=engine)
    BASE = declarative_base()

    def get_session(self):
        return self.Session()


def run_back() -> None:
    db = Database()
    try:
        db.BASE.metadata.create_all(db.engine)
        print(f"{Fore.GREEN}[+] {Fore.WHITE}Table was created successfully")
    except Exception as e:
        print(f"{Fore.YELLOW}[i] {Fore.WHITE}Error creating table: {Fore.YELLOW}{e}")
