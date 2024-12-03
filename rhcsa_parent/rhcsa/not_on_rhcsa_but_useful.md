* The nologin shell acts as a replacement shell for the user accounts not intended to interactively
log into the system. It is wise from a security standpoint to disable an account from logging into
the system, when the account does not require it. For example, a mail server may require an
account to store mail and a password for the user to authenticate with a mail client used to retrieve
mail. That user does not need to log directly into the system.
A common solution to this situation is to set the user's login shell to /sbin/nologin. If the user
attempts to log in to the system directly, the nologin shell closes the connection.