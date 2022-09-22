
### Train and understand regression models
**Regression** identifies the strength of relationship between one or more features and a single label. fitting a trend line.
* **Simple linear regression** models a linear relationship between a single feature and a usually continuous label, allowing the label to be predicted by the feature. 
* **Fitting linear regression**: Regression typically aims to find the line that produces the least amount of error, where error here means the difference between the actual data point value, and the predicted value.
* **Multiple linear regression** models the relationship between several features and a single label.
  *  the model expects features to be independent is called a model assumption
* **R-squared**: R2 is a value between 0 and 1 that tells us how well a linear regression model fits the data. When people talk about correlations being strong, they often mean that the R2 value was large.
* R-squared limitations:
  * Because of how R2 is calculated, the more samples we have, the higher the R2. Not comparable if using different amounts of data.
  * R2 values don't tell us how well a model will work with new, previously unseen data.
  * R2 values don't tell us the direction of the relationship.
  * no universal criteria for what makes an R2 value “good enough”.
* **Polynomial regression** models relationships as a particular type of curve. 
  * A major advantage of polynomial regression is that it can be used to look at all sorts of relationships.
  * It can also be used where the label (y value) has no theoretical upper limit.
  * The major disadvantage to polynomial curves is that they often extrapolate poorly, when beyond training data.
  * nother disadvantage is that polynomial curves are easy to overfit.
  * In general, it's not recommended to extrapolate from a polynomial regression unless you have an a-priori reason to do so (which is only very rarely the case, so it's best to err on the side of caution, and never extrapolate from polynomial regressions!)
* 

### Train a simple linear regression model
```Python
import statsmodels.formula.api as smf
model = smf.ols(formula = formula, data = dataset).fit()
print("Intercept:", model.params[0], "Slope:", model.params[1])
print("R-squared:", model.rsquared)
model.summary()

```

### Refine and test machine learning models
* **Feature Scaling** is a technique that changes the range of values that a feature has. Doing so helps models learn faster and more robustly.
* **Normalization** means to scale values so that they all fit within a certain range – typically 0 – 1.
* **Standardization** is similar but instead, we subtract the mean of the values, and then divide by the standard deviation. After standardization, our mean value is zero, and about 95% of values fall between -2 and 2.  
  `data["standardized"] = (data.col - numpy.mean(data.col)) / (numpy.std(data.col))`
* A model has been **overfit** if it works better on the training data than it does on other data.
* The job of the **test dataset** is to check how well the model works; it doesn't contribute to training directly, also call a validation dataset.
  * if test performance stops improving during training, we can stop – there is no point in continuing.
  * we can use a test dataset after training. This gives us an indication of how well the final model will work when it sees ‘real-world’ data it hasn't seen before.
* **Two cost functions**: 
  * The first cost function is using the training dataset, just like we've seen before. This cost function is fed to the optimizer and used to train the model. 
  * The second cost function is calculated using the test dataset. This is used for us to check how well the model might work in the real world. The result of the cost function isn't used to train the model. To calculate this, we pause training, look at how well the model is performing on a test dataset, and then resume training.
* Train/test split
  ```
  from sklearn.model_selection import train_test_split
  import statsmodels.formula.api as smf
  from sklearn.metrics import mean_squared_error as mse
  
  train, test = train_test_split(dataset, train_size=0.7, random_state=21)
  
  formula = "label ~ feature"
  # Create and train the model
  model = smf.ols(formula = formula, data = train).fit()
  
  # Use the in-buit sklearn function to calculate the MSE
  correct_labels = train['rescues_last_year']
  predicted = model.predict(train['weight_last_year'])
  MSE = mse(correct_labels, predicted)
  print('MSE = %f ' % MSE)
  
  correct_labels = test['rescues_last_year']
  predicted = model.predict(test['weight_last_year'])
  MSE = mse(correct_labels, predicted)
  ```
* The **hold-out approach** is like train-and-test, but instead of splitting a dataset into two, it's split into three: training, test—also known as validation—and hold-out.
* **Statistical approaches**: Simpler models that have originated in statistics often don't need test datasets. Instead, what degree the model is overfit can be calculated directly as statistical significance: a ‘p-value’.
* When building models, it's important to test them using different train/test splits. Simply assigning more data to the train set doesn't always guarantee the best results.
* 

### [Train and evaluate regression models](https://learn.microsoft.com/en-us/training/modules/train-evaluate-regression-models/3-exercise-model)
```Python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Split data 70%-30% into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# Fit a linear regression model on the training set
model = LinearRegression().fit(X_train, y_train)
print (model)

# Evaluate the model using the test data
predictions = model.predict(X_test)
mse = mean_squared_error(y_test, predictions)
print("MSE:", mse)
rmse = np.sqrt(mse)
print("RMSE:", rmse)
r2 = r2_score(y_test, predictions)
print("R2:", r2)

from sklearn.linear_model import Lasso
# Fit a lasso model on the training set
model = Lasso().fit(X_train, y_train)

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor().fit(X_train, y_train)

from sklearn.ensemble import GradientBoostingRegressor
model = GradientBoostingRegressor().fit(X_train, y_train)
```

### Optimize Hyperparameters
```Python
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import make_scorer, r2_score

# Use a Gradient Boosting algorithm
alg = GradientBoostingRegressor()

# Try these hyperparameter values
params = {
 'learning_rate': [0.1, 0.5, 1.0],
 'n_estimators' : [50, 100, 150]
 }

# Find the best hyperparameter combination to optimize the R2 metric
score = make_scorer(r2_score)
gridsearch = GridSearchCV(alg, params, scoring=score, cv=3, return_train_score=True)
gridsearch.fit(X_train, y_train)
print("Best parameter combination:", gridsearch.best_params_, "\n")

# Get the best model
model=gridsearch.best_estimator_
print(model, "\n")
```

