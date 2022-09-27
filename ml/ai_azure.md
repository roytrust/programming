
* [Master the basics of Azure: AI Fundamentals](https://docs.microsoft.com/en-us/users/23110622/collections/0kjyh8rn55yknr)
* [Foundations of data science for machine learning](https://docs.microsoft.com/en-us/learn/paths/machine-learning-foundations-using-data-science/)
* [Azure Data Scientist Associate dp-100](https://learn.microsoft.com/en-us/certifications/azure-data-scientist/)
* [ML Exercises](https://microsoftlearning.github.io/mslearn-dp100/)
* Responsible AI: fairness, reliability and safety, privacy and security, inclusiveness, transparency, accountability
* [Algorithm Cheat Sheet](https://docs.microsoft.com/en-us/azure/machine-learning/algorithm-cheat-sheet)
* [Sandbox](https://docs.microsoft.com/en-us/learn/modules/build-cosmos-db-app-with-vscode/2-setup-cosmosdb)
* [Python Statistics Fundamentals](https://realpython.com/python-statistics/)

## Azure Machine Learning
* datastores: Azure Storage (blob and file containers), Azure Data Lake stores, Azure SQL Database, Azure Databricks file system (DBFS)
* dataset: tabular, file
* Pipeline steps: PythonScriptStep, DataTransferStep, DatabricksStep, AdlaStep, ParallelRunStep. OutputFileDatasetConfig. ScheduleRecurrence, Schedule

### [Tune hyperparameters](https://learn.microsoft.com/en-us/training/modules/tune-hyperparameters-with-azure-machine-learning/)
  * *search space*: the set of hyperparameter values tried during hyperparameter tuning
  * *Discrete hyperparameters*: qnormal, quniform, qlognormal, qloguniform
  * *Continuous hyperparameters*: normal, uniform, lognormal, loguniform
  * *Grid sampling*: can only be employed when all hyperparameters are discrete, and is used to try every possible combination of parameters in the search space.
  * *Random sampling* is used to randomly select a value for each hyperparameter, which can be a mix of discrete and continuous values.
  * *Bayesian sampling* chooses hyperparameter values based on the Bayesian optimization algorithm, which tries to select parameter combinations that will result in improved performance from the previous selection.
  * (Configuring early termination) *bandit policy* to stop a run if the target performance metric underperforms the best run so far by a specified margin.
  * *median stopping policy* abandons runs where the target performance metric is worse than the median of the running averages for all runs.
  * *truncation selection policy* cancels the lowest performing X% of runs at each evaluation interval based on the truncation_percentage value you specify for X.
  * (Running a hyperparameter tuning experiment) HyperDriveConfig  
    a training script for hyperparameter tuning: Include an argument for each hyperparameter you want to vary; Log the target performance metric.
  * `best_run = run.get_best_run_by_primary_metric(); best_run_metrics = best_run.get_metrics(); script_arguments = best_run.get_details() ['runDefinition']['arguments']`
* Differential Privacy. opendp.smartnoise: Upper and lower bounds, Sample size, Epsilon

### [Explain machine learning models](https://learn.microsoft.com/en-us/training/modules/explain-machine-learning-models-with-azure-machine-learning/)
* Model explainers use statistical techniques to calculate **feature importance**. This enables you to quantify the relative influence each feature in the training dataset has on label prediction. Explainers work by evaluating a test data set of feature cases and the labels the model predicts for them.
* *Global feature importance* quantifies the relative importance of each feature in the test dataset as a whole. It provides a general comparison of the extent to which each feature in the dataset influences prediction.
* *Local feature importance* measures the influence of each feature value for a specific individual prediction.  
  For a multi-class classification model, a local importance values for each possible class is calculated for every feature, with the total across all classes always being 0. 
* **MimicExplainer** - An explainer that creates a global surrogate model that approximates your trained model and can be used to generate explanations. This explainable model must have the same kind of architecture as your trained model (for example, linear or tree-based).
* **TabularExplainer** - An explainer that acts as a wrapper around various SHAP explainer algorithms, automatically choosing the one that is most appropriate for your model architecture.
* **PFIExplainer** - a Permutation Feature Importance explainer that analyzes feature importance by shuffling feature values and measuring the impact on prediction performance.


## Fundations
### Machine learning
* The goal of machine learning is to find patterns in data and use these patterns to make estimates.
* Machine learning differs from normal software development in that we use special code, rather than our own intuition, to improve how well the software works.
* The learning process conceptually uses four components:
  * **Data** about the topic we're interested in.
  * A **model**, which makes estimates.
  * An **objective** the model is trying to achieve.
  * An **optimizer**, which is the extra code that changes the model depending on its performance.
* Data can be thought of as features, and labels. Features correspond to potential model inputs, while labels correspond to model outputs, or desired model outputs.
* The goal of training is to improve a model so that it can make high-quality estimations or predictions. Once trained, you can use a model in the real world like normal software.
* Models don’t train themselves. They're trained using data plus two pieces of code, the __objective function__ and the __optimizer__. 
* The **objective** is what we want to the model to be able to do. So that a computer can understand our objective, we need to provide our goal as code snippet called an **objective function** (also known as **cost function**). Objective functions judge whether the model is doing a good job.
* During training, the model makes a prediction, and the objective function calculates how well it performed. The optimizer is code that then changes the model’s parameters so the model will do a better job next time.
* It's important to keep in mind that the objective, data, and optimizer are simply a means to train the model. They are not needed once training is complete. It's also important to remember that training only changes the parameter values inside of a model; it doesn't change what kind of model is used. 
* Error, cost, and loss - loosely interchangeable
* **Gradient descent** is an optimization algorithm. It's way of calculating how to improve a model, given a cost function and some data.
* **Step size (learning rate)** changes how quickly and how well gradient descent performs.

* **About data**: Aren't just large, but representative, Don't contain errors, Aren't missing key information
* **One-hot encoding** is a way to encode categorical data ... each available category gets its own single column, and a given row only contains a single 1 in the category it belongs to.
* **Statistical power** refers to a model’s ability to reliably identify real relationships between features and labels.
* A **population** is all possible data we care about. A **sample** is the subset of that data which we actually have on hand.
* What makes a **good dataset**? contains relevant information, is complete, is a good representation of the population (real-world).




### What is AI?
Simply put, AI is the creation of software that imitates human behaviors and capabilities. Key workloads include:

* Machine learning - This is often the foundation for an AI system, and is the way we "teach" a computer model to make prediction and draw conclusions from data.
* Anomaly detection - The capability to automatically detect errors or unusual activity in a system.
* Computer vision - The capability of software to interpret the world visually through cameras, video, and images. For example: image classification, object detection, semantic segmentation, image analysis, face detection-analysis-recognition, OCR (optical character recognition)
* Natural language processing - The capability for a computer to interpret written or spoken language, and respond in kind.
* Knowledge mining - The capability to extract information from large volumes of often unstructured data to create a searchable knowledge store.
* **How machine learning works**: Data scientists can use all of that data to train machine learning models that can make predictions and inferences based on the relationships they find in the data.

### Automated machine learning
* automatically tries multiple pre-processing techniques and model-training algorithms in parallel. Classification, Regression, Time series forecasting
* Input: dataset, target metric, time/cost constraint
* **cross-validation**: after the model is trained using a portion of the data, the remaining portion is used to iteratively test, or cross-validate, the trained model. The metric is calculated by comparing the predicted value from the test with the actual known value, or label.
* The difference between the predicted and actual value, known as the **residuals**, indicates the amount of error in the model. 
 
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

* Read text: OCR API (Regions, lines, words), Read API (Pages, lines, words)

### Custom Vision
* Image classification: Product identification, Disaster investigation, Medical diagnosis
* Object detection: Checking for building safety, Driving assistance, Detecting tumors. Return class, probability score, coordinates of a bounding box

### NLP: Natural Language Processing
* The **Language service** provides advanced natural language processing over raw text, and includes four main functions: **sentiment analysis, key phrase extraction, language detection, and named entity recognition**.
* **Speech cognitive service**: recognize and synthesize speech. Speech-to-Text, Text-to-Speech API. 
  * Speech recognition: 1. An acoustic model that converts the audio signal into phonemes (representations of specific sounds). 2. A language model that maps phonemes to words, usually using a statistical algorithm that predicts the most probable sequence of words based on the phonemes.
  * Speech synthesis: the system typically tokenizes the text to break it down into individual words, and assigns phonetic sounds to each word. It then breaks the phonetic transcription into prosodic units (such as phrases, clauses, or sentences) to create phonemes that will be converted to audio format. These phonemes are then synthesized as audio by applying a voice, which will determine parameters such as pitch and timbre; and generating an audio wave form that can be output to a speaker or written to a file.
* Translation: The **Translator** service, which supports text-to-text translation. The **Speech** service, which enables speech-to-text and speech-to-speech translation.
* **Conversational Language Understanding**: Utterances, Entities, Intents.  the **None** intent is created but left empty on purpose. The None intent is a required intent and can't be deleted or renamed. **Authoring**
* **Bot service**: 
  * A **knowledge base** of question and answer pairs - usually with some built-in natural language processing model to enable questions that can be phrased in multiple ways to be understood with the same semantic meaning. **question answering feature**
  * A **bot service** that provides an interface to the knowledge base through one or more channels.

### Others
* [**Face service**](https://docs.microsoft.com/en-us/learn/modules/detect-analyze-faces/2-face-analysis-azure): Face Detection, Face Verification, Find Similar Faces, Group faces based on similarities, Identify people
* **Form Recognizer service**: Matching field names to values, Processing tables of data, Identifying specific types of field, such as dates
* **Anomaly Detector**: identifies anomalies that exist outside the scope of a boundary. The boundary is set using a sensitivity value. By default, the upper and lower boundaries for anomaly detection are calculated using concepts known as **expectedValue, upperMargin, and lowerMargin**. The upper and lower boundaries are calculated using these three values. If a value exceeds either boundary, it will be identified as an anomaly. You can adjust the boundaries by applying a marginScale to the upper and lower margins as demonstrated by the following formula. _upperBoundary = expectedValue + (100 - marginScale) * upperMargin_
  * Batch: Flat trend, Seasonal time series data , real-time detection
* **Cognitive Search**: data from any source, full text search and analysis, AI powered search, Multi-lingual, Geo-enabled, Congiurable user experience. 
  * Index, Indexer, Knowledge store (table projections, object projections, file projections), skillset 
  * **Natural language processing skills**: key phrase extraction, text translation skill.
  * **Image processing skills**: Image analysis skill, Optical character recognition skill.
  *  the index stores its name, the data type, and supported behaviors for the field such as, is the field searchable, can the field be sorted?

## References 
* [Statistics By Jim](https://statisticsbyjim.com/)
* 
