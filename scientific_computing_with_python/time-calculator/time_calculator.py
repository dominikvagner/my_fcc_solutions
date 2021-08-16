from datetime import datetime, date, timedelta

def add_time(start, duration, day = None):
    format = '%I:%M %p'
    start = datetime.strptime(start, format)
    day_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

    if day != None:
        format = '%I:%M %p, %A'
        day = day.lower().capitalize()   
        start = start + timedelta(days = day_dict[day])

    duration_list = duration.rsplit(':')
    new_time = start + timedelta(hours = int(duration_list[0]), minutes = int(duration_list[1]),)

    day_diff = (new_time.date() - start.date()).days
    
    final = new_time.strftime(format).lstrip('0')
    
    if day_diff > 1:
        final = final + f' ({day_diff} days later)'
    elif day_diff == 1:
        final = final + f' (next day)'

    return final