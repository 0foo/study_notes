

**11.** Write shell scripts on server1 that create users and groups according to the following parameters. Ensure all users except cindy use autofs for their profiles:
```
manny:1010:dba_admin,dba_managers,dba_staff
moe:1011:dba_admin,dba_staff
jack:1012:dba_intern,dba_staff
marcia:1013:it_staff,it_managers
jan:1014:dba_admin,dba_staff
cindy:1015:dba_intern,dba_staff
```

#### **Solution to Task 11**
On server1, create a text file called "grouplist.txt" that contains the following:
```
dba_admin:5010
dba_managers:5011
dba_staff:5012
dba_intern:5013
it_staff:5014
it_managers:5015
```
Then create a shell script called "creategroup.sh" that contains the following:\
Note: "IFS" is internal field separator, and will separate the group names from the group IDs.
```
#!/bin/bash

while IFS=":" read group gid ; do
echo "Creating group $group..."
groupadd -g $gid $group
done < grouplist.txt
```
Set the permissions on the file so it's executable, then run it:
```
chmod +x creategroup.sh
./creategroup.sh
```
Now check that the groups were created:
```
egrep "it|dba" /etc/group
```
Now that the groups are created, create a text file called "userlist.txt" that contains the following:\
Note: Remember that "cindy" is being created differently, so needs to be omitted.
```
manny:1010:dba_admin,dba_managers,dba_staff
moe:1011:dba_admin,dba_staff
jack:1012:dba_intern,dba_staff
marcia:1013:it_staff,it_managers
jan:1014:dba_admin,dba_staff
```
Create a shell script called "createuser.sh" that contains the following:\
Note: Here we still use the IFS, and we specify the home path with `-b`, the auxilary groups with `-G` and not to create a home directory with `-M`.
```
#!/bin/bash

while IFS=":" read user uid group ; do
echo "Creating user $user..."
useradd -b /mnt/autofs_home -G $group -u $uid -M $user
done < userlist.txt
```
Set the permissions on the file so it's executable, then run it:
```
chmod +x createuser.sh
./createuser.sh
```
Check to make sure the users were created and added to the appropriate groups:
```
tail /etc/passwd
egrep "it|dba" /etc/group
```
Finally, create "cindy" as a one-off user with a local profile:
```
useradd -u 1015 -G dba_intern,dba_staff cindy
```

**12.** Secure copy the shell scripts to server2 and perform the same functions.

#### **Solution to Task 12**
```
scp create* root@192.168.55.72:/root/
scp *.txt root@192.168.55.72:/root/

### Now on server2:
./creategroup.sh
./createuser.sh
useradd -u 1015 -G dba_intern,dba_staff cindy
```

**13.** Set the password on all of the newly created users to `dbapass`.

#### **Solution to Task 13**
```
### On both servers:

for user in manny moe jack marcia jan cindy; do echo "dbapass" | passwd --stdin $user; done
```

**14.** Create sudo command alias for `MESSAGES` with the command `/bin/tail -f /var/log/messages`

#### **Solution to Task 14**
```
### On both servers:

visudo

### While in visudo, add the following lines:

## Messages
Cmnd_Alias MESSAGES = /bin/tail -f /var/log/messages
```

**15.** Enable superuser privileges according to the following:
```
dba_managers: everything
dba_admin: SOFTWARE, SERVICES, PROCESSES
dba_intern: MESSAGES
```

#### **Solution to Task 15**
```
### On both servers:

visudo

### While in visudo, uncomment the following lines:

Cmnd_Alias SOFTWARE = /bin/rpm, /usr/bin/up2date, /usr/bin/yum
Cmnd_Alias SERVICES = /sbin/service, /sbin/chkconfig, /usr/bin/systemctl start....
Cmnd_Alias PROCESSES = /bin/nice, /bin/kill, /usr/bin/kill, /usr/bin/killall

### Then add the following to the mapping section, after %wheel%:

%dba_managers  ALL=(ALL)       ALL
%dba_admin     ALL = SOFTWARE, SERVICES, PROCESSES
%dba_intern    ALL = MESSAGES
```

**16.** Switch to the various users using `su` and test their privileges.

#### **Solution to Task 16**
```
### manny is a dba_manager, so he should have all rights:
su - manny
sudo -i
### If he can elevate, it works

### moe is a dba_admin, but not a dba_manager:
su - moe
sudo -i (this should fail)
sudo yum install tree (don't confirm, but this should work)

### jack is a dba_intern, but not a dba_admin or dba_manager:
su - jack
sudo -i (this should fail)
sudo yum install tree (this should fail)
sudo tail -f /var/log/messages

### marcia is not a member of any elevated groups:
su - marcia
sudo -i (this should fail)
sudo yum install tree (this should fail)
sudo tail -f /var/log/messages (this should fail)
```




















