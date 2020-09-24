## Tips
1. [Environment variable](common.md)
1. [Module path, reload](common.md#modules)
1. [logging](common.md#logging)
1. [exception](common.md#exception)
1. [Date time](common.md#datetime)
1. Platform: os.name=='nt'
1. Sublist: list(zip(*a))[0]
1. Append dict: {**d1, **d2}
1. [Asterisk `*,**` prefix operator](common.md)
1. Remove Emojis: `t.encode('ascii', 'ignore').decode('ascii')`
1. Parallel loop with zip. itertools.zip_longest()
1. types.SimpleNamespace
1. Partial func call: g=functools.partial(f,1)
1. [regex: regular expression](common.md#regex)
1. Current user: getpass.getuser()
1. Find in a list: `[[i,s] for i,s in enumerate(sys.path) if 'pandas' in s]`
1. Converts a string into an expression: eval()
1. Converts an integer to binary string: bin()
1. Execution time: `timeit.timeit(globals=globals(), number=3, stmt=""); from __main__ import x`
1. Get script directory: os.path.dirname(os.path.realpath(__file__))
1. File modify timestamp: `Path().stat.st_mtime; datetime.datetime.fromtimestamp(tm)`
1. File exists: Path.exists(); File mode: Path.chmod(stat.S_IWUSR) # owner writable
1. First not null: `next((i for i in lst if i), 0)
1. Read dict from a file: `dc=ast.literal_eval(open('dict.txt').read())`
1. argparse: `parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter) # show default; add_argument(help="(default: %(default)s)")
    nargs='*' # list like 1 2. + 1 or more; action='append' # multi times`
1. [Memory mapped file mmap](https://realpython.com/python-mmap/). `mmap.mmap(file_obj.fileno(), length=0, access=mmap.ACCESS_READ); mmap_obj[10:20] # as string; `
1. Reflection: `dir(dir); a=getattr(dir, '__str__'); callable(a)`
1. [from dataclasses import dataclass](https://realpython.com/python-data-classes/). `@dataclass(order=True); make_dataclass('Position', ['name', 'lat', 'lon']); typing.Any; cards: List[PlayingCard] = field(default_factory=make_french_deck)`

## Topics/Packages
1. [Web](web.md)
   * [Proxy setup](web.md#proxy-setup)
   * [selenium](web.md#selenium)
   * [requests](web.md#requests)
1. [Jupyter](jupyter.md)
1. [decorator](decorator.md)
1. [Object oriented programming](oop.md)
1. [Testing](test.md)
1. Debug
1. Code quality & style check: `# pylint: disable=`
1. [Functional programming](functional.md)
1. [parse - Matching Strings](https://realpython.com/python-packages/#parse-for-matching-strings). `parse.search("Author: {name} <{email}>", pep498)`

## Overview
* Everything are objects.
* callable: __call__



## Reference
* [IPython Cookbook](https://ipython-books.github.io/)
* [Style guide](https://www.analyticsvidhya.com/blog/2020/07/python-style-guide/)

