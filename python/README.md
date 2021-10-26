## Tips
1. [Environment variable](common.md)
1. [Module path, reload](common.md#modules)
1. [logging](common.md#logging)
1. [exception](common.md#exception)
1. [Date time](common.md#datetime)
2. [iteration](common.md#iteration)
3. Platform: os.name=='nt'
4. Sublist: list(zip(*a))[0]
5. Append dict: {**d1, **d2}
6. [Asterisk `*,**` prefix operator](common.md#asterisk--prefix-operator)
7. Remove Emojis: `t.encode('ascii', 'ignore').decode('ascii')`
8. Parallel loop with zip. itertools.zip_longest()
9. types.SimpleNamespace
10. Partial func call: g=functools.partial(f,1)
11. [regex: regular expression](common.md#regex)
12. Current user: getpass.getuser()
13. Find in a list: `[[i,s] for i,s in enumerate(sys.path) if 'pandas' in s]`
14. Converts a string into an expression: eval()
15. Converts an integer to binary string: bin()
16. Execution time: `timeit.timeit(globals=globals(), number=3, stmt=""); from __main__ import x`
17. Get script directory: os.path.dirname(os.path.realpath(__file__))
18. File modify timestamp: `Path().stat.st_mtime; datetime.datetime.fromtimestamp(tm)`
19. File exists: Path.exists(); File mode: Path.chmod(stat.S_IWUSR) # owner writable
20. First not null: `next((i for i in lst if i), 0)
21. Read dict from a file: `dc=ast.literal_eval(open('dict.txt').read())`
22. argparse: `parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter) # show default; add_argument(help="(default: %(default)s)")
    nargs='*' # list like 1 2. + 1 or more; action='append' # multi times`
1. [Memory mapped file mmap](https://realpython.com/python-mmap/). `mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ); mmap_obj[10:20] # as string; `
1. Reflection: `dir(dir); a=getattr(dir, '__str__'); callable(a)`
1. [from dataclasses import dataclass](https://realpython.com/python-data-classes/). `@dataclass(order=True); make_dataclass('Position', ['name', 'lat', 'lon']); typing.Any; cards: List[PlayingCard] = field(default_factory=make_french_deck)`
1. Run script interactive: python -i
1. [Multiprocessing](http://zetcode.com/python/multiprocessing/)
1. [Encoding decoding](common.md#encoding-decoding)
1. Size: len(pickle.dumps(o))
2. [collection, counter, ChainMap, defaultdict queues](https://realpython.com/python-collections-module/)

## Topics/Packages
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
11. 

## Reference
* [IPython Cookbook](https://ipython-books.github.io/)
* [Style guide](https://www.analyticsvidhya.com/blog/2020/07/python-style-guide/)

