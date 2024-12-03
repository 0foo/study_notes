### Tips
* On the RHCSA exam, you are likely to configure a couple of services. It is a
good idea to read through the exam questions, identify the services that need to be
enabled, and enable them all at once to make sure that they are started automatically
when you restart. This prevents your being so focused on configuring the service that
you completely forget to enable it as well.


* Reset root password if forget
    * Very important, on the RHCSA
    * https://old.reddit.com/r/redhat/comments/e3dpux/a_faster_way_to_recover_the_root_password_for/


* Run mandb to update the man pages for quicker access


* If you have a task at hand and you know the executable name but that's it then you can use yum provides to find how to install it, rpm -qd I believe will give you the documentation for the package, rpm -qc should list the config files if I'm not mistaken, mandb to update the man pages database (I think this happens daily by default and should be in the cron folder if you've forgotten the command), man -k or apropos if you have already forgotten what you need to be searching for, and if you're in a tight spot then 'rpm -ql' will list everything from the installed package for you too - good for figuring out executables or services when you only remember the package name.