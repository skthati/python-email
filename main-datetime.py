# datetime module
import datetime as dt


time_now = dt.datetime.now()
year = time_now.year
month = time_now.month
day = time_now.day
hour = time_now.hour
minute = time_now.minute

day_of_the_week = time_now.weekday()

print(day_of_the_week)

print(f"Today year is {year}, month is {month}, day is {day} and time is {hour}:{minute}.")

