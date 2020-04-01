
## Training Models
### Linear regression
* Simply computing a weighted sum of the input features, plus a constant called the bias term (intercept term).
* Find the value of theta that minimizes the **RMSE/MSE**.
* **Normal Equation**, closed-form equation that directly computes the model parameters that best fit the model to the training set (minimize the **cost function**).
* **Singular value decomposition (SVD)**. np.linalg.pinv, svd.
* **Gradient dissident (GD)**, iterative optimization.
* **Learning rate** hyperparameter, size of the steps. To find a good learning rate, you can use grid search.
* **Global/Local minimum**
* MSE cost function: **convex function**
* For gradient descent, ensure a similar scale, StandardScaler.
* **Batch gradient descent**, Partial derivative. Scale well with the number of features.
* Number of iterations to reach optimal solution, **tolerance**, convergence rate.
* **Stochastic gradient descent**. Simulated annealing, Learning schedule function to determine the learning rate. SGDRegressor.
* **Mini-batch gradient descent.

### Polynomial regression
* PolynomialFeatures.
### Learning curves
* If a model performs well on the training data but generalizes poorly according to the cross-validation metrics, then your model is over fitting. If it performs poorly on both, then it is underfitting.
* Learning curves: plots of the model's performance on the training set and the validation set as a function of the training set size (or the training iteration).
* If your model is underfitting the training data, ddding more training examples will not help. You need to use a more complex model or come up with better features.
* The gap between the curves, the hallmark of an overfitting model.
* One way to improve an overfitting model is to feed it more training data until the validation error reaches the training error.
### The bias/variance trade-off
* A model's generalization error can be expressed as the sum of 3 very different errors.
* **Bias**. This part of the generalization error is due to wrong assumption, such as assuming that the data is linear when it is actually quadratic. A high bias model is most likely to underfit the training data.
* **Variance**. This part is due to the model's excessive sensitivity to small variation in the training data. A model with many degrees of freedom, such as a high degree polynomial model, is likely to have high variance and thus overfit the training data.
* **Irreducible erroe**. This part is due to the noisiness of the data itself. The only way to reduce this part of the error is to clean up the data.
* increasing a model's complexity will typically increase its variance and reduce its bias. Conversely, reducing a model's complexity increases its bias and reduces its variance. This is why it is called a trade-off.
### regularized linear models
* Constrain the weight of the model
* **Ridge regression**. Keep the model weights as small as possible. The regularization term should only be added to the cost function during training.

## Fundamentals of machine learning
### What is machine learning?
* The science (and art) of programming computers so that they can learn from data.
* Field of study that gives computers the ability to learn without be explicitly programmed.
* A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E.

### Machine learning is great for
* Problems for which existing solutions require a lot of fine-tuning or long list of rules.
* Complex problems for which using a traditional approach yields no good solution.
* Fluctuating environments.
* Getting insights about complex problems and large amounts of data.

### Examples of applications
* Analyzing images of products on a production line to automatically classify them.
* Detecting tumors in brain scans.
* Automatically classify news articles.
* Automatically flagging offensive comments on discussion forums.
* Summarizing long documents automatically.
* Creating a chatbot or a personal assistant.
* Forecasting your company's revenue next year based on many performance matrics.
* Making your app react to voice commands.
* Detecting credit card fraud.
* Segmenting clients based on their purchases so that you can design a different marketing strategy for each segment.
* Representing a complex high-dimensional dataset in a clear and insightful diagram.
* Building an intelligent bot for a game.

### Type of machine learning systems
* Supervised/Unsupervised learning
* Semisupervised learning. Photo
* Reinforcement learning. Agent, rewards/penalties, best strategy/policy.
* Batch and online learning. Out-of-core learning. Incremental learning. Learning rate.
* Instant-based versus model-based learning. Generalize.

### Main challenges of machine learning
* Insufficient quantity of training data. The ureasonable effectiveness of data.
* Nonrepresentative training data. Sampling noise, sampling bias.
* Poor-quality data
* Irrelevant features. Feature engineering: feature selection, feature extraction, create new features by gathering new data.
* Overfitting the training data. 
 * Regularization: Constraining a model to make it simpler and reduce the risk of overfitting. 
  * Solutions: simplify the model by selecting one with fewer parameters; gather more training data; Reduce the noise in the training data.
  * Hyperparameter: The amount of regulazition to apply during learning.
* Underfitting the training data.

### Testing and validating
* Generalization error: error rate on new cases. Out-of-sample error.
* Hyperparameter tuning and model selection. Holdout validation, validation set, dev set, cross-validation
* Data mismatch. Train-dev set


