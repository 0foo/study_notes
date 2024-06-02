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
    * display contents of a file
    * concatenate two file: `cat file1 file2`
    * -n to number lines in the output
    * use heredoc to write multiline out
  ```
    cat <<EOF > file.txt
    This is line 1.
    This is line 2.
    This is line 3.
    EOF
  ```

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
        * ALWAYS quote search string
        * -i: not case sensitive
        * -v: invert, lines that do NOT contain the regex
        * -r: recursively search all files/subdir's
        * -e: search for lines matching more than one regex
          * note: this is an OR i.e. matches one patter OR another
          * grep -e "root" -e "daemon" /etc/passwd
        * -A, -B: num lines before and after the match to return
        * -P: Pearl Compatible Regular Expressions (PCRE)
        * -E (extended regex (expressions ERE)
            * means that extended regex doesn't need to be escaped
            * `grep 'cat\|dog' filename` vs `grep 'cat\|dog' filename`

        * Basic Regular Expressions(BRE)
          * Types of grep regex:
              * What doesn't need escaping/What is BRE (basic regular expression)
                - `[]` (Character classes)
                  * ^ is also not inside
                - `^` (Start of line anchor)
                - `$` (End of line anchor)
                - `.` (Any single character)
                - `*` (Zero or more of the preceding element)
                - \< and \> are used to denote word boundaries.
                - \t for tab
                - \n for newline
                - NOTE: No shorthand character classes are available like \d, \w, etc.


        * Extended Regular Expression (ERE)
            * can use these in basic regex but would have to backslash escape
            - `+` (One or more of the preceding element, in extended regular expressions with `grep -E`)
            - `?` (Zero or one of the preceding element, in extended regular expressions with `grep -E`)
            - `|` (Alternation, in extended regular expressions with `grep -E`)
            - `()` (Grouping, in extended regular expressions with `grep -E`)
            - `{}` (Intervals, in extended regular expressions with `grep -E`)
            - NOTE: No shorthand character classes are available like \d, \w, etc.
            
        * Pearl Compatible Regular Expressions (not on RHCSE)
          * pretty much full vocabulary of REGEX
          * Can use shorthand character classes
            - `\d` : Matches any digit (equivalent to `[0-9]`).
            - `\D` : Matches any non-digit.
            - `\w` : Matches any word character (alphanumeric + underscore).
            - `\W` : Matches any non-word character.
            - `\s` : Matches any whitespace character.
            - `\S` : Matches any non-whitespace character.
          * Can use lookahead, lookbehind, conditional, non-capturing, etc. 


        * -w (word match)
          * Consists of alphanumeric characters (letters A-Z, a-z, digits 0-9) and underscores (_).
          * Is delimited by characters that are not considered word characters (e.g., whitespace, punctuation marks, or the beginning/end of a line).
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
      
        - `\w` (Word character: matches any letter, digit, or underscore)
        - `\W` (Non-word character: matches any character that is not a word character)
        - `\d` (Digit: matches any digit, equivalent to `[0-9]`)
        - `\D` (Non-digit: matches any character that is not a digit)
        - `\s` (Whitespace: matches any whitespace character including spaces, tabs, and line breaks)
        - `\S` (Non-whitespace: matches any character that is not a whitespace character)
        - `\b` (Word boundary: matches the position between a word character and a non-word character)
        - `\B` (Non-word boundary: matches a position that is not a word boundary)
        - `\t` (Tab: matches a tab character)
        - `\n` (Newline: matches a newline character)




### Test questions GREP

1. **How would you use `grep` to search for the string "user100" in the `/etc/passwd` file?**
   - a) `grep "user100" /etc/passwd`
   - b) `grep -r "user100" /etc/passwd`
   - c) `grep -v "user100" /etc/passwd`
   - d) `grep -e "user100" /etc/passwd`

2. **Which command would you use to search for the string "root" in all files within the `/etc` directory recursively?**
   - a) `grep "root" /etc`
   - b) `grep -r "root" /etc`
   - c) `grep -i "root" /etc`
   - d) `grep -v "root" /etc`

