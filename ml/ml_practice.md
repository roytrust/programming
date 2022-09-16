
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
