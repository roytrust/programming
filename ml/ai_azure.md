
* [Master the basics of Azure: AI Fundamentals](https://docs.microsoft.com/en-us/users/23110622/collections/0kjyh8rn55yknr)
* Responsible AI: fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability

### What is AI?
Simply put, AI is the creation of software that imitates human behaviors and capabilities. Key workloads include:

* Machine learning - This is often the foundation for an AI system, and is the way we "teach" a computer model to make prediction and draw conclusions from data.
* Anomaly detection - The capability to automatically detect errors or unusual activity in a system.
* Computer vision - The capability of software to interpret the world visually through cameras, video, and images. For example: image classification, object detection, semantic segmentation, image analysis, face detection-analysis-recognition, OCR (optical character recognition)
* Natural language processing - The capability for a computer to interpret written or spoken language, and respond in kind.
* Knowledge mining - The capability to extract information from large volumes of often unstructured data to create a searchable knowledge store.

### How machine learning works
* Data scientists can use all of that data to train machine learning models that can make predictions and inferences based on the relationships they find in the data.
* 

### Computer Vision
* Describing an image
* Tagging visual features
* Detecting objects: identify and locate specific types of object in an image or camera feed. Return a class label, probability, and bounding box for each ojbect in the image.
* Detecting brands
* Detecting faces
* Categorizing an image
* Detecting domain-specific content
* Optical character recognition
* Detect image types. Detect image color schemes. Generate thumbnails. Moderate content.

### NLP: Natural Language Processing
* The Language service provides advanced natural language processing over raw text, and includes four main functions: sentiment analysis, key phrase extraction, language detection, and named entity recognition.
* Speech cognitive: recognize and synthesize speech. Speech-to-Text, Text-to-Speech API. 
  * Speech recognition: 1. An acoustic model that converts the audio signal into phonemes (representations of specific sounds). 2. A language model that maps phonemes to words, usually using a statistical algorithm that predicts the most probable sequence of words based on the phonemes.
  * Speech synthesis: the system typically tokenizes the text to break it down into individual words, and assigns phonetic sounds to each word. It then breaks the phonetic transcription into prosodic units (such as phrases, clauses, or sentences) to create phonemes that will be converted to audio format. These phonemes are then synthesized as audio by applying a voice, which will determine parameters such as pitch and timbre; and generating an audio wave form that can be output to a speaker or written to a file.
* Translation: The **Translator** service, which supports text-to-text translation. The **Speech** service, which enables speech-to-text and speech-to-speech translation.

### Others
* **Anomaly Detector**: identifies anomalies that exist outside the scope of a boundary. The boundary is set using a sensitivity value. By default, the upper and lower boundaries for anomaly detection are calculated using concepts known as **expectedValue, upperMargin, and lowerMargin**. The upper and lower boundaries are calculated using these three values. If a value exceeds either boundary, it will be identified as an anomaly. You can adjust the boundaries by applying a marginScale to the upper and lower margins as demonstrated by the following formula. _upperBoundary = expectedValue + (100 - marginScale) * upperMargin_
* **Cognitive Search**: data from any source, full text search and analysis, AI powered search, Multi-lingual, Geo-enabled, Congiurable user experience. 
  * Index, Indexer, Knowledge store (table projections, object projections, file projections), skillset 
  * **Natural language processing skills**: key phrase extraction, text translation skill.
  * **Image processing skills**: Image analysis skill, Optical character recognition skill.
  * 
