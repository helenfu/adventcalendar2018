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

    most_mins_asleep = 0
    guard_most_asleep = ""
    for guard, time in mins_asleep.iteritems():
        if most_mins_asleep < time:
            most_mins_asleep = time
            guard_most_asleep = guard

    time_most_asleep = 0
    most_days_asleep = 0
    for time, days in enumerate(sleep_times[guard_most_asleep]):
        if most_days_asleep < days:
            time_most_asleep = time
            most_days_asleep = days

    print int(guard_most_asleep) * time_most_asleep