### Pipeline
```Python
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LinearRegression
import numpy as np

# Define preprocessing for numeric columns (scale them)
numeric_features = [6,7,8,9]
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())])

# Define preprocessing for categorical features (encode them)
categorical_features = [0,1,2,3,4,5]
categorical_transformer = Pipeline(steps=[
    ('onehot', OneHotEncoder(handle_unknown='ignore'))])

# Combine preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)])

# Create preprocessing and training pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('regressor', GradientBoostingRegressor())])


# fit the pipeline to train a linear regression model on the training set
model = pipeline.fit(X_train, (y_train))
```

### Use the Trained Model
```Python
import joblib
# Save the model as a pickle file
filename = 'model.pkl'
joblib.dump(model, filename)

loaded_model = joblib.load(filename)
# Use the model to predict
result = loaded_model.predict(X_new)
```

## Assessing models
* Model Accuracy = Correct Predictions / Total Predictions
```Python
from sklearn.metrics import accuracy_score

# Calculate the model's accuracy on the TEST set
actual = test.label
predictions = model.predict(test[features])

# Return accuracy as a fraction
acc = accuracy_score(actual, predictions)

# Return accuracy as a number of correct predictions
acc_norm = accuracy_score(actual, predictions, normalize=False)

print(f"The random forest model's accuracy on the test set is {acc:.4f}.")
print(f"It correctly predicted {acc_norm} labels in {len(test.label)} predictions.")
```

## [Train and evaluate classification models](https://learn.microsoft.com/en-us/training/modules/train-evaluate-classification-models/)

```Python
from sklearn.linear_model import LogisticRegression

# Set regularization rate
reg = 0.01

# train a logistic regression model on the training set
model = LogisticRegression(C=1/reg, solver="liblinear").fit(X_train, y_train)

from sklearn.metrics import accuracy_score
print('Accuracy: ', accuracy_score(y_test, predictions))

from sklearn. metrics import classification_report
print(classification_report(y_test, predictions))

from sklearn.metrics import precision_score, recall_score
print("Overall Precision:",precision_score(y_test, predictions))
print("Overall Recall:",recall_score(y_test, predictions))

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, predictions)

# the probability pairs for each case
y_scores = model.predict_proba(X_test)
print(y_scores)

# calculate ROC curve
from sklearn.metrics import roc_curve
fpr, tpr, thresholds = roc_curve(y_test, y_scores[:,1])

from sklearn.metrics import roc_auc_score
auc = roc_auc_score(y_test,y_scores[:,1])
print('AUC: ' + str(auc))

from sklearn.ensemble import RandomForestClassifier
# Create preprocessing and training pipeline
pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                           ('logregressor', RandomForestClassifier(n_estimators=100))])
model = pipeline.fit(X_train, (y_train))
```
* **Support Vector Machine algorithms**: Algorithms that define a hyperplane that separates classes.
* **Tree-based algorithms**: Algorithms that build a decision tree to reach a prediction
* **Ensemble algorithms**: Algorithms that combine the outputs of multiple base algorithms to improve generalizability.

### [Multiclass classification models](https://learn.microsoft.com/en-us/training/modules/train-evaluate-classification-models/7-exercise-multiclass-classification)
* **One vs Rest (OVR)**, in which a classifier is created for each possible class value, with a positive outcome for cases where the prediction is this class, and negative predictions for cases where the prediction is any other class.
* **One vs One (OVO)**, in which a classifier for each possible pair of classes is created. 

## Train and evaluate clustering models
* *Clustering* is a form of unsupervised machine learning in which observations are grouped into clusters based on similarities in their data values, or features.
* *Principal Component Analysis (PCA)* to analyze the relationships between the features and summarize each observation as coordinates for two principal components - in other words, we'll translate the six-dimensional feature values into two-dimensional coordinates.
```Python
from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA

# Normalize the numeric features so they're on the same scale
scaled_features = MinMaxScaler().fit_transform(features[data.columns[0:6]])

# Get two principal components
pca = PCA(n_components=2).fit(scaled_features)
features_2d = pca.transform(scaled_features)
features_2d[0:10]

import matplotlib.pyplot as plt
%matplotlib inline

plt.scatter(features_2d[:,0],features_2d[:,1])
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.title('Data')
plt.show()
```
* [how do you know how many clusters to separate your data into?](https://learn.microsoft.com/en-us/training/modules/train-evaluate-cluster-models/3-exercise-model)  
 One way we can try to find out is to use a data sample to create a series of clustering models with an incrementing number of clusters, and measure how tightly the data points are grouped within each cluster. A metric often used to measure this tightness is the *within cluster sum of squares (WCSS)*, with lower values meaning that the data points are closer. You can then plot the WCSS for each model.
* Clustering: K-Means, Hierachial (divisive, agglomerative)


## Reference
* [Interpreting Linear Regression Through statsmodels .summary()](https://medium.com/swlh/interpreting-linear-regression-through-statsmodels-summary-4796d359035a)
* [StatQuest: Principal Component Analysis (PCA), Step-by-Step](https://youtu.be/FgakZw6K1QQ)
* [A Step-by-Step Explanation of Principal Component Analysis (PCA)](https://builtin.com/data-science/step-step-explanation-principal-component-analysis)
* 
