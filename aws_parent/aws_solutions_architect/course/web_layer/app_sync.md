* when see graphQL or access to real time data on exam, think app sync

* Managed service that uses graphQL
* Can integrate with all kinds of data sources
    * relational, http apis, dynamo, elastic search, many more
    * custom sources with lambda
* retrieve data in real time with Web Sockets or MQTT on websocket
    * know this real time aspect for the exam
* monitor with cloud watch


 * mobile apps


 * clients-> can be anything from mobile to web to offline sync to realtime dashboards
    * think REALTIME
 

* schemas
    * defines the structure of data and operations (queries, mutations, and subscriptions) for your AppSync API. It serves as the blueprint for how clients can interact with the API

 * resolvers
    * the connecting code to the data source 
    * connect the operations defined in the schemas to the dtaa source

* app sync can sync with cognito
    * can set roles and allowed actions like allowing a blogger to post but not a reader