
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
