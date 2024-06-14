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
                  - ^ this means NOT if inside a character class
                  - `grep '[^a-z]' file.txt`
                    - This matches any character that is not a lowercase letter from 'a' to 'z'.
                    - don't have to backslash if in a character class
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
            - Note: depending on your build shorthand character classes may or may not be available in extended regex
            
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
        - `\s` (Whitespace: matches any whitespace character including spaces, tabs, and line breaks)
        - `\S` (Non-whitespace: matches any character that is not a whitespace character)
        - `\b` (Word boundary: matches the position between a word character and a non-word character)
        - `\B` (Non-word boundary: matches a position that is not a word boundary)
        - `\t` (Tab: matches a tab character)
        - `\n` (Newline: matches a newline character)

        * These are additional character classes that don't work with grep -E
        - `\d` (Digit: matches any digit, equivalent to `[0-9]`)
        - `\D` (Non-digit: matches any character that is not a digit)


