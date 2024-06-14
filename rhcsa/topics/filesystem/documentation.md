## Documentation

* Locate, read, and use system documentation including man, info, and files in `/usr/share/doc`
    * man command, <command> --help, info/pinfo
        * see command list above
    * /usr/share/docs
        * some services put very useful info here

    * The *man* command can be used to view help for a command. To search for a command based on a keyword the *apropros* command or *man* with the -k option can be used. The *mandb* command is used to build the man database.

    * To search for a command based on a keyword in occurring in its man page:
        ```shell
        man -k <keyword>
        ```

    * The *whatis* command can be used to search for a command in the man database for a short description.

    * The *info* command provides more detailed information than the *man* command. 

    * The `/usr/share/doc` directory contains documentation for all installed packages under sub-directories that match package names followed by their version.

    * man
        * -k (keyword) (list of commands with that keyword)
        * -f (short description)
        * Manual

    * mandb
        * Update the mandb
    
    * info/pinfo
        * More detailed than man, is the replacement for man, has links and navigation across multiple pages while man only has single page, man page will display if no info page available

    * apropos
        * Search the command in the mandb, equivalent to man -k

    * whatis
        * Search the command in the mandb for description


## Exam Objectives

### Locate, read, and use system documentation including man, info, and files in /usr/share/doc 

    * **Using `man` (Manual Pages)**:
  * **Basic Command**:
    * `man command`: Displays the manual page for the specified command.
  * **Sections**:
    * Manual pages are divided into sections (1: User Commands, 2: System Calls, 3: Library Functions, etc.).
    * typically don't have to use this unless the search term appears in multiple sections
        * ex: passwd command vs passwd file
        
    * Example: `man 5 passwd` displays the manual page for the `passwd` file in section 5.
        * **Structured in Sections**:
        * **Section 1**: User Commands (e.g., `ls`, `grep`).
            * this is user commands
        * **Section 2**: System Calls (e.g., `open`, `read`).
            * lower level system calls
        * **Section 3**: Library Functions (e.g., `printf`, `malloc`).
            * lower level library calls
        * **Section 4**: Special Files (e.g., `/dev/null`).
            * special FILES on the system
        * **Section 5**: File Formats and Conventions (e.g., `/etc/passwd`).
            * explains FILES on the system
        * **Section 6**: Games and Screensavers.
        * **Section 7**: Miscellaneous (e.g., `man`, `regex`).
        * **Section 8**: System Administration Commands (e.g., `mount`, `ifconfig`).

  * **Searching**:
    * `/search_term`: Search for a term within the man page (press `n` for next occurrence).
    * `man -k keyword` or `apropos keyword`: Searches the man page descriptions for the specified keyword.
  * **Example**:
    * View the manual page for `ls`:
      ```bash
      man ls
      ```

* **Using `info` (Info Pages)**:
  * **Basic Command**:
    * `info command`: Displays the info page for the specified command, which often contains more detailed information than man pages.
  * **Navigation**:
    * `h`: Opens the help menu.
    * `Space`: Moves to the next page.
    * `b`: Moves to the previous page.
    * `q`: Quits the info page.
    * `m`: Opens the main menu (if available).
  * **Searching**:
    * `Ctrl+S`: Starts an incremental search.
  * **Example**:
    * View the info page for `bash`:
      ```bash
      info bash
      ```

* **Using `/usr/share/doc`**:
  * **Locating Documentation**:
    * System documentation for installed packages is often located in `/usr/share/doc`.
  * **Viewing Documentation**:
    * Use `ls` to list available documentation:
      ```bash
      ls /usr/share/doc
      ```
    * Use `cat`, `less`, or `more` to read documentation files:
      ```bash
      less /usr/share/doc/package/README
      ```
  * **Examples**:
    * List documentation for all installed packages:
      ```bash
      ls /usr/share/doc
      ```
    * Read the README file for a specific package:
      ```bash
      less /usr/share/doc/vim-common/README
      ```

* **Searching Documentation**:
  * **Using `man -k` or `apropos`**:
    * `man -k keyword` or `apropos keyword`: Searches for man pages related to the specified keyword.
    * Example:
      ```bash
      man -k password
      ```
  * **Using `locate`**:
    * `locate filename`: Finds the location of files with the specified name, useful for finding documentation files.
    * Example:
      ```bash
      locate README
      ```

