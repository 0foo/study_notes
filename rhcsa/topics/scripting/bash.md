## Bash Scripting

* manually run scripts are run from a subshell of the terminal environment

* shebang. This is the line #!/bin/bash
    * The shebang makes clear that the subshell should be a bash subshell
    * run the subshell as bash subshell
    * if it is omitted, the script code will be executed by the shell that is used in the parent shell.
        * cause issues if user uses ksh or sh or soemthing else
    
* comments: #
* ensure script is executable: chmod +x <yourscriptname.sh>
    * or can just pass script to /bin/bash command


* exit 0
    * add exit command at the end of every script 
    * 0 means a success, and will return a 0 at the end of successful script execution
    * calling scripts can run `echo $?` to see if script ran successfully

* parameters
    * starts at $1 continues up, $2,$3, etc.
    * $@ is all arguments in array
``` 
    for i in "$@" do
        echo $i
    done
``````

* variables 
    * assign with x="Test"
    * reference with dollar sign: echo $x

* command substitution 
    * dollar sign plus parenthesis
    * useful for assigning output of commands to variables
    * x=$(echo "test) && echo $x

* pipe output to /dev/null
    * ping -c 1 google.com > /dev/null $$ echo "google is up"

* redirect both stdout && sterr
    * pass a 2>&1 after your redirect 
    * use &> instead of >
    * $(ping -c 1 "$SOMESITE" > /dev/null 2>&1) && echo "it's up" || echo "it's down"
    * https://vegastack.com/tutorials/bash-redirect-stderr-stdout/

* useful keywords:
    * read => get input from user
    * echo => show output 




### Looping structures

* for loop over array
```
for i in "$@" do
    echo $i
done

```
* for loop with init;action;condition structure

```
for (( COUNTER=100; COUNTER>1; COUNTER-- )); do
    echo $COUNTER
done

```

* for/in loop
    * note: inclusive, includes both 100 and 105

```
for i in {100..104}; do
    echo $i
done
```



* while 
    * iterates WHILE condition is true
```
while <some test>; do
    <some action>
done
```
```
TBI
```
* until
    * iterates while a condition is false, i.e. UNTIL a condition is true

```
until <some test>; do
    <some action>
done
```





### Conditional Structures

* if/else
    * can add more conditions with elif
```
if [ -z $1 ]; then
    echo enter a name
    read NAME
elif [ -z $2 ]; then
    echo "sup"
else
    NAME=$1
fi
```



* && and ||
    * || is a logical OR and will execute the second part of the statement only if the first part is NOT true i.e. false
    * && is the logical AND and will execute the second part of the statement only if the first part is true
    * ex:
```
[ -z $1 ] && echo no argument provided
ping -c 1 10.0.0.20 2>/dev/null || echo node is not available
```

```
SOMESITE="google.com"
$(ping -c 1 "$SOMESITE" > /dev/null 2>&1) && echo "it's up" || echo "it's down"
```


* test command
    * Evaluate a conditional expression
    * combine with if/then for supreme power
    * two ways of writing
    * test <flags> or [ <flags> ]
    * test flag s
        * https://ss64.com/bash/test.html
    * new test: [[ <flags> ]]
        * The double bracket [[ construct, also known as 'extended test' or 'New Test' is more versatile 
        * the old test [ is more portable
    * examples:
```
test -1 -gt -2 && echo yes
# yes

[ -1 -gt -2 ] && echo "yes"
# yes

if [ -1 -gt -2 ]; then
    echo "yes"
else
    echo "no"
fi
# yes

```

* case 
    * looks for a match pattern, then if finds match pattern will execute the co-orresponding code
    * will then terminate


* match pattern
    * A pattern and its commands make a clause, which ends with ;;.
    * Patterns support special characters.
    * The ) operator terminates a pattern list.
    * The | operator separates multiple patterns.
    * The script executes the commands corresponding to the first pattern matching the input $variable.
    * The asterisk * symbol defines the default case, usually in the final pattern.
    * It is a common practice to use the wildcard asterisk symbol (*) as a final pattern to define the default case. This pattern will always match.

* exit status
    * The script has two exit statuses:
        *  The return status when the input matches no pattern is 0.
        * If the command matches the input variable to a pattern, the executed command exit status is returned.
```
case EXPRESSION in

  PATTERN_1)
    STATEMENTS
    ;;

  PATTERN_2)
    STATEMENTS
    ;;

  PATTERN_N)
    STATEMENTS
    ;;

  *)
    STATEMENTS
    ;;
esac
```

```
#!/bin/bash

echo -n "Enter the name of a country: "
read COUNTRY

echo -n "The official language of $COUNTRY is "

case $COUNTRY in

  Lithuania)
    echo -n "Lithuanian"
    ;;

  Romania | Moldova)
    echo -n "Romanian"
    ;;

  Italy | "San Marino" | Switzerland | "Vatican City")
    echo -n "Italian"
    ;;

  *)
    echo -n "unknown"
    ;;
esac
```


### Arrays
* set array
    * some_array=(1 "Test" 3.2 "Stuff")

* access arrays (zero indexed)
    * echo ${some_array[0]}

* get length of array
    * ` echo ${#some_array[@]} `
    * the @ explodes the array, the # returns the count

* gotcha: pass in a string as array value will separate that string based on SPACES NOT QUOTES
    ```
    test=' "a" "b" "c d" '
    nick@nick-XPS-9315:~$ array=($test)
    nick@nick-XPS-9315:~$ echo ${#array[@]}
    4
    ```
* to separate based on quotes use eval
    ```
    nick@nick-XPS-9315:~$ array=($test)
    nick@nick-XPS-9315:~$ echo ${#array[@]}
    3
    ```    



### Troubleshooting
* If a script does not do what you expect it to do, try starting it as an argument to the bash -x command.
* This will show you line by line what the script is trying to do, and also will show you specific errors if it does not work.
* `/bin/bash -x somescript.sh`


### Best Practices for bash scripts (Continually In Progress)
* quote variables to avoid word splitting
    * "$DEMO"
    * technically don't need to do this with new test [[]]
