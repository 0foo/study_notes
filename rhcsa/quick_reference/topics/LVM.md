* Physical volume
    * `pvcreate /dev/sdXn`
    * `pvs`, `pvscan`, `pvdisplay`
    * `pvremove /dev/sdXn`



* Volume group
    * `vgcreate myvg /dev/sdXn`
    * `vgs`, `vgscan`, `vgdisplay`
    * `vgextend`, `vgreduce`
    * `vgextend myvg /dev/sdYn`
    * `vgremove myvg`


* Logical volume
    * `lvcreate -L 10G -n mylv myvg`
    * `lvs`, `lvscan`, `lvdisplay`
    * `lvextend`/`lvreduce` or `lvresize`
    * `lvresize -L [+|-][Size] <vgname>/<lvname>`
    * `lvextend -L +10G /dev/myvg/mylv` + `resize2fs /dev/myvg/mylv`
    * `lvremove /dev/myvg/mylv`