3. **What command will search for lines containing the word "error" in `logfile.txt`, ignoring case sensitivity?**
   - a) `grep "error" logfile.txt`
   - b) `grep -v "error" logfile.txt`
   - c) `grep -r "error" logfile.txt`
   - d) `grep -i "error" logfile.txt`

4. **How do you search for lines in `file.txt` that do not contain the string "test"?**
   - a) `grep "test" file.txt`
   - b) `grep -v "test" file.txt`
   - c) `grep -r "test" file.txt`
   - d) `grep -i "test" file.txt`

5. **Which `grep` option would you use to show the line numbers of matching lines in `config.txt` that contain "port"?**
   - a) `grep "port" config.txt`
   - b) `grep -i "port" config.txt`
   - c) `grep -n "port" config.txt`
   - d) `grep -v "port" config.txt`

6. **How can you search for lines in `data.txt` that contain either "cat" or "dog"?**
   - a) `grep "cat|dog" data.txt`
   - b) `grep -e "cat" -e "dog" data.txt`
   - c) `grep -v "cat|dog" data.txt`
   - d) `grep -r "cat" -r "dog" data.txt`

7. **Which command will show lines containing "admin" and the two lines following each match in `users.txt`?**
   - a) `grep -A 2 "admin" users.txt`
   - b) `grep -B 2 "admin" users.txt`
   - c) `grep -C 2 "admin" users.txt`
   - d) `grep -v "admin" users.txt`

8. **What does the following command do? `grep -w "root" /etc/passwd`**
   - a) Searches for lines containing "root" exactly as a word in `/etc/passwd`
   - b) Searches for lines containing "root" in any form in `/etc/passwd`
   - c) Searches for lines not containing "root" in `/etc/passwd`
   - d) Searches for lines containing "root" case-insensitively in `/etc/passwd`

9. **How do you search for lines starting with "root" in `/etc/passwd`?**
   - a) `grep "root" /etc/passwd`
   - b) `grep '^root' /etc/passwd`
   - c) `grep -v "root" /etc/passwd`
   - d) `grep -i "root" /etc/passwd`

10. **Which command would you use to search for a pattern using extended regular expressions in `file.txt`?**
    - a) `grep -E "pattern" file.txt`
    - b) `grep -F "pattern" file.txt`
    - c) `grep -G "pattern" file.txt`
    - d) `grep -P "pattern" file.txt`

11. **How can you search for lines ending with "bash" in `file.txt`?**
    - a) `grep "bash$" file.txt`
    - b) `grep "^bash" file.txt`
    - c) `grep -v "bash" file.txt`
    - d) `grep -i "bash" file.txt`

12. **What does `grep -A 3 "ERROR" logfile.txt` do?**
    - a) Shows lines containing "ERROR" and 3 lines before each match
    - b) Shows lines containing "ERROR" and 3 lines after each match
    - c) Shows lines containing "ERROR" only
    - d) Shows lines not containing "ERROR"

13. **Which command will display the count of lines containing "fail" in `output.log`?**
    - a) `grep -c "fail" output.log`
    - b) `grep -v "fail" output.log`
    - c) `grep -n "fail" output.log`
    - d) `grep -r "fail" output.log`

14. **How do you search for the string "admin" in compressed file `data.gz`?**
    - a) `grep "admin" data.gz`
    - b) `zgrep "admin" data.gz`
    - c) `grep -z "admin" data.gz`
    - d) `gzip -grep "admin" data.gz`

15. **What does the following command do? `grep "\<root\>" file.txt`**
    - a) Searches for lines containing the word "root" in `file.txt`
    - b) Searches for lines containing "root" as part of any word in `file.txt`
    - c) Searches for lines starting with "root" in `file.txt`
    - d) Searches for lines ending with "root" in `file.txt`

16. **Which command would you use to search for the pattern "error" in all `.log` files in the current directory?**
    - a) `grep "error" *.log`
    - b) `grep -r "error" *.log`
    - c) `grep -v "error" *.log`
    - d) `grep -i "error" *.log`

