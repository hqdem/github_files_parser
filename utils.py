from datetime import date, timedelta


def get_date_intervals(start_year=2013, start_month=1, start_day=1, delta_days=14):
    start_inc_date = date(year=start_year, month=start_month, day=start_day)

    dates = []
    while start_inc_date < date.today():
        dates.append((start_inc_date, start_inc_date + timedelta(days=delta_days)))
        start_inc_date += timedelta(days=delta_days)
    return dates
