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
* jobs: see all background jobs with this command
* fg
    * default send send last background job started to the foreground
    * use the job id from jobs command to pull a specific bg job to the foreground
* bg <jobs id>
    * can start a job in the background from paused state
* a long running job
    *  can pause with ctrl + Z .... 
    * then type bg will start it and send to background
* cntrl + C
    * will cancel a job

* any forground jobs are terminated when shell is closed
* any background jobs are not terminated and stay in the process list


### Daemons
* processes that provide services


### Kernel processes
* spun up by the kernel
* in ps aux will have brackets around them
* cannot be managed by administrators with standard tools




### Commands
* ps
    * default ps command only show procs started by current user
    * ps -ef 
        * shows the command used to start the process
    * ps aux
        * show short summary of all process information
    * ps fax
        * shows a tree of proc's with parent child relationships
* pgrep
    * can grep search process list

* nice/renice
    * can adjust proc priority
    * linux priority 
        * higher priority wins
        * is a dynamic number that is reduced by the proc scheduler over time the more CPU it has taken 
        * at some point priority gets low enough the proc will be popped off the cpu and a new proc placed onto the core
        * nice basically adds a constant to this to make it end early and have less CPU time or a negative to give it more CPU time
    * ranges from niceness values of: -20 to 19
    * default niceness is 0 which equals priority value of 20
    * the lower the niceness the higher priority
    * nice start the proc with certain priority
        nice -n 19 sleep 500 &
    * renice adjust running proc priority
        * renice -n 10 -p 1234
    * note: increasing priority of one proc will take time away from other procs
* for normal processes PR (priority) = 20 + NI (NI is nice and ranges from -20 to 19)

* pidof <command>
    * returns the process id of command 
    * 
* top
    * r: change priority of proc
    * n: can change nice alue

* kill
    * SIGTERM (15) is the default signal sent if not specified
    * send a signal to a process
    * view all signals with: 
        * man 7 signal
        * kill -l
    * kill -9
        * the uber process killer: will kill no matter what
* pkill
    * pkill -15 firefox
    * corresponds with pgrep in searching processes to kill, so use pgrep first to validate what you're about to kill
    * can kill process with exact name using regex: pkill '^somecommand$'
* killall
    * kills all procs with the same name
    * have to match name exactly unlike with pkill which used regex matching

* top/htop
    * k: send signal to a process
        * prompts for a PID, then a signal to send
    * r: renice running process
        * prompts for a PID, then niceness level
* uptime
    * shows uptime and load average

 * load average
    * load average: number of procs that are in runnable(waiting to be scheduled) or blocking state(waiting for I/O)
    * can be viewed via top command or via uptime command

* lscpu
    * show proc/core hardware info
    * can view the number of cores in system

* tuned/tuned-adm
    * can set different profiles for a system
    * this will optimize performance for that system type