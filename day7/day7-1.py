from sets import Set

prereq_index = len('Step ')
dep_index = len('Step _ must be finished before step ')

prereq_to_dep = {}
dep_to_prereq = {}
ready = set()

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
    ans = ""
    while True:
        roots = get_roots()
        ready = ready.union(roots)
        ready_list = list(ready)
        ready_list.sort()
        next = ready_list[0]
        ready.remove(next)
        ans += next

        if len(prereq_to_dep) == 0:
            break

        deps = list(prereq_to_dep[next])
        for dep in deps:
            if len(dep_to_prereq[dep]) > 1:
                dep_to_prereq[dep].remove(next)
            else:
                ready.add(dep)
                del dep_to_prereq[dep]
        del prereq_to_dep[next]

    print ans
