### Whats in audit logs

### Contents of Audit Logs

Audit logs contain records of various system events that are monitored by the `auditd` service. These events can include security-related actions, system calls, file access, network activity, and more. Each log entry provides detailed information about the event, such as the time of occurrence, user involved, type of event, and result of the action.

### Common Types of Events Logged

* **System Calls**:
    * Records details about system calls made by processes.
    * Example: File operations like open, read, write, and close.

* **File Access**:
    * Logs events related to file access and modifications.
    * Example: Creation, deletion, modification of files.

* **User Actions**:
    * Tracks user actions such as login, logout, and authentication attempts.
    * Example: Successful and failed login attempts.

* **SELinux Denials**:
    * Logs Security-Enhanced Linux (SELinux) policy violations.
    * Example: Denial of access to a file due to SELinux policy.

* **Process Information**:
    * Records details about process execution.
    * Example: Starting and stopping of processes.

* **Network Activity**:
    * Monitors network-related events.
    * Example: Connections and communications between systems.

* **Administrative Actions**:
    * Tracks administrative actions and commands.
    * Example: Use of `sudo` to execute privileged commands.


### Location of Audit Logs

The audit logs on a Linux system are typically stored in the `/var/log/audit/` directory.

* Main Audit Log File
    * The main audit log file is usually:
        * `/var/log/audit/audit.log`


### `ausearch` Command Tutorial

The `ausearch` command is part of the `audit` package, used to search the audit logs in Linux systems. It provides a powerful way to filter and find specific events in the audit logs.

### Basic Usage

* Search for All Events
    * `ausearch -a all`

### Common Options

* Search by Event ID
    * `ausearch -a event_id`
    * Example: `ausearch -a 12345`

* Search by User ID
    * `ausearch -ua uid`
    * Example: `ausearch -ua 1000`

* Search by Username
    * `ausearch -ua username`
    * Example: `ausearch -ua alice`

* Search by Date and Time
    * `ausearch -ts start_time -te end_time`
    * Example: `ausearch -ts recent`  *Search from the most recent time*
    * Example: `ausearch -ts 07/01/2024 08:00:00 -te 07/01/2024 17:00:00`  *Search from 8 AM to 5 PM on July 1, 2024*

* Search by Key
    * `ausearch -k key_name`
    * Example: `ausearch -k login`

* Search by System Call
    * `ausearch -sc syscall`
    * Example: `ausearch -sc execve`

* Search by Message Type
    * `ausearch -m message_type`
    * Example: `ausearch -m AVC`  *Search for SELinux denials*

### Combining Options

* Search by Multiple Criteria
    * `ausearch -ua username -ts recent -m message_type`
    * Example: `ausearch -ua alice -ts recent -m AVC`

### Examples

1. **Search for All Events Related to a Specific User:**
    ```sh
    ausearch -ua alice
    ```

2. **Search for Events by a Specific Event ID:**
    ```sh
    ausearch -a 12345
    ```

3. **Search for Events in a Specific Time Range:**
    ```sh
    ausearch -ts 07/01/2024 08:00:00 -te 07/01/2024 17:00:00
    ```

4. **Search for SELinux Denials:**
    ```sh
    ausearch -m AVC
    ```

5. **Search for Events with a Specific Key:**
    ```sh
    ausearch -k login
    ```

### Output Options

* Show Detailed Information
    * `ausearch -i`
    * This option interprets the output for readability.

### Example with Detailed Output

* Search for Recent SELinux Denials with Detailed Information:
    ```sh
    ausearch -m AVC -ts recent -i
    ```

### Summary

* `ausearch` is a powerful tool to search and filter audit logs.
* Common options include searching by event ID, user ID, username, date/time, key, system call, and message type.
* Use `-i` for detailed, human-readable output.


