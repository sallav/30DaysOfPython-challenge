from datetime import datetime
from datetime import date
from datetime import timedelta

# Get the current day, month, year, hour, minute and timestamp

now = datetime.now()

day = now.day
month = now.month
year = now.year

hour = now.hour
minute = now.minute

timestamp = now.timestamp()

print("{}.{}.{} {}:{}".format(day, month, year, hour, minute))
print(timestamp)

# Format the current date using this format: "%m/%d/%Y, %H:%M:%S")

today = now.strftime("%m/%d/%Y, %H:%M:%S")
print(today)

# Change string to time

date_string = "27 March 2022"
date_object = datetime.strptime(date_string, "%d %B %Y")

print(date_object)

# Calculate the time difference between now and new year.

new_year = datetime(year=2023, month=1, day=1, hour=0, minute=0, second=0)
difference = new_year - now

print(difference)

tday = date(year=2022, month=3, day=27)
nyear = date(year=2023, month=1, day=1)

diff = nyear - tday

print(diff)

# Calculate the time difference between 1 January 1970 and now.

secs = datetime.now().timestamp()

tdiff = timedelta(seconds=secs)

print(tdiff)
