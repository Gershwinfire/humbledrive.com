from get_time import get_time
import pytz

alltimezones = pytz.all_timezones

for time in alltimezones:
    print(time)

##ASK FOR TIMEZONE DESIRED:
timezone = input("DESIRED TIME ZONE: ")

wanted_time = get_time(timezone)

print(wanted_time)