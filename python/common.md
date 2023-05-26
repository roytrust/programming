
### <a id="modules">[venv, modules, import](https://realpython.com/python-import)
* module path: PYTHONPATH; sys.path.append()
* `sys.modules[], sys.meta_path`
* module location: `m.__file__`
* from importlib import reload; reload()
* **Packages**: __path__, __init__.py
* List contents of a namespace: `dir(); dir(ns)`
* [Virtual environments: venv](https://realpython.com/python-virtual-environments-a-primer)
* List outdated: `pip list --outdated`. `pip show --verbose -f pandas`
* `pip cache info`, `pip config list`
* 3rd party dependences: `{m for m in sys.modules if "." not in m} - sys.stdlib_module_names`

### logging
* Reset log level: logging.getLogger().setLevel(logging.DEBUG)
* `logging.basicConfig(format='%(asctime)s %(message)s', level=os.environ.get('LOGLEVEL', 'INFO'))`
* [logging tips](https://realpython.com/python-logging/): `logging.error(msg, exc_info=True); logging.exception()`
* [tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)

### <a id=env> Args, shell, env
* argparse: `parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter) # show default; add_argument(help="(default: %(default)s)")
    nargs='*' # list like 1 2. + 1 or more; action='append' # multi times`
* args: `sys.argv; sys.orig_argv`
* Environment variable: `os.environ; shutil.which()`
* Run script interactive: python -i
* Check version: `sys.version_info >= (3, 11)`
    
### exception
* sys.exc_info(), logging.exception(e), repr(e)
* traceback.print_exc()
* pdb ! run code. alias in ~/.pdbrc
* Notes: `err = ValueError(123); err.add_note("Enriching Exceptions with Notes"); err.__notes__; raise err`
* Exception group: `try: raise ExceptionGroup("test2", [TypeError("int"), ValueError(654)])  except* ValueError as err: print(f"handling ValueError: {err.exceptions}")`

### Datetime
* [datetime formatting](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
```python
# current date time
from datetime import datetime
datetime.now(); datetime.now().time(); datetime.now().date()
now.strftime('%Y%m%d')
datetime.strptime('20200801', '%Y%m%d').weekday()
from datetime import date; date.today()
datetime.timedelta(days=1)
```
* Timezone: `from zoneinfo import ZoneInfo; tz=ZoneInfo("America/Vancouver"); ts = datetime.now(tz=ZoneInfo("America/Vancouver")); ts.astimezone(ZoneInfo("Europe/Oslo")); zoneinfo.available_timezones(); hour = timedelta(hours=1); (ts + 1 * hour).astimezone(tz); tz.utcoffset(datetime(1995, 1, 1)) / hour; tz.tzname(datetime(2021, 1, 28))`

### [Asterisk `*,**` prefix operator](https://treyhunner.com/2018/10/asterisks-in-python-what-they-are-and-how-to-use-them/)
* unpack into function call. 
```python
print(*sys.verson_info)
list(row) for row in zip(*lists)

```
* pack arguments to func
```python
def tag(tag_name, **attributes):
    attribute_list = [
        f'{name}="{value}"'
        for name, value in attributes.items()
    ]
    return f"<{tag_name} {' '.join(attribute_list)}>"
```
* Positional arguments with keyword only arguments. `func(*p, k)`
* Keyword only arguments without positional arguments. `func(iterable,*,k)`
* tuple unpacking. `f,*r,l=alist`
* list literal. `{*iterable1,*iterable2}`
* dictionary literals. Copy/merge `{**d1, k:v}`
* Populate kwarg values with a dict: `f(**v)`
* Using ** when calling a func: `def f(a, b, c); v={'c': 3, 'b': 2}; f(1, **v)`

### regex
* `import re; re.sub(r'reg', '', s)`
* Find a Specific Word: `/[^.]* word [^.]*\./gi`
* Stripe invalid characters: `/[<>|:"*?\\/]+/g`
* Replace multiple whitespace: `/\s\s+/g`. trim the beginning
* Limit to alphanumeric chars: `/^[A-Z0-9]+$/i`
* Turn URLs into links: `str.replace(/\b(https?|ftp|file):\/\/\S+/g, '<a href="$&">$&</a>');`
* Delete duplicate words: `str.replace(/\b(\w+)\s+\1\b/gi, '$1');`

### [Encoding decoding](https://realpython.com/python-encodings-guide/)
* String in unicode: `s.encode("unicode-escape").decode()`
* For requests: json.dumps(json, ensure_ascii=True)
* charset detect: `import chardet; chardet.detect(b)`
* [language detect](https://www.geeksforgeeks.org/detect-an-unknown-language-using-python/): `langdetect.detect(s)`

### [Iteration](https://www.analyticsvidhya.com/blog/2021/07/everything-you-should-know-about-iterables-and-iterators-in-python-as-a-data-scientist/)
* Iterables are objects that can be iterated in iterations. has __iter__()
* An Iterator is an object representing a stream of data that produces a data value at a time using the __next__() method. An Iterator is an object representing a stream of data that produces a data value at a time using the __next__() method. StopIteration.
* Iterables supports only iter() function. But iterators supports both iter() and next() function.
* the iterator can be used just once.
* 
