import datetime

date_and_time = datetime.datetime(2021, 8, 22, 11, 2, 5)

print("Original Time:")
print(date_and_time)

time_change = datetime.timedelta(minutes=75)
new_time = date_and_time + time_change

print(new_time)
