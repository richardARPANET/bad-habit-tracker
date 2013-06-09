from django.utils import timezone
import datetime


def timesince(date_time):
    now = timezone.now()
    diff = now - date_time

    output = str()
    #tuple of date diff
    dateinfo = weeks_days_hours_minutes(diff)

    if dateinfo[0] > 0:
        output += ' {0} week'.format(dateinfo[0])
        #append s if required
        output += 's' if dateinfo[0] is not 1 else ''
    if dateinfo[1] > 0 and dateinfo[1] - (dateinfo[0] * 7):
        if dateinfo[0] > 0:
            num = dateinfo[1] - (dateinfo[0] * 7)
        else:
            num = dateinfo[1]

        output += ' {0} day'.format(num)
        output += 's' if dateinfo[1] is not 1 else ''
    if dateinfo[2] > 0:
        output += ' {0} hour'.format(dateinfo[2])
        output += 's' if dateinfo[2] is not 1 else ''
    if dateinfo[3] > 0:
        output += ' {0} minute'.format(dateinfo[3])
        output += 's' if dateinfo[3] is not 1 else ''
    return output


def weeks_days_hours_minutes(td):
    return td.days/7, td.days, td.seconds//3600, (td.seconds//60) % 60
