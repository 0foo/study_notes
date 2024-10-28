### Arithmetic expansion is very important


### test

* test 1 -lt 2; echo $?
* [ 4 -lt 2 ] && echo "sup" || echo "aw"


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

### variable names
* can use either:
  * ${HOST}
  * $HOST
* use braces if need to concatenate inside a string

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