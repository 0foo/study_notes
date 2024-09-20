### Processes
* kill
* ps aux, ps -ef, ps fax (tree)
* `nice -n 19 sleep 50` / `renice -n 10 -p 1` / `ps -eo pid,comm,ni`
* pgrep/pkill (both are regex, use pgrep first)
* top/htop
* kill / 

### process priority
* chrt -r <priority> <command>
* chrt -r -p 5 1234
* `nice\renice`
* `nice -n 19 sleep 500 &`
* `renice -n 10 -p 1234`

