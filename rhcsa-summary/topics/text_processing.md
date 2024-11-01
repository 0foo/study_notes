### Know
* globbing
* shell expansion- 5 types and how to avoid if not wanted
* seq 
* redirection or error/stdout also tee command
* grep and it's various comman flags
* less(man) navigation 
* brace expansion
* variable expansion
* arithmetic expansion
* command substitution
* glob/regex: 
    * `man grep` 
    * glob: *, ?, [az], [a-z], [^az], character classes i.e. [[:upper:]], ^ and $/start_end of line
    * regex: alternation with |, -E with grep
* grep: recursive, not, case insensitive, logical OR, logical AND
* how to combine regex/glob: c[aou]*t

### Essentials/Tips
* `man bash` search for expansion
* `man grep` has regex explanation!!!
* `ls *a` : files that end with a
* `ls *a*`: files with a in them
* ignore blank lines= grep '^$'
* use single quotes for regex


### redirection
* >  output stout
* 2> output sterr
* `cat file > /dev/null 2>&1`  output both same as `cat file &> /dev/null`
* `| tee`

### seq
* echo $(seq 2 2 10)
* (start step end)

### Shell expansion
* brace expansion
    * `echo {Sunday,Monday,Tuesday,Wednesday}.log`
    * `echo file{1..3}.txt`
    - Numeric Range: `{1..5}` → `1 2 3 4 5`
    - Alphabetic Range: `{a..e}` → `a b c d e`
    - Comma-Separated: `{apple,banana,grape}` → `apple banana grape`
    - Prepend/Append: `file{1,2,3}.txt` → `file1.txt file2.txt file3.txt`
    - Nested: `{x,y}{1,2}` → `x1 x2 y1 y2`
    - Zero-Padding: `{01..03}` → `01 02 03`
    - Step: `{1..10..2}` → `1 3 5 7 9`
* variable expansion
    * `echo $VARIABLENAME` or `echo ${VARIABLENAME}`
    * braces useful if need to concatenate
* command substitution
    * `echo $(pwd)`
* Arithmetic Expansion
    * `echo $((3 + 2))`
* avoid expansion with backslash i.e. \$HOME
* Use double quotation marks to suppress globbing and shell expansion, but still allow command and variable substitution
* Use single quotation marks to interpret all text literally.


### regex/glob
* `man grep` has regex/glob explanation!!!

### Grep
`man grep`




less, cat, head, tail, cut, sort, wc, awk, sed, grep, zgrep

