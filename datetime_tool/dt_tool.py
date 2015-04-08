# Python datetime converter tool

import datetime

def datetimeSqlPython(input, format="%Y-%m-%d %H:%M:%S"):  # Convert Sql string to datetime
    return datetime.datetime.strptime(input, format)

def datetimePythonSql(input, format="%Y-%m-%d %H:%M:%S"):  # Convert datetime to Sql string
    return datetime.datetime.strftime(input, format)

def shiftTimeline(date, conditions): #Shifting date and time - simple way (get params as a dict)

    if 'weeks' in conditions:
        weeks = conditions['weeks']
    else:
        weeks = 0

    if 'days' in conditions:
        days = conditions['days']
    else:
        days = 0

    if 'hours' in conditions:
        hours = conditions['hours']
    else:
        hours = 0

    if 'minutes' in conditions:
        minutes = conditions['minutes']
    else:
        minutes = 0

    if 'seconds' in conditions:
        seconds = conditions['seconds']
    else:
        seconds = 0

    return date + datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)

def timestampNow():   #String output NOW in MySql format
    return datetimePythonSql(datetime.datetime.now())


