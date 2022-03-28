from datetime import datetime
import pytz



def get_time(timezone):

    UTC = pytz.utc
    IST = pytz.timezone(timezone)

    display_time = datetime.now(IST)
     
    hours_minutes = display_time.strftime("%H:%M")
    hour = int(display_time.strftime("%H"))

    if hour < 12:
        hours_minutes = hours_minutes + "AM"
    else:
        hours_minutes = hours_minutes + "PM"

    return hours_minutes