from datetime import datetime

def is_date_valid(val):
    return datetime.strptime(val,"%B %d, %Y %H:%M:%S") if val else False

print(is_date_valid("December 17, 1995 03:24:00"))
