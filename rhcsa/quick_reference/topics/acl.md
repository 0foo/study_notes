### View
* `getfacl filename`

### Set/Remove
* `setfacl -m u:username:rw- filename`
* `setfacl -m g:groupname:r-- filename`
* `setfacl -m o::--- filename`
* `setfacl -m m::rwx filename`
* `setfacl -x u:username filename`
* `setfacl -b filename`
* `setfacl -R -m u:username:rwx directory`


## Default
* `setfacl -d -m u:username:rwx directory`
* `setfacl -d -m g:groupname:rx directory`


### Examples
* `setfacl -m u:alice:rw- example.txt`
* `setfacl -m g:developers:r-- project`
* `setfacl -x u:alice example.txt`
* `setfacl -d -m u:alice:rwx /shared`
* `setfacl -R -m g:developers:rx /project`
* `setfacl -b example.txt`
* `setfacl -m m::rwx example.txt`



