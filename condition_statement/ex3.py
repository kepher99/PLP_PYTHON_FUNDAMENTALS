import datetime

weekend = ["saturday", "sunday"]

# Get the current day of the week
current_day = datetime.datetime.now().strftime("%A").lower()

if current_day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("Wake up at 6:00")
else:
    print("Sleep in")