17. **How do you search for lines containing the string "example" but not displaying lines containing "test" in `sample.txt`?**
    - a) `grep "example" sample.txt`
    - b) `grep -v "test" sample.txt`
    - c) `grep "example" sample.txt | grep -v "test"`
    - d) `grep -i "example" sample.txt`

18. **Which command will show lines containing "network" and the three lines before and after each match in `config.txt`?**
    - a) `grep -A 3 -B 3 "network" config.txt`
    - b) `grep -C 3 "network" config.txt`
    - c) `grep -A 3 "network" config.txt`
    - d) `grep -B 3 "network" config.txt`

19. **How would you search for lines in `data.txt` that contain a three-letter word starting with "b" and ending with "t"?**
    - a) `grep "^b.t$" data.txt`
    - b) `grep "b.t" data.txt`
    - c) `grep -E "^b.t$" data.txt`
    - d) `grep -i "b.t" data.txt`

20. **What does `grep -o "pattern" file.txt` do?**
    - a) Displays only the matched parts of matching lines
    - b) Displays lines containing "pattern"
    - c) Inverts the match, showing lines that do not contain "pattern"
    - d) Counts the number of lines containing "pattern"

1. **How would you use `grep` to find lines starting with the word "start" in `file.txt`?**
   - a) `grep 'start$' file.txt`
   - b) `grep '^start' file.txt`
   - c) `grep -E 'start^' file.txt`
   - d) `grep -E '$start' file.txt`

2. **Which `grep` command finds lines that end with "end" in `file.txt`?**
   - a) `grep '^end' file.txt`
   - b) `grep 'end^' file.txt`
   - c) `grep 'end$' file.txt`
   - d) `grep -E 'end' file.txt`

3. **How do you search for lines containing any single character between "a" and "z" followed by "bc" in `file.txt`?**
   - a) `grep '[a-z]bc' file.txt`
   - b) `grep 'a-zbc' file.txt`
   - c) `grep '[a-z]{1}bc' file.txt`
   - d) `grep -E '[a-z]{1}bc' file.txt`

4. **Which command will find lines containing exactly three consecutive digits in `data.txt`?**
   - a) `grep '[0-9][0-9][0-9]' data.txt`
   - b) `grep '[0-9]{3}' data.txt`
   - c) `grep -E '[0-9][0-9][0-9]' data.txt`
   - d) `grep -E '[0-9]{3}' data.txt`

5. **How do you use `grep` to find lines that contain either "cat" or "dog" in `file.txt`?**
   - a) `grep 'cat|dog' file.txt`
   - b) `grep -E 'cat|dog' file.txt`
   - c) `grep -e 'cat' -e 'dog' file.txt`
   - d) `grep 'cat\|dog' file.txt`

6. **Which `grep` command finds lines containing a word boundary followed by "word" in `text.txt`?**
   - a) `grep '\<word\>' text.txt`
   - b) `grep -E '\bword\b' text.txt`
   - c) `grep -w 'word' text.txt`
   - d) `grep '\bword\b' text.txt`

7. **How would you find lines containing the word "example" followed by zero or more characters in `sample.txt`?**
   - a) `grep 'example*' sample.txt`
   - b) `grep 'example.*' sample.txt`
   - c) `grep -E 'example.*' sample.txt`
   - d) `grep -E 'example*' sample.txt`

8. **Which command finds lines that contain a digit followed by a non-digit character in `numbers.txt`?**
   - a) `grep '[0-9][^0-9]' numbers.txt`
   - b) `grep '[0-9]\D' numbers.txt`
   - c) `grep -E '[0-9]\D' numbers.txt`
   - d) `grep -E '[0-9][^0-9]' numbers.txt`


9. **How do you search for lines containing a sequence of three vowels in `text.txt`?**
   - a) `grep '[aeiou]{3}' text.txt`
   - b) `grep -E '[aeiou]{3}' text.txt`
   - c) `grep '[aeiou]{3,3}' text.txt`
   - d) `grep -E '[aeiou]{3,3}' text.txt`

