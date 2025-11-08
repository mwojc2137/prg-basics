time = input("Enter time 24-hour, (hh:mm): ")

time = time.split(":")

hour = int(time[0])

minute = int(time[1])

time_of_day = "am"

if minute >= 60 or hour >= 24:
    print("No such hour exists, you fool!")
else:
    if hour >= 12:
        time_of_day = "pm"
    if hour > 12:
        hour -= 12
    print(f"Time in 12-hour format: {hour}:{minute}{time_of_day}")