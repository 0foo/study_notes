
**27.** Fix the web server on server1 and make sure all files are accessible. Do not make any changes to the web server configuration files. Ensure it's accessible from server2 and the client browser.

#### **Solution to Task 27**
Ok, this is a long one. First, we need to check the web server and see what's going on:
```
systemctl status httpd
```
We see something similar to the following:
```
× httpd.service - The Apache HTTP Server
     Loaded: loaded (/usr/lib/systemd/system/httpd.service; enabled; vendor preset: disabled)
     Active: failed (Result: exit-code) since Wed 2023-02-08 14:03:47 CET; 7s ago
       Docs: man:httpd.service(8)
    Process: 2935 ExecStart=/usr/sbin/httpd $OPTIONS -DFOREGROUND (code=exited, status=1/FAILURE)
   Main PID: 2935 (code=exited, status=1/FAILURE)
     Status: "Reading configuration..."
        CPU: 37ms

Feb 08 14:03:47 rhcsa9-server1 systemd[1]: Starting The Apache HTTP Server...
Feb 08 14:03:47 rhcsa9-server1 httpd[2935]: AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using fe80::a00:2>
Feb 08 14:03:47 rhcsa9-server1 httpd[2935]: (13)Permission denied: AH00072: make_sock: could not bind to address [::]:85
Feb 08 14:03:47 rhcsa9-server1 httpd[2935]: (13)Permission denied: AH00072: make_sock: could not bind to address 0.0.0.0:85
Feb 08 14:03:47 rhcsa9-server1 httpd[2935]: no listening sockets available, shutting down
Feb 08 14:03:47 rhcsa9-server1 httpd[2935]: AH00015: Unable to open logs
Feb 08 14:03:47 rhcsa9-server1 systemd[1]: httpd.service: Main process exited, code=exited, status=1/FAILURE
Feb 08 14:03:47 rhcsa9-server1 systemd[1]: httpd.service: Failed with result 'exit-code'.
Feb 08 14:03:47 rhcsa9-server1 systemd[1]: Failed to start The Apache HTTP Server.
```
Ok, we can see here that the it had `(13)Permission denied`, and could not bind to port 85. So, we know the webserver is on port 85, and it's having a permissions issue. Port 85 is a reserved port, and SELinux isn't going to let us bind to that port. Let's get some tools installed to troubleshoot:
```
dnf install -y policycore* setrouble*
```
Now that we have our tools installed, let's try to start it again and see what our logs tell us:
```
systemctl start httpd
grep httpd /var/log/messages
```
Oh man, look at all that gold...
```
Feb  8 14:03:47 rhcsa9-server1 httpd[2935]: AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using fe80::a00:27ff:fe6b:9f4a%enp0s3. Set the 'ServerName' directive globally to suppress this message
Feb  8 14:03:47 rhcsa9-server1 httpd[2935]: (13)Permission denied: AH00072: make_sock: could not bind to address [::]:85
Feb  8 14:03:47 rhcsa9-server1 httpd[2935]: (13)Permission denied: AH00072: make_sock: could not bind to address 0.0.0.0:85
Feb  8 14:03:47 rhcsa9-server1 httpd[2935]: no listening sockets available, shutting down
Feb  8 14:03:47 rhcsa9-server1 httpd[2935]: AH00015: Unable to open logs
Feb  8 14:03:47 rhcsa9-server1 systemd[1]: httpd.service: Main process exited, code=exited, status=1/FAILURE
Feb  8 14:03:47 rhcsa9-server1 systemd[1]: httpd.service: Failed with result 'exit-code'.
Feb  8 14:03:50 rhcsa9-server1 setroubleshoot[2936]: SELinux is preventing /usr/sbin/httpd from name_bind access on the tcp_socket port 85. For complete SELinux messages run: sealert -l d28fbbf2-b7c7-4a6d-a677-7b498dc14c8c
Feb  8 14:03:50 rhcsa9-server1 setroubleshoot[2936]: SELinux is preventing /usr/sbin/httpd from name_bind access on the tcp_socket port 85.#012#012*****  Plugin bind_ports (99.5 confidence) suggests   ************************#012#012If you want to allow /usr/sbin/httpd to bind to network port 85#012Then you need to modify the port type.#012Do#012# semanage port -a -t PORT_TYPE -p tcp 85#012    where PORT_TYPE is one of the following: http_cache_port_t, http_port_t, jboss_management_port_t, jboss_messaging_port_t, ntop_port_t, puppet_port_t.#012#012*****  Plugin catchall (1.49 confidence) suggests   **************************#012#012If you believe that httpd should be allowed name_bind access on the port 85 tcp_socket by default.#012Then you should report this as a bug.#012You can generate a local policy module to allow this access.#012Do#012allow this access for now by executing:#012# ausearch -c 'httpd' --raw | audit2allow -M my-httpd#012# semodule -X 300 -i my-httpd.pp#012
Feb  8 14:03:52 rhcsa9-server1 setroubleshoot[2936]: SELinux is preventing /usr/sbin/httpd from name_bind access on the tcp_socket port 85. For complete SELinux messages run: sealert -l d28fbbf2-b7c7-4a6d-a677-7b498dc14c8c
Feb  8 14:03:52 rhcsa9-server1 setroubleshoot[2936]: SELinux is preventing /usr/sbin/httpd from name_bind access on the tcp_socket port 85.#012#012*****  Plugin bind_ports (99.5 confidence) suggests   ************************#012#012If you want to allow /usr/sbin/httpd to bind to network port 85#012Then you need to modify the port type.#012Do#012# semanage port -a -t PORT_TYPE -p tcp 85#012    where PORT_TYPE is one of the following: http_cache_port_t, http_port_t, jboss_management_port_t, jboss_messaging_port_t, ntop_port_t, puppet_port_t.#012#012*****  Plugin catchall (1.49 confidence) suggests   **************************#012#012If you believe that httpd should be allowed name_bind access on the port 85 tcp_socket by default.#012Then you should report this as a bug.#012You can generate a local policy module to allow this access.#012Do#012allow this access for now by executing:#012# ausearch -c 'httpd' --raw | audit2allow -M my-httpd#012# semodule -X 300 -i my-httpd.pp#012
```
If we read through all of that, we can see a couple of things going on there. First, it tells us that SELinux is preventing httpd from binding to the port, and then tells us if we want even more detail, we can run `sealert -l d28fbbf2-b7c7-4a6d-a677-7b498dc14c8c`. We don't need to do that, since there's enough info to get going with. Looking further down, it gives us a couple of suggestions on how to fix it. First, we can change the port type by running `semanage port -a -t PORT_TYPE -p tcp 85` and specifying the port type, *OR...* we can create a custom policy by running `ausearch -c 'httpd' --raw | audit2allow -M my-httpd` and then follow it with `semodule -X 300 -i my-httpd.pp`. We're going to choose the latter:
```
ausearch -c 'httpd' --raw | audit2allow -M my-httpd
semodule -X 300 -i my-httpd.pp
```
Now try starting the service again:
```
systemctl start httpd
```
Alright! It works!

