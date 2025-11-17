def time_string(hours, minutes, time_format):
    time = ""
    if hours < 10:
        hours = f"0{hours}"
    if minutes < 10:
        minutes = f"0{minutes}"
    if time_format == 12:
        ampm = "am"
        if int(hours) >= 12:
            if int(hours) > 12:
                hours = int(hours) - 12
            ampm = "pm"
        elif int(hours) == 0:
            hours = 12
        time = f"{hours}:{minutes}{ampm}"
    if time_format == 24:
        time = f"{hours}:{minutes}"
    return time

hours = int(input("Hours (0-24): "))
minutes = int(input("Minutes (0-60): "))
time_format = int(input("Enter time format (12 or 24): "))

print(time_string(hours, minutes, time_format))