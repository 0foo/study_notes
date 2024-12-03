

**26.** Write a script named awesome.sh in the root directory on server1.
- a) If “me” is given as an argument, then the script should output “Yes, I’m awesome.”
- b) If “them” is given as an argument, then the script should output “Okay, they are awesome.”
- c) If the argument is empty or anything else is given, the script should output “Usage ./awesome.sh me|them”

#### **Solution to Task 26**
```
vi /awesome.sh
```
Add the following to the file:
```
#!/bin/bash

if [ "$1" = "me" ] ; then
    echo "Yes, I'm awesome."

elif [ "$1" = "them" ] ; then
    echo "Okay, they are awesome."

else
    echo "Usage ./awesome.sh me|them"

fi
```
Change the permissions and test it:
```
chmod +x /awesome.sh
/awesome.sh me
/awesome.sh them
/awesome.sh everyone
/awesome.sh
```



