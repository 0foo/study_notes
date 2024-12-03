* Search all files in the /var/lib directory that are owned by the chrony user.
* List all files in the /var directory that are owned by root and the group owner is mail.
* List all files in the /usr/bin directory that has a file size greater than 50 KB.
* Search all files in the /home/student directory that have not been changed in the last
120 minutes.
* List all the block device files in the /dev directory.



Page 614
Create a new directory called /home/student/grading.
• Createthreeemptyfilesinthe/home/student/gradingdirectorynamedgrade1, grade2, and grade3.
• Capture the first five lines of the /home/student/bin/manage-files file in the / home/student/grading/manage-files.txt file.
• Append the last three lines of /home/student/bin/manage-files to the file /home/ student/grading/manage-files.txt. You must not overwrite any text already in the file /home/student/grading/manage-files.txt.
• Copy/home/student/grading/manage-files.txtto/home/student/grading/ manage-files-copy.txt.
• Edit the file /home/student/grading/manage-files-copy.txt so that there should be two sequential lines of text reading Test JJ.
• Edit the file /home/student/grading/manage-files-copy.txt so that the Test HH line of text must not exist in the file.
• Edit the file /home/student/grading/manage-files-copy.txt so that the line A new lineshouldexistbetweenthelinereadingTest BBandthelinereadingTest CC.
Create a hard link named /home/student/hardlink to the file /home/student/ grading/grade1. You will need to do this after creating the empty file /home/ student/grading/grade1 as specified above.
• Create a soft link named /home/student/softlink to the file /home/student/ grading/grade2.
• Save the output of a command that lists the contents of the /boot directory to the file /home/student/grading/longlisting.txt. The output should be a “long listing” that includes file permissions, owner and group owner, size, and modification date of each file.



Page 622
• Terminate the process that is currently using the most CPU time.
• Create a new group called database that has the GID 50000.
• Create a new user called dbuser1 that uses the group database as one of its secondary groups. The initial password of dbuser1 should be set to redhat. Configure the user dbuser1 to force a password change on its first login. The user dbuser1 should be able to change its password after 10 days since the day of the password change. The password of dbuser1 should expire in 30 days since the last day of the password change.
• Configure the user dbuser1 to use sudo to run any command as the superuser.
• Configure the user dbuser1 to have a default umask of 007.
• Create a new directory called /home/student/grading/review2 with student and database as its owning user and group respectively. Configure the permissions on that directory so that any new file in it inherits database as its owning group irrespective to the creating user. The permissions on /home/student/grading/review2 should allow the group members of database and the user student to access the directory and create contents in it. All other users should have read and execute permissions on the directory. Also, ensure that users are only allowed to delete files they own from /home/student/ grading/review2 and not files belonging to others.



p 629
• Generate SSH keys for the user student on serverb. Do not protect the private key with a passphrase. The private and public key files should be named /home/student/.ssh/review3_key and /home/student/.ssh/review3_key.pub respectively.
• On servera, configure the user student to accept logins authenticated by the SSH key pair you created for the user student on serverb. The user student on serverb should be able to log in to servera using SSH without entering a password.
• On serverb, configure the sshd service to prevent users from logging in as root via SSH.
• On serverb, configure the sshd service to prevent users from using their passwords to log in. Users should still be able to authenticate logins using an SSH key pair.
• Create a tar archive named /tmp/log.tar containing the contents of /var/log on serverb. Remotely transfer the tar archive to /tmp directory on servera, authenticating as student using the student user’s private key of the SSH key pair.
• Configure the rsyslog service on serverb to log all messages it receives that have the priority level of debug or higher to the file /var/log/grading-debug. This configuration should be set in an /etc/rsyslog.d/grading-debug.conf file, which you need to create.
• Install the zsh package,available in the BaseOS repository,on serverb.
• Enable the default module stream for the module python36 and install all provided
packages from that stream on serverb.
• Set the timezone of serverb to Asia/Kolkata.


P 637
• Determine the name of the Ethernet interface and its active connection profile on serverb.
• On serverb, create a new connection profile called static for the available Ethernet interface that statically sets network settings and does not use DHCP. Use the settings in the following table.
IPv4 address
172.25.250.111
Netmask
255.255.255.0
Gateway
172.25.250.254
DNS server
172.25.250.254

Set the server’s Ethernet interface to use the updated network settings displayed in the table above.
• Ensure that the host name of serverb is statically set to server-review4.lab4.example.com.
• On serverb, set client-review4 as the canonical host name for the IPv4 address 172.25.250.10 of the host servera.lab.example.com.
• Configure the additional IPv4 address 172.25.250.211 with the netmask 255.255.255.0 on the same interface of serverb that has the existing static network settings. Do not remove the existing IPv4 address. Make sure that serverb responds to all addresses when the connection you statically configured on its interface is active.
• On serverb, restore the original network settings by activating the original network connection and deactivating the static network connection you created manually.


p644
Accomplish the following tasks on serverb to complete the exercise.
On serverb, a block device containing the XFS file system exists but is not yet mounted. Determine the block device and mount it on the /review5-disk directory. Create the /review5-disk directory, if necessary.
On serverb, locate the file called review5-path. Create a file named /review5-disk/review5-path.txt that contains a single line consisting of the absolute path to the review5 file.
On serverb, locate all the files having contractor1 and contractor as the owning user and group, respectively. The files must also have the octal permissions of 640. Save the list of these files in /review5-disk/review5-perms.txt.
On serverb, locate all files 100 bytes in size. Save the absolute paths of these files in / review5-disk/review5-size.txt.