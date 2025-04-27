import datetime

start_date = datetime.date(2021, 2, 1)
end_date = datetime.date(2021, 3, 1)

# delta time- diff of one day inbetween
delta = datetime.timedelta(days=1)

while start_date <= end_date:
    print(start_date, end="\n")
    start_date += delta
