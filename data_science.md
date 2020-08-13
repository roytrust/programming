## Quick
* [NumPy cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Numpy_Python_Cheat_Sheet.pdf)
* [pandas cheat sheet](https://github.com/pandas-dev/pandas/blob/master/doc/cheatsheet/Pandas_Cheat_Sheet.pdf)
* [matplotlib cheat sheet](https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Matplotlib_Cheat_Sheet.pdf)

## pandas
* DataFrame: A set of pandas Series that shares the same index.
* `df = pd.DataFrame(np.random.rand(n, 3), columns=list('abc')); index = pd.date_range('1/1/2000', periods=8); df = pd.DataFrame(np.random.randn(8, 3), index=index, columns=['A', 'B', 'C'])` 
* From text: `df = pd.read_csv(io.StringIO(text), header=0, index_col=0, sep='\s+')`
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
* Slice by mask: `df[mask]; isin([]); isin(dict)`
* pivot_tables()
* df[co].last_valid_index; first_valid_index
* Series: s.rename(); s.to_frame()
* Rows with missing: df[df.isnull().any(axis=1)]
* Month end: date.to_period('M').to_timestamp('M')
* Null: np.nan - float, pd.NaT - datetime, notnull()
* Compare: df.equals(df1)
* Float comparison: `np.isclose(df.v1, df.v2, equal_nan=True, rtol=1e-10)`
* Boolean reduction: (df>0).all(), any(), empty, pd.Series([True]).bool() # single element
* Combining overlapping datasets: `df1.combine_first(df2); combine(); return np.where(pd.isna(x), y, x)`. where() returns the same shape.
* Transpose: df.T
* assign a dict to a row: `df.iloc[1] = {'x': 9, 'y': 99}`
* Query: `df.query('(a < b) & (b < c)'); ilevel_0; `
* Computing indicator / dummy variables: `pd.get_dummies(df['key']); pd.get_dummies(pd.cut(values, bins)); pd.get_dummies(df, drop_first=True)`
* Factorizing values: `labels, uniques = pd.factorize(x); np.unique(x, return_inverse=True)[::-1]`
* Exploding a list-like column: `df.assign(var1=df.var1.str.split(',')).explode('var1')`
* Select rows with data closest to certain value using argsort: `df.loc[(df.C - aValue).abs().argsort()]`
* [Efficiently and dynamically creating new columns using applymap](https://pandas.pydata.org/pandas-docs/stable/user_guide/cookbook.html#new-columns): `df[new_cols] = df[source_cols].applymap(categories.get)`
* Setting portions of a MultiIndex with xs: `df2.xs('y',level='variable3',axis=1,drop_level=False).ffill()`
* Prepending a level to a multiindex: `pd.concat({'Foo': df}, names=['Firstlevel'])`
* Flatten Hierarchical columns: `df.columns = ['_'.join(tup).rstrip('_') for tup in df.columns.values]; df.columns = df.columns.get_level_values(0)`
* Fill forward a reversed timeseries: `df.reindex(df.index[::-1]).ffill()`
* [cumsum reset at NaN values](https://stackoverflow.com/questions/18196811/cumsum-reset-at-nan)
* Using replace with backrefs: `df.replace({ 'A' : "http:.+\d\d\/(.*?)(;|\\?).*$"}, { 'A' : r'\1'} ,regex=True)`
* Grouping: `grp=df.groupby([]); grp['a'].min().reset_index(); gb.get_group('cat'); s.expanding().apply(); c.add(1).cumprod(); gb.transform(replace)`
* Select rows by max value in groups: `df.loc[df.groupby(['a'])['b'].idxmax()]; idxmin()`. sort then take first of each: `df.sort_values(by="b").groupby("a", as_index=False).first()`
* Unlike agg, apply’s callable is passed a sub-DataFrame which gives you access to all the columns: `df.groupby('animal').apply(lambda subf: subf['size'][subf['weight'].idxmax()])`
* Sort groups by aggregated data: `ord = gb[['data']].transform(sum).sort_values(by='data'); df.loc[ord.index]`
* Shift groups of the values in a column based on the index: `df.groupby(level=0)['beyer'].shift(1)`
* Calculating the number of specific consecutive equal values: `df['A'].groupby((df['A'] != df['A'].shift()).cumsum()).cumsum()`
* Expanding data
  * [Alignment and to-date - group handler](https://stackoverflow.com/questions/15489011/python-time-series-alignment-and-to-date-functions). 
  * [Rolling Computation window based on values instead of counts](https://stackoverflow.com/questions/14300768/pandas-rolling-computation-with-window-based-on-values-instead-of-counts)
* Splitting by edge: `dfs = list(zip(*df.groupby((1 * (df['Case'] == 'B')).cumsum().rolling(window=3, min_periods=1).median())))[-1]; list(df.groupby((df.a == "B").shift(1).fillna(0).cumsum()))`
* Vectorized Lookup: `prices.lookup(orders.Date, orders.ticker)`
* kdb like asof join: `pd.merge_asof(trades, quotes, on='time')`
* [SQL like non-equal join](https://stackoverflow.com/questions/15581829/how-to-perform-an-inner-or-outer-join-of-dataframes-with-pandas-on-non-simplisti)
* [merge with logic - searchsorted](https://stackoverflow.com/questions/25125626/pandas-merge-with-logic/2512764)

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
* Diff 2 df: `pd.concat([dfa, dfb]).drop_duplicates(keep=False); df.duplicated(['a']); index.duplicated()`
* Float format: `df.round(6)`

### [MultiIndex / advanced indexing](https://pandas.pydata.org/pandas-docs/stable/user_guide/advanced.html#advanced-hierarchical)
* `df.columns.levels; s[::2]; df.swaplevel(0, 1, axis=0); df.reorder_levels([1, 0], axis=0); df.rename_axis(index=['abc', 'def']);  Index.set_names(); dfm.index.is_lexsorted(); dfm.index.lexsort_depth; index.take(positions)`
* It is important to note that tuples and lists are not treated identically in pandas when it comes to indexing. Whereas a tuple is interpreted as one multi-level key, a list is used to specify several keys. Or in other words, tuples go horizontally (traversing levels), lists go vertically (scanning levels).
*  a list of tuples indexes several complete MultiIndex keys, whereas a tuple of lists refer to several values within a level: `s.loc[[("A", "c"), ("B", "d")]];  # list of tuples. s.loc[(["A", "B"], ["c", "d"])]  # tuple of lists`
* Use slicers: `dfmi.loc[(slice('A1', 'A3'), slice(None), ['C1', 'C3']), :]; idx = pd.IndexSlice; dfmi.loc[idx[:, :, ['C1', 'C3']], idx[:, 'foo']]; dfmi.loc['A1', (slice(None), 'foo')]; dfmi.loc[idx[mask, :, ['C1', 'C3']], idx[:, 'foo']]; df2.loc(axis=0)[:, :, ['C1', 'C3']] = -10; df2.loc[idx[:, :, ['C1', 'C3']], :] = df2 * 1000`
* Cross-section: `df.xs('one', level='second', axis=1, drop_level=False); df.xs(('one', 'bar'), level=('second', 'first'), axis=1); df.loc[:, ('bar', 'one')]; `
* **level** in the reindex() and align() to broadcast values across a level: `df.mean(level=0); df2.reindex(df.index, level=0); df.align(df2, level=0); index.levels[1]; index.levels[1]`
* IntervalIndex. `pd.IntervalIndex.from_breaks([0, 1, 2, 3, 4]); pd.Interval(1, 2); idxr = df.index.overlaps(pd.Interval(0.5, 2.5)); c = pd.cut(range(4), bins=2); c.categories; pd.cut([0, 3, 5, 1], bins=c.categories); pd.interval_range(start=0, end=5); pd.interval_range(start=pd.Timestamp('2017-01-01'), periods=4, freq='W')`
* `index.is_monotonic_increasing; index.is_monotonic_decreasing; index.is_unique
* Compared with standard Python sequence slicing in which the slice endpoint is not inclusive, label-based slicing in pandas **is inclusive**. 

### [Time series](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
* `between_time(); indexer_between_time()`
* [Constructing a datetime range that excludes weekends and includes only certain times](https://stackoverflow.com/questions/24010830/pandas-generate-sequential-timestamp-with-jump/24014440#24014440?)
* Divide single values of a dataframe by monthly averages: `grouper = pd.Grouper(key='Date', freq='M'); df.groupby(grouper).transform(lambda x: x/x.mean())`
* Customized agg func: `gpy = df.groupby(pd.Grouper(level='Date', freq='Q')); gpy.agg(lambda x: np.nan if (np.isnan(x).any() or len(x)<3) else x.sum())`
* [Valid frequency arguments to Grouper](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html#timeseries-offset-aliases)
* resample: `df.resample('60Min', how=conversion, base=30); res=df.groupby('string').resample('M', how='sum'); res.groupby(level='date').apply(lambda x: x / x.sum())`

### [Categoricals](https://pandas.pydata.org/pandas-docs/stable/user_guide/categorical.html)

### Topics
* Missing data: https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html
* [Options](https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html). `with pd.option_context('display.max_rows', None): df; pd.options.display.max_rows; pd.set_option('display.max_rows', None), pd.reset_option('all')`



## NumPy
* Random: `np.random.randint(20,size=(3,5); random.choice([]); shuffle(); permutation(); normal(loc=1, scale=2, size=(2, 3))`
* Slice: `np.s_[::2]; np.s_[:, [2]]`
* Map/ufunc/vectorization, use the broadcasting rules of numpy: `np.frompyfunc(len, 1, 1); np.vectorize(len); type(np.add) == np.ufunc # test if a ufunc; np.add.reduce(); set ops`
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
* Evenly distributed between 2 values. `np.linspace(1,20,100)`
* np.fromfunction, Initialize using a function.
* x.itemsize. Data buffer, x.data.tobytes()
* **Reshape**. In place, x.shape=(2,3). Pointing at the same data, x.reshape(2,3). New ndarray, x.ravel()
* QR decomposition, linalg.qr()
* Solving a system of linear scholar equations. `solution=linalg.solve(coeffs,depvars); coeffs.dot(solution),depvars; np.allclose(coeffs.dot(solution),depvars)`
* **Vectorization**, `X,Y=np.meshgrid(x,y), np.sin(X*Y/30.5)`
* np.save, np.load, savetxt, loadtxt, savez
* ufunc: `np.less.outer(range(1,3), range(1,7))`


## matplotlib
* Start: `import matplotlib.pyplot as plt; import matplotlib as mpl; ptl.plot(range(4); plt.show()`
* backend: `mpl.rcParams["backend"];  MPLBACKEND env-var; mpl.use()`
* Interactive mode: `mpl.is_interactive(); mpl.interactive(); plt.ion() # turn on; plt.ioff(); plt.draw()`
* plt.gca() returns the current axes, and gcf() returns the current figure.
* plt.subplot(211) specifies numrows, numcols, plot_number.

* [Parts of a figure](https://matplotlib.org/tutorials/introductory/usage.html#figure-parts)
* [pyplot tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html#sphx-glr-tutorials-introductory-pyplot-py)
* Cheatsheet: https://github.com/matplotlib/cheatsheets

## Reference
* [NumPy notebook](https://github.com/ageron/handson-ml2/blob/master/tools_numpy.ipynb)
* [Pandas notebook](https://github.com/ageron/handson-ml2/blob/master/tools_pandas.ipynb)
* [Matplotlib notebook](https://github.com/ageron/handson-ml2/blob/master/tools_matplotlib.ipynb)
* [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/) 
