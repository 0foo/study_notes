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
