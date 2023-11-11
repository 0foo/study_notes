
1. less, cat, head, tail, cut, sort, wc


1. less
    * press q to quit less
    * search with forward slash: /<keyword>
    * search backwards with questio mark: ?<keyword>
    * cycle search with 'n'
    * 'G' to go to last line of file
    * This same commands as vim and man
    * note: more is similar to less(less is a newer version)


1. head and tail
    * default is 10 lines, use -n to custom define line nums
    * can tail -f  for real time following of file updates
    * can view specific line numbers by combining them
        * head -n 11 | tail 1
        * will show line 11 

1. cut
    * essentially an explode 
    * -d is the delimiter
    * -f is the field number to extract
    * cut -d : -f 1 /etc/passwd
        * cuts with colon delimiter
        * extracts field number 1 

1. sort
    * default is byte order NOT alphabetically
    * -n is numeric order
    * -r is reverse
    * -t:  column separator, i.e. what explodes it
    * -k: column to sort with -t
    * ex: sort -k3  -t: /etc/passwd
        * uses field separator : to sort by 3rd field

1. wc
    * counts lines, words, characters etc.
    * in format lines, words, characters
    * 

1.  awk
    * awk is a huge system and whole books written about it
    * how much to know about awk for rhcsa?
    * can pull out 4th field: 
        * awk -F : '{print $4}' /etc/passwd
    * equivalent to:
        * cut -d : -f 4 /etc/passwd
    * awk has better parsing ability than cut sometimes, so if cut no work try awk


1. sed
    * stream editor
    * can filter files like grep but also allows modification of the files
    * sed -i s/old-text/new-text/g somefile
    * can put quotes around the s/ field
    * delete a line number:
        * sed -i -e '2d' ~/somefile
        * delete line 2



* ### Awk and Sed are huge programs dont need to focus too much on them, easy to get lost in them

1.  Use grep and regular expressions to analyse text
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


    * Always surround regex with quotes or single quotes for escaping purposes
        * grep '^root' /etc/passwd
      
    * Common regular expression parameters are shown below:
        | Symbol | Description                                                        |
        |--------|--------------------------------------------------------------------|
        | ^      | Beginning of a line or word                                        |
        | $      | End of a line or word                                              |
        | \|     | Or                                                                 |
        | .      | Any single character: r.t matches rat rot rut, etc.                                                      |
        | *      | Zero to infinite number of the previous character                                        |
        | ?      | Zero or one  of any of the previous character: cou?ler, matches color and couler, makes previous character optional                                              |
        | []     | Range of characters  [abc] matches a or b or c                                        |
        | \      | Escape character                                                   |
        | ''     | Mask meaning of enclosed special characters                        |
        | ""     | Mask meaning of all enclosed special characters except \, $ and '' |
        |{x}| matches a number of the PREVIOUS character: x{3}, matches xxx|
        |{x,y}| matches a minimum of x and maximum of y: x{1,3} matches 1 to 3 x's|
