from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from ..models import CreatedIntervals


class CreatedIntervalsRepository:
    def __init__(self, db_session: Session):
        self._session = db_session

    def fill_db_with_intervals(self, intervals):
        db_intervals = []

        for interval in intervals:
            self._session.add(CreatedIntervals(start_date=interval[0], end_date=interval[1]))
            try:
                self._session.commit()
            except IntegrityError:
                self._session.rollback()
                continue

        self._session.add_all(db_intervals)
        self._session.commit()

    def get_incomplete_intervals(self):
        return self._session.query(CreatedIntervals).where(CreatedIntervals.is_completed == 0).order_by(CreatedIntervals.start_date)
