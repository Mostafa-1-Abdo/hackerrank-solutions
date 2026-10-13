def convert_time_to_24hour_format(time_12hour_format: str) -> str:
    hour = int(time_12hour_format[:2])
    period = time_12hour_format[-2:]

    if period == "AM" and hour == 12:
        hour = 0

    elif period == "PM" and hour != 12:
        hour += 12

    return str(hour).zfill(2) + time_12hour_format[2:-2]


time_12hour_format = input()
print(convert_time_to_24hour_format(time_12hour_format))
