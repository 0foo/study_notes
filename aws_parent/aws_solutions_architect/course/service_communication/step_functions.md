* workflow orchestration
* have deep integration with numerous other services
* represent flow as json state machine
* integrate with TONS of aws services

#### Trigger 
* management console
* AWS SDK
* cli
* AWS lambda (startExecution API call via SDK)
* API gateway
* Event Bridge
* Code Pipeline
* other stepfunctions



#### Tasks
* lambda task: invoke lambda function
* activity task
    * set up an http activity worker
    * activity worker will poll the step function service and see if there's something for it to do
    * After receiving a task, the worker processes it and sends the result back using the SendTaskSuccess, SendTaskFailure, or SendTaskHeartbeat APIs.
* service tasks
    * connect to a supported AWS service
    * i.e. lambda, ECS, Fargate, Dynamo, etc.
* wait task
    * wait for a duration

* very common exam question: DOES NOT INTEGRATE WITH MECHANICAL TURK
    * have to use ASWF instead of step functions


#### Workflows
* two types: standar and express

* Express: fast, high throughput workloads, cheaper, with short duration
* Standard: longer, slower, more reliable/durable, with longer potential duration

* Two types of Express workflow
    1. Syncronous
        * client wait until workflow completes then return result
        * i.e. api gateway calling a sync workflow, waiting, returning response to client
    2. Asyncronous
        * client don't wait for workflow for comlete, just send and forget
        * i.e. promises
        * used if client doesn't need immediate response/result
        * i.e. api gateway kicks off a workflow and doesn't wait for completion

* Don't have to know the following, just here for reference
    * Execution Duration:
    * Standard: Up to 1 year.
    * Express: Up to 5 minutes.

    * Execution Volume:
    * Standard: Designed for low to moderate execution volumes (e.g., workflows with critical state tracking and retries).
    * Express: Designed for high-volume workloads (e.g., millions of executions per second, like event-driven applications).

    * Pricing Model:
    * Standard: Charges per state transition.
    * Express: Price on number of executions,  duration of executions, and memory consumption (is cheaper)

    * Performance and Scalability:
    * Standard: Scales for moderate concurrency with exact-once execution.
    * Express: Scales for extremely high concurrency with at-least-once execution (potential for duplicate processing).

    * State Durability:
    * Standard: Each state is durably persisted, making it more suitable for workflows requiring high reliability.
    * Express: Optimized for speed, so state is not durably persisted between steps.

#### Error handling
* enable error handling, retries, and add alerting to Step Function State Machine
* best practice: setup eventbridge to alert via email if statemachine function fails

* can add retry blocks