### Essentials/tips
* man nice/renice
* man chrt
* ps -ef or ps aux
* pgrep/pkill
* ps -eO [x] --sort +[x]
* ps u $(pgrep sha1sum)



### Processes
* kill
* ps aux, ps -eF, ps fax (tree)
* `nice -n 19 sleep 50` / `renice -n 10 -p 1` / `ps -eo pid,comm,ni`
* top/htop
* kill / 

* ps aux or ps -eF
    * gives info on all procs with info

* ps -eO ni,cmd,<other commands>

* pgrep/pkill 
    * find/kill a proc by name/regex instead of proc id
    * (both are regex, use pgrep first)

* individual processes use `ps u <process id's>`
    * ps u $(pgrep sha1sum)

### process scheduling
* view current scheduling info: `chrt -p <PID>`
* view max priorities: `chrt --max`
* change scheduling priority: `chrt -p <priority> <PID>`
* change scheduling policy: `chrt [-r|-f|-r|--other|--batch|--idle] `
* can combine:
    * `chrt -r -p 5 1234`

### scheduling policies
* NOTE: all this is in: `man chrt`
* --other: SCHED_OTHER: The default policy for non-real-time tasks.
* -f: SCHED_FIFO: First-In-First-Out real-time policy. 
    * Tasks are executed in the order they become runnable and continue until they are done or preempted by a higher-priority task.
* -r: SCHED_RR: Round-robin real-time policy. 
    * Similar to FIFO but each task has a time quantum, and once it expires, the task is moved to the end of the queue.
* --batch: SCHED_BATCH: Used for CPU-intensive tasks that can afford to wait longer for CPU time.
* --idle: SCHED_IDLE: Used for tasks that only run when no other tasks are running (extremely low priority).


### process priority
* `nice\renice`
* `nice -n 19 sleep 500 &`
* `renice -n 10 -p 1234`

