### Text processing
1. `less`
    * press q to quit less
    * search with forward slash: /<keyword>
    * search backwards with questio mark: ?<keyword>
    * cycle search with 'n'
    * 'G' to go to last line of file
    * This same commands as vim and man
    * note: more is similar to less(less is a newer version)

1. `cat`
    * TBI

1. `head` and `tail`
    * default is 10 lines, use -n to custom define line nums
    * can tail -f  for real time following of file updates
    * can view specific line numbers by combining them
        * head -n 11 | tail 1
        * will show line 11 

1. `cut`
    * essentially an explode 
    * -d is the delimiter
    * -f is the field number to extract
    * cut -d : -f 1 /etc/passwd
        * cuts with colon delimiter
        * extracts field number 1 

1. `sort`
    * default is byte order NOT alphabetically
    * -n is numeric order
    * -r is reverse
    * -t:  column separator, i.e. what explodes it
    * -k: column to sort with -t
    * ex: sort -k3  -t: /etc/passwd
        * uses field separator : to sort by 3rd field

1. `wc`
    * counts lines, words, characters etc.
    * in format lines, words, characters
    * 

1. `awk`
    * awk and sed are huge programs dont need to focus too much on them, easy to get lost in them
    * awk is a huge system and whole books written about it
    * how much to know about awk for rhcsa?
    * can pull out 4th field: 
        * awk -F : '{print $4}' /etc/passwd
    * equivalent to:
        * cut -d : -f 4 /etc/passwd
    * awk has better parsing ability than cut sometimes, so if cut no work try awk


1. `sed`
    * awk and aed are huge programs dont need to focus too much on them, easy to get lost in them
    * stream editor
    * can filter files like grep but also allows modification of the files
    * sed -i s/old-text/new-text/g somefile
    * can put quotes around the s/ field
    * delete a line number:
        * sed -i -e '2d' ~/somefile
        * delete line 2

1.  `grep` and `zgrep`
    * Use grep and regular expressions to analyse text
    * zgrep is grep on compressed files
    * The grep command is used to find text. For example:
        ```shell
        grep user100 /etc/passwd 
        ```
    * grep: general regular expression parser 
        * -i: not case sensitive
        * -v: invert, lines that do NOT contain the regex
        * -r: recursively search all files/subdir's
        * -e: search for lines matching more than one regex
        * -A, -B: num lines before and after the match to return
        * -E (use alternation)
        * -w (word match)
        * -n (show line numbers)

    * Always surround regex with quotes or single quotes for escaping purposes
        * grep '^root' /etc/passwd
      
    * Common regular expression parameters are shown below:
        * ^ : Beginning of a line or word
        * $ : End of a line or word
        * | : Or
        * . : Any single character: r.t matches rat, rot, rut, etc.
        * * : Zero to infinite number of the previous character
        * ? : Zero or one of any of the previous character: cou?ler matches color and couler, makes previous character optional
        * [] : Range of characters [abc] matches a or b or c
        * \ : Escape character
        * '' : Mask meaning of enclosed special characters
        * "" : Mask meaning of all enclosed special characters except \, $ and ''
        * {x} : Matches a number of the previous character: x{3} matches xxx
        * {x,y} : Matches a minimum of x and maximum of y: x{1,3} matches 1 to 3 x's
        * \b: boundary anchor used to make sure regex is searched based on a word not the string inside a text
            * grep "\bword\b" file.txt
                * will return all occurance or word with non word character in front and back
                * a non-word character is basically NOT alphanumeric (more or less)


## Exam Objectives

### Use grep and regular expressions to analyze text 

* **Basic Usage**:
  * **Search for a Pattern**:
    * `grep pattern file`: Searches for lines in `file` that contain `pattern`.
    * Example:
      ```bash
      grep "keyword" file.txt
      ```

* **Regular Expressions (Regex)**:
  * **Basic Patterns**:
    * `.` : Matches any single character.
    * `^` : Matches the beginning of a line.
    * `$` : Matches the end of a line.
    * `*` : Matches zero or more occurrences of the previous character or group.
    * `[]` : Matches any one of the enclosed characters.

* **Examples**:
  * **Search for Lines Starting with a Pattern**:
    ```bash
    grep "^pattern" file.txt
    ```
  * **Search for Lines Ending with a Pattern**:
    ```bash
    grep "pattern$" file.txt
    ```
  * **Search for Lines Containing a Word**:
    ```bash
    grep "\bword\b" file.txt
    ```
  * **Search for Lines Not Containing a Pattern**:
    ```bash
    grep -v "pattern" file.txt
    ```
  * **Count Matching Lines**:
    ```bash
    grep -c "pattern" file.txt
    ```

* **Advanced Usage**:
  * **Recursive Search in Directories**:
    ```bash
    grep -r "pattern" directory/
    ```
  * **Search for Patterns in Specific File Types**:
    ```bash
    grep "pattern" *.txt
    ```
  * **Using grep with Pipelines**:
    ```bash
    command | grep "pattern"
    ```

* **Combining Commands**:
  * **Count Lines Matching a Pattern in a Command Output**:
    ```bash
    command | grep "pattern" | wc -l
    ```
  * **Search for Patterns in Compressed Files**:
    ```bash
    zgrep "pattern" file.gz
    ```

* **Using Extended Regular Expressions**:
  * **Using `-E` Option**:
    ```bash
    grep -E "pattern" file.txt
    ```
  * **Escape Special Characters**:
    ```bash
    grep "\(" file.txt
    ```

* **Ignoring Case Sensitivity**:
  * **Using `-i` Option**:
    ```bash
    grep -i "pattern" file.txt
    ```

* **Understanding Output**:
  * **Display Matching Lines Only**:
    ```bash
    grep -o "pattern" file.txt
    ```

* **Common Errors**:
  * **No Such File or Directory**:
    ```bash
    grep: file.txt: No such file or directory
    ```

* **Searching for Multiple Patterns**:
  * **Using `-e` Option**:
    ```bash
    grep -e "pattern1" -e "pattern2" file.txt
    ```

* **Searching for Inverted Patterns**:
  * **Using `-v` Option**:
    ```bash
    grep -v "pattern" file.txt
    ```