10. **Which `grep` command finds lines containing the word "start" at the beginning of a line and "end" at the end of a line in `sentences.txt`?**
    - a) `grep '^start.*end$' sentences.txt`
    - b) `grep 'start.*end$' sentences.txt`
    - c) `grep -E '^start.*end$' sentences.txt`
    - d) `grep -E 'start.*end$' sentences.txt`

11. **How do you search for lines containing either "foo" or "bar" in `strings.txt`?**
    - a) `grep 'foo\|bar' strings.txt`
    - b) `grep -E 'foo|bar' strings.txt`
    - c) `grep -e 'foo' -e 'bar' strings.txt`
    - d) `grep 'foo|bar' strings.txt`

12. **Which command finds lines containing "error" followed by one or more whitespace characters in `log.txt`?**
    - a) `grep 'error\s+' log.txt`
    - b) `grep -E 'error\s+' log.txt`
    - c) `grep 'error[[:space:]]+' log.txt`
    - d) `grep -E 'error[[:space:]]+' log.txt`

13. **How do you find lines containing a word character followed by a non-word character in `data.txt`?**
    - a) `grep '\w\W' data.txt`
    - b) `grep -E '\w\W' data.txt`
    - c) `grep '\w\W' data.txt`
    - d) `grep -E '\w\W' data.txt`

14. **Which `grep` command finds lines containing "hello" followed by zero or one "o" in `phrases.txt`?**
    - a) `grep 'hello?' phrases.txt`
    - b) `grep -E 'hello?' phrases.txt`
    - c) `grep 'hello\?' phrases.txt`
    - d) `grep -E 'hello\?' phrases.txt`

15. **How do you search for lines containing a sequence of exactly two digits followed by "abc" in `codes.txt`?**
    - a) `grep '[0-9]{2}abc' codes.txt`
    - b) `grep '[0-9][0-9]abc' codes.txt`
    - c) `grep -E '[0-9]{2}abc' codes.txt`
    - d) `grep -E '[0-9][0-9]abc' codes.txt`

16. **Which command finds lines containing a capital letter followed by any lowercase letters in `names.txt`?**
    - a) `grep '[A-Z][a-z]*' names.txt`
    - b) `grep -E '[A-Z][a-z]*' names.txt`
    - c) `grep '[A-Z][a-z]+' names.txt`
    - d) `grep -E '[A-Z][a-z]+' names.txt`

17. **How do you search for lines containing "alpha" or "beta" or "gamma" in `words.txt`?**
    - a) `grep 'alpha|beta|gamma' words.txt`
    - b) `grep -E 'alpha|beta|gamma' words.txt`
    - c) `grep -e 'alpha' -e 'beta' -e 'gamma' words.txt`
    - d) `grep 'alpha\|beta\|gamma' words.txt`

18. **Which `grep` command finds lines containing "123" or "456" at the end of a line in `digits.txt`?**
    - a) `grep '123$|456$' digits.txt`
    - b) `grep -E '123$|456$' digits.txt`
    - c) `grep -e '123$' -e '456$' digits.txt`
    - d) `grep '123\|456$' digits.txt`

19. **How do you find lines containing a non-whitespace character followed by "xyz" in `chars.txt`?**
    - a) `grep '\Sxyz' chars.txt`
    - b) `grep -E '\Sxyz' chars.txt`
    - c) `grep '\sxyz' chars.txt`
    - d) `grep -E '\sxyz' chars.txt`

20. **Which command finds lines containing one or more word characters in `tokens.txt`?**
    - a) `grep '\w+' tokens.txt`
    - b) `grep -E '\w+' tokens.txt`
    - c) `grep '\W+' tokens.txt`
    - d) `grep -E '\W+' tokens.txt`


* Answers: a,b,d,b,d,b,a,a,b,a,a,b,a,b,a,a,c,c,a,a
* Answers: b,c,a,d,b,a,c,b,b,c,b,b,a,b,c,b,b,b,b,b
