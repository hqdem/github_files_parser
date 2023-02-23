from sqlalchemy import Column, Integer, Date, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CreatedIntervals(Base):
    __tablename__ = 'repos_created_intervals'

    id = Column('id', Integer, primary_key=True)
    start_date = Column('start_date', Date)
    end_date = Column('end_date', Date)
    is_completed = Column('is_completed', Boolean, default=False)
