* AWS managed service
* centrally manage and automate AWS backups across AWS services
* no need to create custom scripts and manual processes
* want a central view of your backup strategy
* supported services: all database related services, all file system services, and more


* supports cross region backups
    * can have your backup pushed to another region (disaster recovery)
* supports cross account backups


* supports point in time recovery (PITR) for supported services
* on demand and scheduled backups
* tag based backup policies
* you can create backup policies known as backup plans 
    * i.e. define frequency
    * backup window
    * transition to cold storage?
    * retention period of backups

### AWS backup vault lock
* option to enable
* enforce a WORM (write once read many) state for all the backups you store in your backup vault
* can't delete or modify backups
* even root user can't delete/modify backups when enabled
