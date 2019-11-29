#PID manager program meant to allocate memory process
from threading import Thread
from time import sleep,time
from random import uniform
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
def makeThreads():
    #Creates the htreads for each pid
    threads = []
    for i in range(100):
        thread = Thread(target = AssignPid)
        thread.start()
        threads.append(thread)
    for i in threads:
        i.join()
def AssignPid():
    #assigns the Pid to the thread
    pid = allocate_pids()
    if pid == -1:
        raise RuntimeError("All pids in use")
    sleep(uniform(0,3))
    release_pid(pid)
def main():
    allocate_map()
    ts =  time()#checks start time
    makeThreads()
    tf = time()#checks finish time
    print(tf-ts)#will show how long it took to finish the program

main()
