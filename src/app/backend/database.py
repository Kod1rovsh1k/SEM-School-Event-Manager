from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from django.conf import settings

class Database:
    def __init__(self):
        db_name = settings.DATABASES['default']['NAME']
        self.engine = create_engine(f'sqlite:///{db_name}', echo=False)
        self.Session = sessionmaker(bind=self.engine)
        self.BASE = declarative_base()
        self.BASE.metadata.create_all(self.engine)

    def get_session(self):
        return self.Session()