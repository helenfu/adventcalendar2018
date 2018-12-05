inputs = []

try:
    while True:
        inputs.append(raw_input())

except EOFError:
    inputs.sort()
    sleep_times = {}
    mins_asleep = {}
    guard = "-1"
    fall_asleep = 0
    for val in inputs:
        date, action = val.split("] ")
        minute = int(date[15:])
        if action == "wakes up":
            for time in range(fall_asleep, minute):
                sleep_times[guard][time] += 1
                mins_asleep[guard] += 1
        elif action == "falls asleep":
            fall_asleep = minute
        else:
            guard = action[7:].split(" ")[0]
            if guard not in sleep_times:
                sleep_times[guard] = [0 for i in range(60)]
            if guard not in mins_asleep:
                mins_asleep[guard] = 0


    time_most_asleep = 0
    most_days_asleep = 0
    most_asleep_guard = "-1"
    for guard in sleep_times:
        for time, days in enumerate(sleep_times[guard]):
            if most_days_asleep < days:
                time_most_asleep = time
                most_days_asleep = days
                most_asleep_guard = guard

    print int(most_asleep_guard) * time_most_asleep