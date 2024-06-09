## Memory manamgement


Total Memory: The sum of all physical RAM.
Used Memory: Memory currently used by processes.
Free Memory: Unused memory.
Shared Memory: Memory used by multiple processes.
Buffers/Cached Memory: Memory used by the kernel to cache data.
Swap Usage: The amount of swap space in use.


### Commands

#### System Wide Memory
* `free -h`
* `cat /proc/meminfo`


#### Per process Memory
* `ps aux --sort=-%mem`
* `top/htop`



### Monitoring and Optimization
* Monitoring Memory Usage:
    * Regularly check memory usage using tools like free, vmstat, top, and htop.
    * Monitor swap usage to ensure it's not excessively used, which can indicate insufficient RAM.

* Managing Swap Space:
    * Ensure swap space is configured properly. Typically, swap should be 1-2 times the size of RAM.
    * Add swap space using a swap file or partition if necessary.

* Optimizing Application Memory Usage:
    * Identify memory-hogging applications using top, ps, or smem.
    * Tune application configurations to optimize memory usage.
    * Consider using tools like cgroups to limit memory usage for specific processes.

* Clearing Cache and Buffers:
    * Sometimes, you might need to free up cache and buffer memory manually.
    * `echo 3 > /proc/sys/vm/drop_caches`

* Kernel Parameters:
    * Adjust kernel parameters related to memory management via /proc/sys/vm.
    * Parameters like swappiness, dirty_ratio, and vfs_cache_pressure can be tuned to optimize memory performance.