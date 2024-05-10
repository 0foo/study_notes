### Storage


* Logical Block Addressing
    * abstracts away cylinders and heads and just allows accessing the harddrive in contiguous linear storage units
    * block size
    * block number 
    * find your block size: `lsblk -o NAME,PHY-SeC`
    * dd uses this with it's -bs(blocksize) paramter


* CHS is an earlier form of hard disk addressing. It stands for:
    * C: cylinder, the valid range is between 0 and 1023 cylinders.
    * H: Head, the valid range is between 0 and 254 heads (formerly 0-15).
    * S: Sector, the valid range is between 1 and 63 sectors.
