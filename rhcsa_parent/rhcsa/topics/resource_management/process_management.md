## Procs vs Threads

* procs is concurrency between applications/commands
    * typically managed within the OS
    * fork()
* threads are inter process concurrency
    * threads share address space, file handles, etc.
    * basically threads share everythin within a process
    * typically managed within the applicaiton
    * clone() or pthreads
    * a single CPU will service a thread
    * no linux tool available to manage threads(they are managed within the command)

## types of processes

1. shell jobs
1. daemons
1. kernel processes


### Shell jobs
* process spun up from within a shell
* any command run from the shell
* child of the shell
* alias: interactive process

* foreground job
    * blocks terminal until completed
* background job
    * send to background with & flag
    * sends a job to background


#### Working with shell jobs
* start a command with & symbol to send it to background to allow use of terminal
* without & symbol will be a foreground(fg)job and will have to wait until finishes to use terminal again
* all procs/jobs started from a terminal are children to that terminal process

* `cntrl + Z`
    * Use Ctrl+Z to suspend a running foreground job. 
    * This will stop the job and return control to the shell, displaying a job number.

* `bg`
    * If you have a job that is currently stopped or running in the foreground and you want to move it to the background, you can use the `bg` command.
    * Use bg followed by the job number to resume the suspended job BUT in the background.
    * bg <jobs id>

* `fg`
    * To bring a background job to the foreground, use the `fg` command followed by the job number.
    * if no job number passed the default is to send send last background job started to the foreground
    * use the job id from `jobs` command to pull a specific bg job to the foreground

* Job Numbers and Percent Sign (%)
    * The job number is prefixed with a percent sign (%). For example, %1 refers to job number 1.
    * The most recent job can be referred to as %% or %+.
    * The previous job can be referred to as %-.

* can decouple a process from a shell with: `nohup <somecommand> &`
    * this decouples from terminal and makes the process an orphan
    * either process 1 (init) or a user specific systemd process will adopt the orphan
        * [/topics/boot/3-systemd.md](systemd)

### Daemons
* processes that provide services

### Kernel processes
* spun up by the kernel
* in ps aux will have brackets around them
* cannot be managed by administrators with standard tools

### Change Process priority
* two concepts: priority/scheduling policy

* process by default start with policy of SCHED_OTHER
* this is the standard type of policy for normal processes that share the CPUs
* if you need real time processing can change the scheduling policy(see below)
    * SCHED_FIFO
    * SCHED_RR
* you can set prioirty of real time processing via the chrt command
* for SCHED_OTHER you set priority using the nice command

### Process Schedule Policy
* They're basically the same
    * both give the process uninterruptable access to the CPU

* Round Robin will share CPU amongst equal priority process whereas FIFO will monopolize the CPU


* SCHED_FIFO (First-In, First-Out)

    * Characteristics:
        * Priority-Based: Processes are scheduled strictly based on their priority. Higher priority processes always preempt lower priority ones.
        * Non-Preemptive: Once a process starts running, it will continue to run until it either voluntarily yields the CPU, is blocked (e.g., waiting for I/O), or is preempted by a higher priority process.
        * No Time Slicing: There is no time slicing among processes with the same priority. If a process does not yield the CPU, it can monopolize it, potentially causing starvation of lower priority processes.

    * Use Cases:
        * Suitable for tasks that require uninterrupted execution until completion or voluntary yielding.
        * Ideal for real-time applications where tasks need to run to completion once started, such as data acquisition systems.

* SCHED_RR (Round-Robin)

    * Characteristics:
        * Priority-Based: Similar to SCHED_FIFO, processes are scheduled based on priority. Higher priority processes preempt lower priority ones.
        * Preemptive with Time Slicing: Among processes with the same priority, the scheduler uses a round-robin mechanism, giving each process a fixed time slice (quantum) to run.
        * Fair CPU Distribution: Ensures that all processes with the same priority get a fair share of CPU time, preventing any single process from monopolizing the CPU.

    * Use Cases:
        * Suitable for real-time applications that require guaranteed CPU time while also ensuring that no single process can monopolize the CPU.
        * Ideal for tasks that need periodic execution, such as multimedia processing or periodic polling tasks.


