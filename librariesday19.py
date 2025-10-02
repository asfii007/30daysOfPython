# Dates & Time
import time
import datetime
import calendar
# Time example

print("Sleeping for 1 second...")
time.sleep(7)
print("Awake again!")

# Datetime example
now = datetime.datetime.now()
print("Current date & time:", now)
print("Formatted date:", now.strftime("%Y-%m-%d %H:%M:%S"))

# Calendar example
print("Calendar for October 2025:")
print(calendar.month(2025, 10))

