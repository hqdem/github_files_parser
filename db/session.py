from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from config import Config

engine = create_engine(Config.db_uri, echo=False)
session = Session(bind=engine)
