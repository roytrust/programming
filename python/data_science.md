## NumPy ``
* [NumPy cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
* `x=np.random.randint(20,size=12)`
* N largest value. `ind=np.argpartition(x,-4)[-4:]; np.sort(x[ind])`
* matching within a tolerance. `np.allclose(x1,x2,0.1)`
* Keep values within an interval.`np.clip(x,lower,upper_limit)`
* Extract based on condition. `np.extract((x<3)|(x>10),x)`
* Return values based on condition. `np.where(x>5); np.where(x>5,"hit","miss")`
* nth percentile. `np.percentile(x,30,axis=0)`


## pandas
* [pandas cheat sheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)
* df[c].unique()
* df.iloc[:, :-1].values; iloc[:, -1]; [[]] get df back
* df.info(), df.describe()
* df.index
* df['date'].dt.date
* df['c'].astype('int')
* Custom conversion: df['c'].apply(f)
* np.where
* np.to_datetime(); np.to_numeric()
* functools.reduce()
* filter(), map()
* read_csv(nrows=n)
* isin([])
* subset of columns based on type, select_dtypes()
* pivot_tables()


### Options
* pd.options.display.max_rows; pd.set_option('display.max_rows')

## matplotlib
* [matplotlib cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf)


