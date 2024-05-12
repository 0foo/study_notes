## Apache


* main configuration file   
    * /etc/httpd/conf/httpd.conf




* DocumentRoot parameter 
    * This parameter specifies the default location where the Apache web server looks for its contents.

* ServerRoot. 
    * This defines the default directory where Apache will look for its configuration files. 
    * By default, the /etc/httpd directory is used for this purpose,

* virtual hosts
    * apache uses virtual hosts where it has on I.P. addy but will route based on requested URL

* note: apache can run in a multiprocess or multithreaded mode
    * https://serverfault.com/questions/823121/why-is-apache-spawning-so-many-processes/823162