### Know
* text_processing.md
* conditional
* for loop
* what does bash script return if there's no return statement?
* what exit code is true or false in bash?
* how to access the exit code of last run process?
* test command and 2 ways to access the result!?
* compare strings if equal
* read a file line by line
* output multiline to file
* sequences
* what does export do
* how to view all environment variables (2 ways)

### See text_processing.md section for part 1!!!

### test
* return codes are not echo-able directly
* they are assigned to ? variable
* test 1 -lt 2; echo $?
* [ 4 -lt 2 ] && echo "True" || echo "False"


### if
* if test 1 -lt 2; then echo "sup"; fi
* if [ 4 -lt 2 ]; then echo "sup"; else  echo "aw"; fi
* if [ 4 -lt 2 ]; then echo "sup"; elif [ 1 -lt 2 ]; then  echo "aw yeah"; fi

```
systemctl is-active psacct > /dev/null 2>&1

if [ $? -ne 0 ]; then
  sudo systemctl start psacct
elif [sometest]; then
  something
else
  sudo systemctl stop psacct
fi
```

### for
* iterates over items separated by: spaces, tabs, or newlines
* for EVEN in $(seq 2 2 10); do echo "$EVEN"; done
* for x in $(ls -d */); do echo "$x"; done

### exit codes
* returns exit code of last command by default

### Other interesting options
```
# Read a file line by line
while read line; do
    echo "$line"
done < input_file.txt
```

* output multiline to a file
```
cat <<EOF > file.txt
This is line 1.
This is line 2.
This is line 3.
EOF
```

### Variables
* Shell variables that are not environment variables can only be used by the shell. Environment
variables can be used by the shell and by programs run from that shell.
* You can make any variable defined in the shell into an environment variable by marking it for
export with the export command.

* `env` vs `set`
* `unset`


### Not needed RHCSA

```
if [ "$str1" = "$str2" ]; then
  echo "Strings are equal."
else
  echo "Strings are not equal."
fi

# double brackets allow regex/pattern matching
if [[ "$str" == hello* ]]; then
  echo "String starts with 'hello'."
else
  echo "String does not start with 'hello'."
fi
```



* pipe to while loop
```
ls | while read file; do
  echo "File: $file"
done
```
* note: the while loop is in a subshell so subshell free version:
```
count=0
while read line; do
  echo "Processing: $line"
  count=$((count + 1))
done < <(ls)
```

```
IFS=$'\n'; for i in $(ls -d1 */); do echo "$here/$i"; cd "$here/$i"; ls; cd $here; done;
```

```
for i in $(ls); do echo "LOCATION: $here/$i"; test -d "$here/$i" && cd "$here/$i"; ls; cd ~; done;
```

* text block via cli
```
cat <<EOF > file.txt
This is line 1.
This is line 2.
This is line 3.
EOF
```

