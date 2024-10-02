less, cat, head, tail, cut, sort, wc, awk, sed, grep, zgrep

```
cat <<EOF > file.txt
This is line 1.
This is line 2.
This is line 3.
EOF
```



### seq
* echo $(seq 2 2 10)


### brace expansion
- Numeric Range: `{1..5}` → `1 2 3 4 5`
- Alphabetic Range: `{a..e}` → `a b c d e`
- Comma-Separated: `{apple,banana,grape}` → `apple banana grape`
- Prepend/Append: `file{1,2,3}.txt` → `file1.txt file2.txt file3.txt`
- Nested: `{x,y}{1,2}` → `x1 x2 y1 y2`
- Zero-Padding: `{01..03}` → `01 02 03`
- Step: `{1..10..2}` → `1 3 5 7 9`



### shell pattern matching (also known as globbin)
* tbd


### regex
* ^cat$
* c[aou]t
* c.t
* c[aou]*t
* c.*t
* 'c.\{2\}t'
* '^[#;]'
* It is recommend practice to use single quotes to encapsulate the regular expression
because they often contain shell metacharacters (such as $, *, and {}).

```
. The period (.) matches any single character.
? The preceding item is optional and will be matched at most once.
* The preceding item will be matched zero or more times.
+ The preceding item will be matched one or more times.
{n} The preceding item is matched exactly n times.
{n,} The preceding item is matched n or more times.
{,m} The preceding item is matched at most m times.
{n,m} The preceding item is matched at least n times, but not more than m times.
[:alnum:] Alphanumeric characters: '[:alpha:]' and '[:digit:]'; in the 'C' locale and ASCII
character encoding, this is the same as '[0-9A-Za-z]'.
[:alpha:] Alphabetic characters: '[:lower:]' and '[:upper:]'; in the 'C' locale and ASCII
character encoding, this is the same as '[A-Za-z]'.
[:blank:] Blank characters: space and tab.
[:cntrl:] Control characters. In ASCII, these characters have octal codes 000
through 037, and 177 (DEL). In other character sets, these are the
equivalent characters, if any.
[:digit:] Digits: 0 1 2 3 4 5 6 7 8 9.
[:graph:] Graphical characters: '[:alnum:]' and '[:punct:]'.
[:lower:] Lower-case letters; in the 'C' locale and ASCII character encoding, this is a
b c d e f g h i j k l m n o p q r s t u v w x y z.
[:print:] Printable characters: '[:alnum:]', '[:punct:]', and space.
[:punct:] Punctuation characters; in the 'C' locale and ASCII character encoding, this
is! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ' { | } ~. In other character sets,
these are the equivalent characters, if any.
[:space:] Space characters: in the 'C' locale, this is tab, newline, vertical tab, form
feed,carriage return, and space.
[:upper:] Upper-case letters: in the 'C' locale and ASCII character encoding, this is A
B C D E F G H I J K L M N O P Q R S T U V W X Y Z.
[:xdigit:] Hexadecimal digits: 0 1 2 3 4 5 6 7 8 9 A B C D E F a b c d e f.
\b Match the empty string at the edge of a word.
\B Match the empty string provided it is not at the edge of a word.
\< Match the empty string at the beginning of word.
\> Match the empty string at the end of word.
\w Match word constituent. Synonym for '[_[:alnum:]]'.
\W Match non-word constituent. Synonym for '[^_[:alnum:]]'.
\s Match white space. Synonym for '[[:space:]]'.
\S Match non-whitespace. Synonym for '[^[:space:]]'.
```

### Grep
-i (run case-insensitive).
-v return lines that do not contain matches
-r recursive
-A / -B 
-e With multiple -e options used is logical OR.
* grep -e 'pam_unix' -e 'user root' -e 'Accepted publickey'
* grep -v '^[#;]' /etc/ethertypes