* framework used for processing data streams in real time
* Plug kinesis streams or amazon MSK (managed kafka) -> kinesis analytics
* AWS will:
    * provision the infrastructure for you
    * manage the backups(checkpoints, snapshots)
    * use any Apache Flink features to transform the data


* FLINK CANNOT READ FROM FIREHOSE!!!!

* FIREHOSE CAN READ FROM FLINK!!!