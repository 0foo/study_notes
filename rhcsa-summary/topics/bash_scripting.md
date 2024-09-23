

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