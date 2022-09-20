
### [Explore and analyze data](https://docs.microsoft.com/en-us/training/modules/explore-analyze-data-with-python/7-exercise-real-world-data)
* the role of a data **scientist** primarily involves exploring and analyzing data. Data exploration is at the core of data science, and is a key element in data analysis and machine learning. Data exploration is at the core of data science, and is a key element in data analysis and machine learning.
* **Machine learning** is a subset of data science that deals with predictive modeling. In other words, machine learning uses data to creates predictive models, in order to predict unknown values. 
* Machine learning works by identifying **relationships** between data values that describe characteristics of something—its features, such as the height and color of a plant—and the value we want to predict—the label, such as the species of plant. These relationships are built into a model through a **training process**.


Data exploration and analysis is typically an iterative process, in which the data scientist takes a sample of data and performs the following kinds of task to analyze it and test hypotheses:
* **Clean data** to handle errors, missing values, and other issues.
* **Apply statistical techniques to better understand the data**, and how the sample might be expected to represent the real-world population of data, allowing for random variation.
* **Visualize data** to determine relationships between variables, and in the case of a machine learning project, identify features that are potentially predictive of the label.
* Revise the hypothesis and repeat the process.

* Check for missing values and badly recorded data
* Consider removal of obvious outliers
* Consider what real-world factors might affect your analysis and consider if your dataset size is large enough to handle this
* Check for biased raw data and consider your options to fix this, if found
* 
* **statistical analysis**. Descriptive statistics and data distribution. 
* **statistics** is fundamentally about taking samples of data and using probability functions to extrapolate information about the full population of data.
* **Measures of central tendency**: mean, median, mode.
* **probability density function**, which estimates the distribution of grades for the full population. "bell curve" of what statisticians call a normal distribution with the mean and mode at the center and symmetric tails.
* **Distribution**: histogram, boxplot. _right skewed_. df.describe()
* Eliminate outliers by **quantile**: df.quantile()
* **Measure of variance**
  * **Range**: the difference between the max and min.
  * **Variance**: The average of the squared difference from the mean, var()
  * **Standard Deviation**: The square root of the variance, std(). Generally the most useful. It provides a measure of variance in the data on the same scale as the data itself. The higher the standard deviation, the more variance there is when comparing values in the distribution to the distribution mean - in other words, the data is more spread out.
  * _normal distribution_, df.plot.density(), scipy.stats.gaussian_kde()

* Comparing data: df.boxplot()
* from sklearn.preprocessing import MinMaxScaler; scaler = MinMaxScaler(); scaler.fit_transform()
* **correlation statistic** is a value between -1 and 1 that indicates the strength of a relationship. Values above 0 indicate a positive correlation (high values of one variable tend to coincide with high values of the other), while values below 0 indicate a negative correlation (high values of one variable tend to coincide with low values of the other). Series.corr()
* **slope-intercept** form of a linear equation looks like this: y=mx+b. The difference between the original y value and the f(x) value is the **error**
* **least squares regression**: The line of best fit is the line that gives us the lowest value for the sum of the squared errors. 
* Using the **regression coefficients** for prediction

### Feature engineering
* One-hot encode categorical features: `dataset = pandas.get_dummies(dataset, columns=[], drop_first=False)`
* 
