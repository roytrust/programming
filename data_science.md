## Quick
* [NumPy cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
* [pandas cheat sheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)
* [matplotlib cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf)

## pandas
* DataFrame: A set of pandas Series that shares the same index.
* `index = pd.date_range('1/1/2000', periods=8); df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])` 
* Underlying data: `.array; df.to_numpy()` preferrable over value
* Histogramming: `value_count(), mode()`
* Discretization and quantiling, bins: `cut(); qcut()`
* Reindexing and altering labels: To reindex means to conform the data to match a given set of labels along a particular axis. Fill/limit  
`reindex(index=index_labels, columns=column_labels); reindex_like(); align(); drop(columns=[]); rename(); rename_axis() # MultiIndex`
* Index (lable or positional): `df.index; df.set_index(col_name); df.reset_index(drop=True) - regenerate index; df.index.name=''; df.sort_values(by = list_of_cols,ascending=True)`
* Sorting: by index: `sort_index()`. Sort by columns: `df.sort_values(by = list_of_cols,ascending=True)`. argsort()
* Iteration: `for row in itertuples(); for index, row in iterrows(); for label, ser in df.items()`. Indices where to be inserted: searchsorted(). `nsmallest(); nlargest(); `
* [dtypes](https://pandas.pydata.org/pandas-docs/stable/getting_started/basics.html#dtypes). `df['a'].astype('int'); select_dtypes()`
* [Scaling to large dataset](https://pandas.pydata.org/pandas-docs/stable/user_guide/scale.html). load less data, use efficient datatypes (category), use chunking, other libs (Dask). `df.memory_usage(deep=True) # in bytes`
* Accesors. .sparse, .str, .cat for categorical data, and .dt for datetime-like data. 
* Change a column: df[:, 'c'] = x
* DataFrame operations: dict-like: `del df['a']; df.pop()`. Assign in method chains, func: `assign()`. `stack(); unstack()`
* df[c].unique()
* df.iloc[:, :-1].values; iloc[:, -1]; df[['c']] get df back
* df.info(memory_usage='deep'), df.describe()
* Custom conversion: `f(x,**kwargs); df['c'].apply(f, a=1)`
* Datetime: `d=np.to_datetime('2020-05-01'); d.weekofyear; d.strftime(format); pd.Timedelta(days=1); df['date'].dt.date; ` np.to_numeric()
* functools.reduce()
* filter(), map()
* read_csv(nrows=n)
* Slice by mask: df[mask]; isin([])
* pivot_tables()
* df[co].last_valid_index; first_valid_index
* Series: s.rename(); s.to_frame()
* Rows with missing: df[df.isnull().any(axis=1)]
* Month end: date.to_period('M').to_timestamp('M')
* Null: np.nan - float, pd.NaT - datetime, notnull()
* Compare: df.equals(df1)
* Float comparison: `np.isclose(df.v1, df.v2, equal_nan=True, rtol=1e-10)`
* Group: `grp=df.groupby([]); grp['a'].min().reset_index()`
* Select rows by max value in groups: `df.loc[df.groupby(['a'])['b'].idxmax()]; idxmin()`. sort then take first of each: df.sort_values(by="b").groupby("a", as_index=False).first()
* Boolean reduction: (df>0).all(), any(), empty, pd.Series([True]).bool() # single element
* Combining overlapping datasets: `df1.combine_first(df2); combine(); return np.where(pd.isna(x), y, x)`
* Transpose: df.T

### Function application
1. Tablewise Function Application: pipe()
1. Row or Column-wise Function Application: apply(). result_type: reduce, broadcast, expand
1. Aggregation API: agg() and transform()
1. Applying Elementwise Functions: applymap()
* Addtional args: `df.apply(subtract_and_divide, args=(5,), divide=3)`
* Series map: `s.map(t)`

### Series
* Series is ndarray-like. Series like dict: `s['a']`. `s.name; s.rename()`
* A key difference between Series and ndarray is that operations between Series automatically align the data based on label. ... The result of an operation between unaligned Series will have the **union** of the indexes involved. If a label is not found in one Series or the other, the result will be marked as missing NaN. 
* `s=pd.Series(dtype=int); s.add()`
* Compare array-like objects: `pd.Series(['foo', 'bar', 'baz']) == 'foo'; pd.Series(['foo', 'bar', 'baz']) == pd.Index(['foo', 'bar', 'qux']); pd.Series(['foo', 'bar', 'baz']) == np.array(['foo', 'bar', 'qux'])`
* Diff 2 df: `pd.concat([dfa, dfb]).drop_duplicates(keep=False)`
* Float format: `df.round(6)`

### [MultiIndex / advanced indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced-hierarchical)
* `df.columns.levels; s[::2]; df.swaplevel(0, 1, axis=0); df.reorder_levels([1, 0], axis=0); df.rename_axis(index=['abc', 'def']);  Index.set_names(); dfm.index.is_lexsorted(); dfm.index.lexsort_depth; index.take(positions)`
* It is important to note that tuples and lists are not treated identically in pandas when it comes to indexing. Whereas a tuple is interpreted as one multi-level key, a list is used to specify several keys. Or in other words, tuples go horizontally (traversing levels), lists go vertically (scanning levels).
*  a list of tuples indexes several complete MultiIndex keys, whereas a tuple of lists refer to several values within a level: `s.loc[[("A", "c"), ("B", "d")]];  # list of tuples. s.loc[(["A", "B"], ["c", "d"])]  # tuple of lists`
* Use slicers: `dfmi.loc[(slice('A1', 'A3'), slice(None), ['C1', 'C3']), :]; idx = pd.IndexSlice; dfmi.loc[idx[:, :, ['C1', 'C3']], idx[:, 'foo']]; dfmi.loc['A1', (slice(None), 'foo')]; dfmi.loc[idx[mask, :, ['C1', 'C3']], idx[:, 'foo']]; df2.loc(axis=0)[:, :, ['C1', 'C3']] = -10; df2.loc[idx[:, :, ['C1', 'C3']], :] = df2 * 1000`
* Cross-section: `df.xs('one', level='second', axis=1, drop_level=False); df.xs(('one', 'bar'), level=('second', 'first'), axis=1); df.loc[:, ('bar', 'one')]; `
* **level** in the reindex() and align() to broadcast values across a level: `df.mean(level=0); df2.reindex(df.index, level=0); df.align(df2, level=0)`
* IntervalIndex. `pd.IntervalIndex.from_breaks([0, 1, 2, 3, 4]); pd.Interval(1, 2); idxr = df.index.overlaps(pd.Interval(0.5, 2.5)); c = pd.cut(range(4), bins=2); c.categories; pd.cut([0, 3, 5, 1], bins=c.categories); pd.interval_range(start=0, end=5); pd.interval_range(start=pd.Timestamp('2017-01-01'), periods=4, freq='W')`
* `index.is_monotonic_increasing; index.is_monotonic_decreasing; index.is_unique
* Compared with standard Python sequence slicing in which the slice endpoint is not inclusive, label-based slicing in pandas **is inclusive**. 

### [Time series](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)

### [Categoricals](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html)

### Topics
* Missing data: https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
* [Options](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html). `with pd.option_context('display.max_rows', None): df; pd.options.display.max_rows; pd.set_option('display.max_rows', None), pd.reset_option('all')`



## NumPy ``
* `x=np.random.randint(20,size=12)`
* Conditional operators, `x<10, x[x>10]`
* Indexing, `x[2::2]; x[::-1]; x[(0,2),(2:5)]; x[:,(-1,2,-1)]; x[(-1,1),(2,3)]; x[1,...]; np.ix_`
* vstack, hstack, stack
* split, vsplit, hsplit
* transpose, swapaxes
* N largest value. `ind=np.argpartition(x,-4)[-4:]; np.sort(x[ind])`
* matching within a tolerance. `np.allclose(x1,x2,0.1)`
* Keep values within an interval.`np.clip(x,lower,upper_limit)`
* Extract based on condition. `np.extract((x<3)|(x>10),x)`
* Return values based on condition. `np.where(x>5); np.where(x>5,"hit","miss")`
* nth percentile. `np.percentile(x,30,axis=0)`
* np.linspace, Evenly distributed between 2 values.
* np.fromfunction, Initialize using a function.
* x.itemsize. Data buffer, x.data.tobytes()
* **Reshape**. In place, x.shape=(2,3). Pointing at the same data, x.reshape(2,3). New ndarray, x.ravel()
* QR decomposition, linalg.qr()
* Solving a system of linear scholar equations. `solution=linalg.solve(coeffs,depvars); coeffs.dot(solution),depvars; np.allclose(coeffs.dot(solution),depvars)`
* **Vectorization**, `X,Y=np.meshgrid(x,y), np.sin(X*Y/30.5)`
* np.save, np.load, savetxt, loadtxt, savez


## matplotlib
* Cheatsheet: https://github.com/matplotlib/cheatsheets

## Reference
* [NumPy notebook](https://github.com/ageron/handson-ml2/blob/master/tools_numpy.ipynb)
* [Pandas notebook](https://github.com/ageron/handson-ml2/blob/master/tools_pandas.ipynb)
* [Matplotlib notebook](https://github.com/ageron/handson-ml2/blob/master/tools_matplotlib.ipynb)
* [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) 
