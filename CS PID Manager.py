#PID manager program meant to allocate memory process

MIN_PID = 300
MAX_PID = 5000
pids = {}
def allocate_map():
    #creates a dictionary of PIDS that can be used if already created return -1
    keys = range(MIN_PID, (MAX_PID + 1))
    if pids:
        return -1
    for i in keys:
        pids[i] = 0
    return (pids and 1)
def allocate_pids():
    #will give a pids identity for a process if all are used it will return -1
    if not pids:
        return -1
    for i in pids:
        if (pids[i] == 0):
            pids[i] = 1
            return i
    return -1
def release_pid(r):
    #releases the use of a pid identity
    pids[r] = 0
