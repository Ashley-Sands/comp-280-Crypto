def time_and_units(t_time):
    t_time_units = "Secs"

    if t_time > 60:
        t_time /= 60
        t_time_units = "Mins"

    if t_time > 60:
        t_time /= 60
        t_time_units = "Hours"

    if t_time > 24:
        t_time /= 24
        t_time_units = "Days"

    if t_time > 7:
        t_time /= 7
        t_time_units = "Weeks"

    if t_time > 52.1429:
        t_time /= 52.1429
        t_time_units = "Years"

    if t_time > 10:
        t_time /= 10
        t_time_units = "Decades"

    if t_time > 10:
        t_time /= 10
        t_time_units = "Centurys"

    if t_time > 10:
        t_time /= 10
        t_time_units = "Millenniums"

    return (t_time, t_time_units)