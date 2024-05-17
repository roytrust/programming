## [Tips](tips.md)
1. [Jupyter online](https://jupyter.org/try)
2. [venv, module, reload, import](common.md#modules)
3. [args, shell, environment](common.md#env)
4. [logging](common.md#logging)
5. [exception](common.md#exception)
6. [Date time](common.md#datetime)
7. [iteration](common.md#iteration)
11. [Asterisk `*,**` prefix operator](common.md#asterisk--prefix-operator)
16. [regex: regular expression](common.md#regex)
1. [Memory mapped file mmap](https://realpython.com/python-mmap/). `mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ); mmap_obj[10:20] # as string; `
1. [from dataclasses import dataclass](https://realpython.com/python-data-classes/). `@dataclass(order=True); make_dataclass('Position', ['name', 'lat', 'lon']); typing.Any; cards: List[PlayingCard] = field(default_factory=make_french_deck)`
1. Run script interactive: python -i
1. [Multiprocessing](http://zetcode.com/python/multiprocessing/)
1. [Encoding decoding](common.md#encoding-decoding)
1. Size: len(pickle.dumps(o))
2. [collection, counter, ChainMap, defaultdict queues](https://realpython.com/python-collections-module/)
3. Multiple constructor: @classmethod, @singledispatchmethod
4. [namedtuple](https://realpython.com/python-namedtuple/): `from collections import namedtuple; Point = namedtuple("Point", "x, y")`
5. [Structural Pattern Matching](https://realpython.com/python310-new-features/#structural-pattern-matching): `match user: case {"dob": {"age": int(age)}}:; `. 
   sequence pattern, wildcard pattern, class pattern, OR pattern, value pattern. literal. `match (mod_3, mod_5): case (_, 0): case _:`
6. [mock](test_debug.md#mock)

### [Decorators](https://realpython.com/primer-on-python-decorators/)
* [@lru_cache, @total_ordering, @contextmanager, @property, @cached_property, @classmethod, @staticmethod, @dataclass, @atexit.register](https://medium.com/techtofreedom/9-python-built-in-decorators-that-optimize-your-code-significantly-bc3f661e9017). 
* [@logger, @wraps, @repeat, @timeit, @retry, @countcall, @rate_limited,  @singledispatch](https://towardsdatascience.com/12-python-decorators-to-take-your-code-to-the-next-level-a910a1ab3e99)
* 

## Topics/Packages
1. [Python Packaging](https://itnext.io/python-packaging-12ef040c4ea0)
1. [Web](web.md)
   * [Proxy setup](web.md#proxy-setup)
   * [selenium](web.md#selenium)
   * [requests](web.md#requests)
1. [Jupyter](jupyter.md)
1. [decorator](decorator.md)
1. [Object oriented programming](oop.md)
1. [Testing](test_debug.md)
1. [Debug](test_debug.md#debug)
1. Code quality & style check: `# pylint: disable=`
   * [.pylintrc](https://github.com/kubeflow/examples/blob/master/.pylintrc)
3. [Documenting Python](https://devguide.python.org/documenting/). [Sphinx reStructuredText Primer](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html)
4. [Functional programming](functional.md)
5. Profile: `profile, pyinstrument`
6. PDF: https://realpython.com/creating-modifying-pdf/  https://realpython.com/pdf-python/
7. [parse - Matching Strings](https://realpython.com/python-packages/#parse-for-matching-strings). `parse.search("Author: {name} <{email}>", pep498)`
8. deepdiff
9. String similarity match: RapidFuzz
10. WSGI Werkzeug
11. [backoff](https://pypi.org/project/backoff/): retry until some condition is met.
1. [cachetools](https://pypi.org/project/cachetools/)
1. [ipyaggrid - Display pandas dataframes as dynamic HTML5 grids](https://dgothrek.gitlab.io/ipyaggrid/)
1. [Working with Excel](https://automatetheboringstuff.com/2e/chapter13/)
  * [Openpyxl](https://realpython.com/openpyxl-excel-spreadsheets-python/)
  * [Plot charts](https://www.geeksforgeeks.org/python-plotting-charts-in-excel-sheet-using-openpyxl-module-set-1/?ref=lbp)
  * [Pandas ExcelWriter](https://pandas.pydata.org/docs/reference/api/pandas.ExcelWriter.html#pandas.ExcelWriter)

### Protocols
* [Iterators and Iterables](https://realpython.com/python-iterators-iterables/)
* [Descriptors](https://realpython.com/python-descriptors), lookup chain: `att1=property(getter, setter); `
  * descriptors are instantiated just once per class. Lazy Properties. share behavior among all the properties.
* [Context Managers](https://realpython.com/python-with-statement)

## Reference
* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
* [IPython Cookbook](https://ipython-books.github.io/)
* [Style guide](https://www.analyticsvidhya.com/blog/2020/07/python-style-guide/)

