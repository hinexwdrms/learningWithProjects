#time calculator project
def add_time(start, duration, day = 'none'):

    #storing the times in a meaningful way
    start_time, meridium = start.split()
    hour, minute = map(int,start_time.split(':')) #convert the list of hour and minute to int
    time_dict = {
        'hour':hour,
        'minute':minute,
        'meridium':meridium
    }
    
    hours_to_add, minutes_to_add = map(int,duration.split(':'))

    #add hours and minutes
    time_dict['hour'] += hours_to_add
    time_dict['minute'] += minutes_to_add

    #if minutes exceed
    if time_dict['minute']>= 60:
        time_dict['hour']+= time_dict['minute']//60 # // returns the whole number only
        time_dict['minute'] = time_dict['minute'] % 60

    #switch between AM and PM
    day_count= 0
    while time_dict['hour'] >= 12:
        if time_dict['meridium'] == 'AM':
            time_dict['meridium'] = 'PM'
        else:
            time_dict['meridium'] = 'AM' 
            day_count += 1 #next day only if PM --> AM

        time_dict['hour'] -= 12 #one switch in AM/PM --> -12hrs

    #midnight or noon
    if time_dict['hour']==0:
        time_dict['hour']=12

    #calculate the week day if given
    if day.lower()!= 'none':
        days_of_week = ['sunday','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
        current_day_index = days_of_week.index(day.lower())
        final_day_index = (current_day_index + day_count)%7
        final_day = days_of_week[final_day_index].capitalize()
    else:
        final_day = ''

    new_time = f"{time_dict['hour']}:{time_dict['minute']:02d} {time_dict['meridium']}"

    if final_day:
        new_time += f', {final_day}' #add final day if given

    return new_time,day_count


new_time,day_count = add_time('11:55 AM','299:59','Monday')

#output according to day
if day_count > 1:
    print(f'{new_time} ({day_count} days later)')
elif day_count == 1:
    print(f'{new_time} (next day)')
else:
    print(new_time)

