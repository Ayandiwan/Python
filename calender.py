import calendar

# Create a text calendar
cal = calendar.TextCalendar(calendar.SUNDAY)

# Get year and month input from user
year = int(input("Enter year (e.g., 2025): "))
month = int(input("Enter month (1-12): "))

# Display the calendar for the given month
print("\n" + cal.formatmonth(year, month))
