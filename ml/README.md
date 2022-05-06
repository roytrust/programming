1. [AI & Azure](ai_azure.md)
1. [ML hands-on](ml_handson.md)
1. [Linear algebra](linear_algebra.md)

## Concepts and Tips
* **Machine learning** is a technique that uses mathematics and statistics to create a model that can predict unknown values.
* Reinforcement Learning
* Feedback loop
* Clustering: identify similar instances and assign them into clusters, or group of similar instances. 
* A common approach to finding the right hyperparameter values is to use grid search.
*
### Models
* **Regression** is a supervised machine learning technique used to predict numeric values. 
* **Classification** is a supervised machine learning technique used to predict categories or classes.


### Evaluate a regression model
* **Mean Absolute Error (MAE)**: The average difference between predicted values and true values. This value is based on the same units as the label, in this case dollars. The lower this value is, the better the model is predicting.
* **Root Mean Squared Error (RMSE)**: The square root of the mean squared difference between predicted and true values. The result is a metric based on the same unit as the label (dollars). When compared to the MAE (above), a larger difference indicates greater variance in the individual errors (for example, with some errors being very small, while others are large).
* **Relative Squared Error (RSE)**: A relative metric between 0 and 1 based on the square of the differences between predicted and true values. The closer to 0 this metric is, the better the model is performing. Because this metric is relative, it can be used to compare models where the labels are in different units.
* **Relative Absolute Error (RAE)**: A relative metric between 0 and 1 based on the absolute differences between predicted and true values. The closer to 0 this metric is, the better the model is performing. Like RSE, this metric can be used to compare models where the labels are in different units.
Coefficient of Determination (R2): This metric is more commonly referred to as R-Squared, and summarizes how much of the variance between predicted and true values is explained by the model. The closer to 1 this value is, the better the model is performing.

### [Evaluate a classification model](https://docs.microsoft.com/en-us/learn/modules/create-classification-model-azure-machine-learning-designer/evaluate-model)
* **confusion matrix**: a tabulation of the predicted and actual value counts for each possible class.
* **Accuracy**: The ratio of correct predictions (true positives + true negatives) to the total number of predictions. In other words, what proportion of diabetes predictions did the model get right?
* **Precision**: The fraction of positive cases correctly identified (the number of true positives divided by the number of true positives plus false positives). In other words, out of all the patients that the model predicted as having diabetes, how many are actually diabetic?
* **Recall**: The fraction of the cases classified as positive that are actually positive (the number of true positives divided by the number of true positives plus false negatives). In other words, out of all the patients who actually have diabetes, how many did the model identify?
* **F1 Score**: An overall metric that essentially combines precision and recall.
* **ROC** curve (receiver operating characteristic). **Threshold**. **True positive rate**. **False positive rate**
* The larger the area under the curve (which can be any value from 0 to 1), the better the model is performing - this is the **AUC** metric listed with the other metrics below.

## 12 Key Factors
* Data qualiy
* Automation
* Monitor, keep up-to-date
* Algorithm
* Infra, cloud
* libs: SciPy, scikit-learn, 

## Further reading
* [6 Python Libraries to Interpret Machine Learning Models and Build Trust](https://www.analyticsvidhya.com/blog/2020/03/6-python-libraries-interpret-machine-learning-models/)
* [Decoding the Black Box: An Important Introduction to Interpretable Machine Learning Models in Python](https://www.analyticsvidhya.com/blog/2019/08/decoding-black-box-step-by-step-guide-interpretable-machine-learning-models-python/?utm_source=blog&utm_medium=6-python-libraries-interpret-machine-learning-models)