## End-to-End machine learning project
### 1. Frame the problem and look at the big picture
* Business objective. Classification/regression. 
* Select a performance measure. RMSE, MAE
### 2. Get the data
* quick check. `df["col"].value_counts()`; `df.hist(bins=50, figsize=(20,15)); plt.show()`
* create test set. Data snooping bias. pd.cut. StratifiedShuffleSplit. np.random.permutation

### 3. Explore the data. Discover and visualize the data to gain insights.
* correlation. Standard correlation coefficient.
```
cm=df.corr(); 
cm["col"].sort_values(ascending=False); 
from pandas.plotting import scatter_matrix
scatter_matrix(attr, figsize=(12,8))
```
* Experimenting with attribute combinations

### 4. Prepare the data for machine learning algorithms
* Write functions for all data transformations.
* Data cleaning. Fix or remove out outliers. Fill in missing values or drop the rows/columns. dropna, fillna, SimpleImputer, statistics_
* Feature selection. Drop no useful info.
* Feature engineering. 
  * Discretize continuous features. 
   * Decompose features (categorical, date). 
   * Add promising transformations of features (log(x)). 
   * Aggregate features into promising new features.
   * BaseEstimator, TransformerMixin
* Feature scaling. Standardize or normalize features.  
MinMaxScalar, StandardScalar.
* Handling text and categorical attributes.  
  `OrdinalEncoder; one-hot encoding, dummy attributes, OneHotEncoder`.  
  Alternatively, you could replace each category with a learnable, low dimensional vector called an embedding. Each category's representation will be learned during training, Representation learning.
* Transformation pipeline. Pipeline

### 5. Select and train a model. Shortlist promising models.
* LinearRegression, DecisionTreeRegressor, RandomForestRegressor
* Fix underfitting: Select a more powerful model, feed the training algorithm with better features, reduce constraints on the model.
* Better evaluation using cross validation.  
  cross_val_score

### 6. Fine tune the model
* Grid search. GridSearchCV, best_estimator_, cv_results_. Find out feature
* Randomized search. RandomizedSearchCV
* Ensemble methods.
* Analyze the best models and their errors.  
best_estimator_.feature_importances_
* Evaluate your system on the test set. Confidence interval for the generalization error scipy.stats.T.interval  
Don't tweak your model after measuring the generalization error: you would just start overfitting the test set.

### 7. Present your solution
* Document what you have done.
* Story telling presentation.
* Explain why your solution achieves the business objective.
* Present interesting points you noticed along the way.  
Describe what worked and what did not. List your assumptions and your system's limitations.
* Ensure your key findings are communicated through beautiful visualizations or easy-to-remember statements.

### 8. Launch, monitor and main maintain your system
* Automation
* Beaware of slow degradation: model tend to "rot" as data evolves.
* Measuring performance may require a human pipeline, crowdsourcing.
* Also monitor your inputs' quality. Malfunctioning sensor, stale.
* Retrain your models on a regular basis on fresh data.

## Classification
### Training a binary classifier
* SGD: Stochastic gradient descent. SGDClassifier
* RandomForestClassifier
### Performance measures
* Measuring accuracy using cross-validation. cross_val_score(), K-fold
* Confusion matrix. cross_val_predict(), confusion_matrix().  
Each row in a confusion matrix represents an actual class, while each column represents a predicted class. The first row, negative class, the second row positive class.
* precision: The accuracy of the positive predictions, =TP/(TP+FP). 
* recall, also called sensitivity or the true positive rate (TPR), The ratio of positive instances that are correctly detected by the classifier, =TP/(TP+FN).
* Precission and recall. precision_score, recall_score, f1_score. 
* Precision/recall trade-off. Decision threshold. decision_function() returns score.
* precision, recalls, threshold = precision_recall_curve(). threshold[np.argmax(precision>=0.90)]. 
* The ROC Curve: Receiver operating characteristic. fpr, tpr, thresholds = roc_curve(). 
* AUC: Area and the curve. roc_auc_score()
* Prefer the PR curve whenever the positive class is rare or when you care more about the false positive than the false negative. Otherwise, use the ROC curve.

### Multiclass Classification
* one-versus-the-rest(OvR) strategy, one-versus-all
* one-versus-one, OvO strategy
* svm.SVC, decision_function(), classes_
* OneVsOneClassifier, OneVsRestClassifier(SVC())

### Error Analysis
* plt.matshow(conf_mx, cmap=plt.cm.gray)
### Multilabel Classification
* KNeighborsClassifier
### Multioutput Classification

## References
* [hands on notebooks] (https://github.com/ageron/handson-ml2/blob/master/index.ipynb)
* Artificial Intelligence: Foundations of Computational Agents, with Python resources. https://artint.info/index.html
* Deep Learning: http://www.deeplearningbook.org/
