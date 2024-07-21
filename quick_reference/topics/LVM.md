* Physical volume
    * `pvcreate /dev/sdXn`
    * `pvs`
    * `pvdisplay`
    * `pvremove /dev/sdXn`


* Volume group
    * `vgcreate myvg /dev/sdXn`
    * `vgs`
    * `vgdisplay`
    * `vgextend myvg /dev/sdYn`
    * `vgremove myvg`


* Logical volume
    * `lvcreate -L 10G -n mylv myvg`
    * `lvs`
    * `lvextend -L +10G /dev/myvg/mylv` + `resize2fs /dev/myvg/mylv`
    * `lvremove /dev/myvg/mylv`