### chrt
* priority is 0-99
* default is 0
* use -r for RR and -f for FIFO
* start a process with an RR policy (use -f instead of -r for FIFO policy)
    * chrt -r <priority> <command>


* change a running process to a certain policy
    * chrt -r -p 5 1234
    * chrt -f -p 10 1234



### Nice 
* priority is -20 to 19
* default is 0
* `nice\renice`
* `nice -n 19 sleep 500 &`
* `renice -n 10 -p 1234`
* can adjust proc priority
* The priority is specified using a "niceness" value, which ranges from -20 (highest priority) to 19 (lowest priority). 
* The default niceness value is 0.
* default niceness is 0 which equals priority value of 20
* the lower the niceness the higher priority
* note: increasing priority of one proc will take time away from other procs
* for normal processes PR (priority) = 20 + NI (NI is nice and ranges from -20 to 19)





### List/Search Processes
* ps
    * default ps command only show procs started by current user
    * ps -ef 
        * shows ALL processes, plus much info about them, including parent, etc.
    * ps aux
        * show short summary of all process information
        * shows resource usage as well
    * ps -efo pid,comm,ni,pri
        * o: output specific columns
    * sort ps aux by column
        * `ps aux --sort=-%mem`
        * the minus sign(-) means most at the top
    * ps fax
        * shows a tree of proc's with parent child relationships
* pgrep
    * can grep search process list
    * default output is just the process ID
    * can use extended regex by default with this command
    * do not need to input an exact match, will use partial strings and regex as well to search
    * default just searches process name, but can pass -f to search the entire command string
    * always quote
    - `-l` (or `--list-name`): List the process ID and the process name.
    - `-a` (or `--list-full`): List the process ID and the full command line.
    - `-u` (or `--euid`): Match processes by effective user ID.
    - `-U` (or `--uid`): Match processes by real user ID.
    - `-g` (or `--pgroup`): Match processes by process group ID.
    - `-P` (or `--parent`): Match processes by parent process ID.
    - `-d` (or `--delimiter`): Use the specified delimiter in output (default is a newline).
    - `-f` (or `--full`): Match against the full command line.
    - `-n` (or `--newest`): Return only the newest matching process.
    - `-o` (or `--oldest`): Return only the oldest matching process.


* pidof <command>
    * returns the process id of command 


* top/htop
    * n: can change nice value
    * k: send signal to a process
        * prompts for a PID, then a signal to send
    * r: renice running process
        * prompts for a PID, then niceness level


### Kill Processes
* kill
    * send a signal to a process
    * view all signals with: 
        * man 7 signal
        * kill -l
    * SIGTERM (15) is the default signal sent if not specified
    * kill -9
        * the uber process killer: will kill no matter what
        * it's a good idea to send a -15 first before trying -9
    * kill -STOP 12345
        * STOP signal just pauses job
    * kill -CONT PID
        * CONT signal continues
    * list all paused procs
        * `ps aux | grep ' T '`

* pkill
    * pkill -15 firefox
    * corresponds with pgrep in searching processes to kill, so use pgrep first to validate what you're about to kill
    * can kill process with exact name using regex: pkill '^somecommand$'
    
* killall
    * kills all procs with the same name
    * have to match name exactly unlike with pkill which used regex matching



### Other commands
* uptime
    * shows uptime and load average
    * load average
        * load average: number of procs that are in runnable(waiting to be scheduled) or blocking state(waiting for I/O)
        * can be viewed via top command or via uptime command




### Practice





### 
jobs
fg
bg <jobs id>
bg
cntrl + C
nohup <somecommand> &
nice
renice
nice -n 19 sleep 500 &
renice -n 10 -p 1234
ps
ps -ef
ps -o pid,ppid,cmd
ps aux
ps fax
pgrep
pidof <command>
top
htop
man 7 signal
kill -l
kill
kill -9
pkill
pkill -15 firefox
pkill '^somecommand$'
killall
uptime