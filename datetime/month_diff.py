from datetime import datetime, timedelta

# today
today = datetime.today()
d = datetime(2013, 1, 12)
d = datetime(2022, 1, 12)


def diff_month(d1, d2):
    return (d1.year - d2.year) * 12 + d1.month - d2.month


print(diff_month(today, d))