Next, we're going to check the files locally:
```
ls -la /var/www/html

total 12
drwxr-xr-x. 3 root root  57 Feb  7 10:46 .
drwxr-xr-x. 4 root root  33 Feb  1 08:40 ..
-rw-r--r--. 1 root root  18 Feb  1 08:42 file1
-rw-r--r--. 1 root root 168 Feb  1 08:43 file2
-rw-r--r--. 1 root root  32 Feb  1 08:43 file3
```
Okay, we have three files we need to hit here. Let's give it a shot:
```
curl http://127.0.0.1:85/file1

RHCSA is Awesome!
```
So far, so good.
```
curl http://127.0.0.1:85/file2

    February 2023
Su Mo Tu We Th Fr Sa
          1  2  3  4
 5  6  7  8  9 10 11
12 13 14 15 16 17 18
19 20 21 22 23 24 25
26 27 28
```
Still doing alright... Let's check the last one.
```
curl http://127.0.0.1:85/file3

<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>403 Forbidden</title>
</head><body>
<h1>Forbidden</h1>
<p>You don't have permission to access this resource.</p>
</body></html>
```
Damn! We were so close...

Ok, let's see if we can figure out what's going on here. Back to the logs...
```
grep httpd /var/log/messages
```
```
Feb  8 14:26:36 rhcsa9-server1 setroubleshoot[3227]: SELinux is preventing /usr/sbin/httpd from getattr access on the file /var/www/html/file3. For complete SELinux messages run: sealert -l d618c7b8-64e2-42ff-8a6e-03e1cf089356
Feb  8 14:26:36 rhcsa9-server1 setroubleshoot[3227]: SELinux is preventing /usr/sbin/httpd from getattr access on the file /var/www/html/file3.#012#012*****  Plugin restorecon (94.8 confidence) suggests   ************************#012#012If you want to fix the label. #012/var/www/html/file3 default label should be httpd_sys_content_t.#012Then you can run restorecon. The access attempt may have been stopped due to insufficient permissions to access a parent directory in which case try to change the following command accordingly.#012Do#012# /sbin/restorecon -v /var/www/html/file3#012#012*****  Plugin catchall_labels (5.21 confidence) suggests   *******************#012#012If you want to allow httpd to have getattr access on the file3 file#012Then you need to change the label on /var/www/html/file3#012Do#012# semanage fcontext -a -t FILE_TYPE '/var/www/html/file3'#012where FILE_TYPE is one of the following: NetworkManager_exec_t, NetworkManager_log_t, NetworkManager_tmp_t, ...OUTPUT_OMITTED... keystone_cgi_content_t, keystone_cgi_htac
Feb  8 14:26:37 rhcsa9-server1 setroubleshoot[3227]: SELinux is preventing /usr/sbin/httpd from getattr access on the file /var/www/html/file3. For complete SELinux messages run: sealert -l d618c7b8-64e2-42ff-8a6e-03e1cf089356
Feb  8 14:26:37 rhcsa9-server1 setroubleshoot[3227]: SELinux is preventing /usr/sbin/httpd from getattr access on the file /var/www/html/file3.#012#012*****  Plugin restorecon (94.8 confidence) suggests   ************************#012#012If you want to fix the label. #012/var/www/html/file3 default label should be httpd_sys_content_t.#012Then you can run restorecon. The access attempt may have been stopped due to insufficient permissions to access a parent directory in which case try to change the following command accordingly.#012Do#012# /sbin/restorecon -v /var/www/html/file3#012#012*****  Plugin catchall_labels (5.21 confidence) suggests   *******************#012#012If you want to allow httpd to have getattr access on the file3 file#012Then you need to change the label on /var/www/html/file3#012Do#012# semanage fcontext -a -t FILE_TYPE '/var/www/html/file3'#012where FILE_TYPE is one of the following: NetworkManager_exec_t, NetworkManager_log_t, NetworkManager_tmp_t, ...OUTPUT_OMITTED... keystone_cgi_content_t, keystone_cgi_htac
```
Ok, just like last time, it's showing us what's going on here and giving suggestions. SELinux is preventing httpd from getattr access to the file. It suggests we can either `restorecon` the file, or run `semanage fcontext -a -t FILE_TYPE '/var/www/html/file3'` to change the label altogether. Let's take a look at the directory:
```
ls -laZ /var/www/html

drwxr-xr-x. 3 root root system_u:object_r:httpd_sys_content_t:s0      57 Feb  7 10:46 .
drwxr-xr-x. 4 root root system_u:object_r:httpd_sys_content_t:s0      33 Feb  1 08:40 ..
-rw-r--r--. 1 root root unconfined_u:object_r:httpd_sys_content_t:s0  18 Feb  1 08:42 file1
-rw-r--r--. 1 root root unconfined_u:object_r:httpd_sys_content_t:s0 168 Feb  1 08:43 file2
-rw-r--r--. 1 root root unconfined_u:object_r:default_t:s0            32 Feb  1 08:43 file3
```
And we can see that file3 has a different label from the other two. Let's try the `restorecon`:
```
restorecon /var/www/html/file3
```
And check the directory again:
```
ls -laZ /var/www/html

drwxr-xr-x. 3 root root system_u:object_r:httpd_sys_content_t:s0      57 Feb  7 10:46 .
drwxr-xr-x. 4 root root system_u:object_r:httpd_sys_content_t:s0      33 Feb  1 08:40 ..
-rw-r--r--. 1 root root unconfined_u:object_r:httpd_sys_content_t:s0  18 Feb  1 08:42 file1
-rw-r--r--. 1 root root unconfined_u:object_r:httpd_sys_content_t:s0 168 Feb  1 08:43 file2
-rw-r--r--. 1 root root unconfined_u:object_r:httpd_sys_content_t:s0  32 Feb  1 08:43 file3
```
Alright, it's looking better! Now let's try to curl it:
```
curl http://127.0.0.1:85/file3

This file is totally messed up!
```
Success!!! Alright, last thing is to fix the firewall so external clients can reach it:
```
firewall-cmd --add-port=85/tcp --permanent
firewall-cmd --reload
```

