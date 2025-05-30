1. Search for the keyword "example" in the file `data.txt`.
2. Search for the keyword "user" in the file `users.txt` ignoring case.
3. Invert the match for the keyword "error" in the file `log.txt`.
4. Recursively search for the keyword "config" in the directory `/etc`.
5. Search for either the keyword "admin" or "user" in the file `accounts.txt`.
6. Show 3 lines before and after the match for "error" in the file `log.txt`.
7. Use Perl Compatible Regular Expressions to search for the keyword "root" in the file `passwd`.
8. Use extended regular expressions to search for the pattern "cat|dog" in the file `animals.txt`.
9. Search for lines that do not start with a digit in the file `numbers.txt`.
10. Search for lines that end with a period in the file `sentences.txt`.
11. Search for lines that contain any single character followed by "at" in the file `words.txt`.
12. Search for lines that contain zero or more occurrences of "a" followed by "bc" in the file `pattern.txt`.
13. Search for lines that contain the word "start" at the beginning of a line in the file `commands.txt`.
14. Search for lines that contain the word "end" at the end of a line in the file `commands.txt`.
15. Search for lines that contain "apple" followed by any single character in the file `fruits.txt`.
16. Search for lines that contain the word "test" zero or more times in the file `repetition.txt`.
17. Search for lines that contain the word "begin" at a word boundary in the file `text.txt`.
18. Search for lines that contain a tab character in the file `whitespace.txt`.
19. Search for lines that contain a newline character in the file `multiline.txt`.
20. Search for lines that contain one or more occurrences of "error" in the file `log.txt`.
21. Search for lines that contain zero or one occurrence of "warning" in the file `log.txt`.
22. Search for lines that contain either "success" or "failure" in the file `results.txt`.
23. Group the pattern "cat" or "dog" and search in the file `pets.txt`.
24. Search for lines that contain exactly three occurrences of "a" in the file `letters.txt`.
25. Search for lines that match the whole word "word" in the file `dictionary.txt`.
26. Search for lines that contain the range of characters [a-f] in the file `hex.txt`.
27. Escape the special character "." and search for it in the file `dots.txt`.
28. Search for lines that contain exactly two digits in a row in the file `numbers.txt`.
29. Search for lines that contain a minimum of 2 and a maximum of 4 "x" characters in the file `letters.txt`.
30. Search for lines that contain the boundary anchor `\bword\b` in the file `text.txt`.
31. Use the `-n` option to show line numbers for matches of "pattern" in the file `data.txt`.
32. Use the `\d` shorthand character class to search for any digit in the file `numbers.txt`.
33. Use the `\w` shorthand character class to search for any word character in the file `text.txt`.
34. Use the `\s` shorthand character class to search for any whitespace character in the file `whitespace.txt`.
35. Use the `\S` shorthand character class to search for any non-whitespace character in the file `text.txt`.
36. Use the `\D` shorthand character class to search for any non-digit character in the file `numbers.txt`.
37. Search for lines that contain the non-word boundary `\Bword\B` in the file `text.txt`.
38. Search for lines that contain the word "include" using the `-i` option in the file `code.txt`.
39. Search for lines that do not contain the word "exclude" using the `-v` option in the file `list.txt`.
40. Search for lines that contain the keyword "root" in the compressed file `passwd.gz`.
41. Search for lines that contain the keyword "bash" in the file `shells.txt` and show the line numbers.
42. Search for lines that contain the word "network" ignoring case in the file `config.txt`.
43. Search for lines that contain the keyword "server" in the file `hosts` and show 2 lines after the match.
44. Search for lines that contain the keyword "client" in the file `hosts` and show 2 lines before the match.
45. Search for lines that contain the keyword "database" in the file `config` and show 1 line before and 1 line after the match.
46. Search for lines that contain the pattern "^[a-z]" in the file `lowercase.txt`.
47. Search for lines that contain the pattern "[A-Z]$" in the file `uppercase.txt`.
48. Search for lines that contain the word "function" at the start of a line in the file `script.sh`.
49. Search for lines that contain the word "return" at the end of a line in the file `script.sh`.
50. Search for lines that contain the string "TODO" in the file `notes.txt`.


----

1. `grep "example" data.txt`
2. `grep -i "user" users.txt`
3. `grep -v "error" log.txt`
4. `grep -r "config" /etc`
5. `grep -e "admin" -e "user" accounts.txt`
6. `grep -A 3 -B 3 "error" log.txt`
7. `grep -P "root" passwd`
8. `grep -E "cat|dog" animals.txt`
9. `grep "^[^0-9]" numbers.txt`
10. `grep "\.$" sentences.txt`
11. `grep ".at" words.txt`
12. `grep "a*bc" pattern.txt`
13. `grep "^start" commands.txt`
14. `grep "end$" commands.txt`
15. `grep "apple." fruits.txt`
16. `grep "test*" repetition.txt`
17. `grep "\<begin\>" text.txt`
18. `grep "\t" whitespace.txt`
19. `grep "\n" multiline.txt`
20. `grep -E "error+" log.txt`
21. `grep -E "warning?" log.txt`
22. `grep -E "success|failure" results.txt`
23. `grep -E "(cat|dog)" pets.txt`
24. `grep -E "a{3}" letters.txt`
25. `grep -w "word" dictionary.txt`
26. `grep "[a-f]" hex.txt`
27. `grep "\." dots.txt`
28. `grep -E "[0-9]{2}" numbers.txt`
29. `grep -E "x{2,4}" letters.txt`
30. `grep "\bword\b" text.txt`
31. `grep -n "pattern" data.txt`
32. `grep -P "\d" numbers.txt`
33. `grep -P "\w" text.txt`
34. `grep -P "\s" whitespace.txt`
35. `grep -P "\S" text.txt`
36. `grep -P "\D" numbers.txt`
37. `grep "\Bword\B" text.txt`
38. `grep -i "include" code.txt`
39. `grep -v "exclude" list.txt`
40. `zgrep "root" passwd.gz`
41. `grep -n "bash" shells.txt`
42. `grep -i "network" config.txt`
43. `grep -A 2 "server" hosts`
44. `grep -B 2 "client" hosts`
45. `grep -A 1 -B 1 "database" config`
46. `grep "^[a-z]" lowercase.txt`
47. `grep "[A-Z]$" uppercase.txt`
48. `grep "^function" script.sh`
49. `grep "return$" script.sh`
50. `grep "TODO" notes.txt`
