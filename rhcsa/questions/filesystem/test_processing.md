1. How do you quit the `less` command?
2. How can you search for a keyword in `less`?
3. How can you search backwards for a keyword in `less`?
4. Which command cycles through search results in `less`?
5. How do you go to the last line of a file in `less`?
6. What is the difference between `more` and `less`?
7. What does the `cat` command do?
8. How do you concatenate two files using `cat`?
9. How can you number the lines in the output of `cat`?
10. How do you use heredoc to write multiline text to a file with `cat`?
11. What is the default number of lines displayed by `head` and `tail`?
12. How can you follow real-time updates of a file with `tail`?
13. How can you view a specific line number using `head` and `tail` together?
14. What does the `cut` command do?
15. Which option in `cut` specifies the delimiter?
16. Which option in `cut` specifies the field number to extract?
17. How can you extract the first field from `/etc/passwd` using `cut`?
18. What is the default sorting order of the `sort` command?
19. How can you sort numerically with `sort`?
20. How do you sort in reverse order using `sort`?
21. Which option in `sort` specifies the column separator?
22. Which option in `sort` specifies the column to sort by?
23. How can you sort the third field of `/etc/passwd` using `sort`?
24. What does the `wc` command do?
25. How can you count lines, words, and characters in a file using `wc`?
26. What is `awk` and why is it considered a large program?
27. How can you pull out the fourth field from `/etc/passwd` using `awk`?
28. How does `awk` compare to `cut` for parsing?
29. What does the `sed` command do?
30. How can you use `sed` to replace text in a file?
31. How can you delete a specific line number using `sed`?
32. What does the `grep` command do?
33. What is `zgrep` and how does it differ from `grep`?
34. How do you use `grep` to search for a keyword in `/etc/passwd`?
35. What does the `-i` option in `grep` do?
36. What does the `-v` option in `grep` do?
37. How can you recursively search directories with `grep`?
38. How can you search for multiple patterns using `grep`?
39. How do you use `grep` to return lines before and after a match?
40. What are Basic Regular Expressions (BRE) in `grep`?
41. How do you match the start of a line in `grep`?
42. How do you match the end of a line in `grep`?
43. How do you match any single character in `grep`?
44. How do you match zero or more of the preceding element in `grep`?
45. How do you denote word boundaries in `grep`?
46. How do you use extended regular expressions (ERE) with `grep`?
47. What is the `-E` option in `grep` used for?
48. How do you match one or more of the preceding element in `grep -E`?
49. How do you match zero or one of the preceding element in `grep -E`?
50. How do you use alternation in `grep -E`?
51. What are Perl Compatible Regular Expressions (PCRE) in `grep`?
52. How do you use word boundaries in `grep`?
53. How do you show line numbers with `grep`?
54. How do you use the `\d` shorthand character class in `grep`?
55. How do you use the `\w` shorthand character class in `grep`?
56. How do you use the `\s` shorthand character class in `grep`?
57. What does the `-w` option in `grep` do?
58. How do you match a range of characters in `grep`?
59. How do you escape special characters in `grep`?
60. How do you match a specific number of the preceding character in `grep`?




1. Press `q`.
2. Use a forward slash followed by the keyword: `/keyword`.
3. Use a question mark followed by the keyword: `?keyword`.
4. Press `n`.
5. Press `G`.
6. `less` is a newer version with more capabilities.
7. It displays the contents of a file.
8. `cat file1 file2`.
9. Use the `-n` option.
10. 
   ```shell
   cat <<EOF > file.txt
   This is line 1.
   This is line 2.
   This is line 3.
   EOF
11. 10 lines.
12. Use tail -f.
13. head -n 11 | tail -1.
14. It extracts sections of lines from input.
15. -d.
16. -f.
17. cut -d : -f 1 /etc/passwd.
18. Byte order.
19. Use the -n option.
20. Use the -r option.
21. -t.
22. -k.
23. sort -k3 -t: /etc/passwd.
24. Counts lines, words, and characters.
25. wc filename.
26. A powerful text processing language with extensive capabilities.
27. awk -F : '{print $4}' /etc/passwd.
28. awk has better parsing abilities.
29. A stream editor that can filter and modify text.
30. sed -i 's/old-text/new-text/g' somefile.
31. sed -i -e '2d' somefile.
32. Searches for patterns in text.
33. zgrep searches compressed files.
34. grep user100 /etc/passwd.
35. Makes the search case-insensitive.
36. Inverts the match, showing lines that do not match.
37. Use the -r option.
38. Use the -e option with multiple patterns.
39. Use the -A and -B options.
40. Basic regular expressions used by default in grep.
41. Use the ^ character.
42. Use the $ character.
43. Use the . character.
44. Use the * character.
45. Use \< and \>.
46. Use the -E option.
47. Enables extended regular expressions.
48. Use the + character.
49. Use the ? character.
50. Use the | character.
51. Advanced regex with full vocabulary and additional features.
52. Use the \b character class.
53. Use the -n option.
54. Matches any digit: \d.
55. Matches any word character: \w.
56. Matches any whitespace character: \s.
57. Matches whole words.
58. Use the [] character class.
59. Use the \ escape character.
60. Use {x} for exact number matches.
