#### all the servcies 
* Rekognition: face detection, labeling, celebrity recognition
* Transcribe: audio to text (ex: subtitles)
* Polly: text to audio
* Translate: translate langauges
* Lex: build conversational bots – chatbots
* Connect: use Lex to build a cloud contact center 
* Comprehend: natural language processing(sentiment analysis, important sections, etc)
* SageMaker: machine learning for every developer and data scientist
* Kendra: ML-powered search engine for document collection
* Personalize: real-time personalized recommendations
* Textract: extract text and data in documents/images



#### Rekognition
* USE CASE 
    * identify and moderate

* USE CASE EXAMPLES:
    * labeling
    * content moderation
    * text detection!
    * face detection and analysis(gender, age, range, emotions)
    * face search/verification
    * celebrity recognition
    * pathing (sport game analysis of a video) 

* content moderation 
    * inappropriate, offensive, unwanted content
    * used in many applications to create a safer user experience
    * make sure images displayed don't show anything offensive

* set minimum confidence threshold for things to be flagged 
    * either for identificatioan or for moderation

* can do a human manual review in A2I
    * amazon augmented A2
    * select optional manual review


#### Sagemaker
* fully managed service to develop machine learning models 
* intended for developers and data scientists
* collect a lot of data and feed into sagemaker
* label that data, train/tune that data
* can save that model and use it with future data



#### Personalize
* on exam: when see ML service for personalized reccomendations
* fully managed ML service to build apps with real time personalized reccomendations
* customized direct marketing
* same technology used by Amazon.com ( the reccomendation services )
* s3(non realtime) or personalize API(real time) -> personalize
* outputs can be websites, email, mobile, SMS, etc.



### All of these are text/document/speech based

#### Textract
* extracts text from scanned documents(many formats pdfs, images, etc) or handwriting
* can get it as a data file i.e. JSON or something
* can even have forms tables 
* finanical sector, health care, public sector,etc


#### Transcribe
* automatically convert speech to text
* pass in audio and get text back

* automatically remove an PII (personal identifying information) using redaction
    * name, ssn, etc

* supports automatic language identification for multi-lingual audio

 * search, transcribe, automate subtitles, translate into multiple languages
 
* does not user NLP is purely a speech to text with no understanding

#### Polly
* turn text into speech using deep learning
* create applications that will talk
* Lexicon
    * a metadata file you define and upload to the screen with the text
    * customize pronunciation of works with customized lexicon
    * example: can customize it to pronounce 3's as E and 4's as h: St3ep4ne
    * example: can make it say Amazone Web Services any time is sees: AWS
    * upload your defined lexicon and use in synthesize speech operation
    
* SSML
    * literally XML tags added to the written text to indicate functions the speaker should do
        * <break time= "1 second">
    * speech synthesis markup language
    * enables more customization in how speech is made and pronounced
    * emphasize specific words or phrases
    * include breathing sounds/whispering/news caster style/phonetic pronuncaiation/emphazise specific words/phrases/etc.



#### Translate
* simply a service to translate from one language to another at scale


#### Lex
* convert speech to text
* understands language, (natural language understanding) to recognize the intent of speech/text
* helps build chat bots/call center bots


### Amazon connect
* recieve calls, create contact flows, cloud based virtual contact center
* can integrate with other CRM's or other services in AWS
* way cheaper than traditional call center operations
* FLOW:
    * phone call to an Amazon Connect provided number
    * customer calls amazon connect
    * Lex streams all the info from this call and understands the intent of the call
    * Will invoke the right lambda function based on what it hears
    * i.e. an appointment scheduler lambda function that will go into a CRM and schedule a meeting

### Amazon Comprehend
* natural language processing (NLP)
* anytime see NLP on examp think comprehend
* fully managed and serverless service
* uses machine learning to find insights/relationships in text
* USE CASES:
    * langauges, key phrases, places, people, brands or events
    * sentiment analysis to understand how positibe of negative the text is
    * analyze text using tokenization and parts of speech
    * organize a collection of text files by topic 
* EXAMPLES:
    * anaylize customer interactions, emails, etc to find what leads to positive/negative customer experience
    * create and group topics that comprehend will discover


### Amazon Comprehend Medical
* can extract patient info, clinical info, etc
* can detect PHI (protected health information) (using NLP)
    * detectPHI API
* from copy/past text,  S3, kinesis, transcribe, etc  -> Comprehend Medical
* get insights



### KEndra
* when see document serach service on Exam think Kendra
* fully managed document search service powered by machine learning
* many many formats (i.e. pdf, txt, html, powerpoint, etc.)
* can connect and use many data sourced (google drive, box, s3, RDS, etc)
* will index the document
* builds an knowedge index powered by machine learning ]
* User can ask a question: where is the tech department, and Kendra can check it's knowledge base and reply
* 