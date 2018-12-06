from sets import Set

prereq_index = len('Step ')
dep_index = len('Step _ must be finished before step ')

offset_time = 60
worker_count = 5

prereq_to_dep = {}
dep_to_prereq = {}
ready = set()
worker_time_left = [0 for _ in range(worker_count)]
not_working = '-'
working_on = [not_working for _ in range(worker_count)]

def get_char_val(char):
  return ord(char) - ord('A') + 1

def get_step_time(step):
  return get_char_val(step) + offset_time

def get_roots():
    prereqs = Set(prereq_to_dep.keys())
    deps = Set(dep_to_prereq.keys())
    return prereqs.difference(deps)

try:
    while True:
        input = raw_input()
        prereq = input[prereq_index]
        dependency = input[dep_index]
        if prereq in prereq_to_dep:
            prereq_to_dep[prereq].add(dependency)
        else:
            prereq_to_dep[prereq] = Set(dependency)

        if dependency in dep_to_prereq:
            dep_to_prereq[dependency].add(prereq)
        else:
            dep_to_prereq[dependency] = Set(prereq)

except EOFError:
    ready = get_roots()
    time = 0
    done_list = []

    while True:
        for worker in range(worker_count):
            if worker_time_left[worker] > 0:
                worker_time_left[worker] -= 1
            if worker_time_left[worker] == 0 and working_on[worker] != not_working:
                new_done = working_on[worker]
                working_on[worker] = not_working
                done_list.append(new_done)
                # print "{} worker {} finished {}".format(time, worker, new_done)

        for done_step in done_list:
            if done_step in prereq_to_dep:
                deps = list(prereq_to_dep[done_step])
                for dep in deps:
                    if len(dep_to_prereq[dep]) > 1:
                        dep_to_prereq[dep].remove(done_step)
                    else:
                        ready.add(dep)
                        del dep_to_prereq[dep]
                del prereq_to_dep[done_step]

        done_list = []

        ready_list = list(ready)
        ready_list.sort()

        for worker in range(worker_count):
            if worker_time_left[worker] == 0 and len(ready_list) and working_on[worker] == not_working:
                next = ready_list[0]
                ready_list = ready_list[1:]
                ready.remove(next)
                working_on[worker] = next
                worker_time_left[worker] = get_step_time(next)
                # print "{} worker {} starts on {}".format(time, worker, next)

        # print str(time) + " " + " ".join(working_on)
        if len(prereq_to_dep) == 0 and sum(worker_time_left) == 0:
            break
        time += 1
    print time
