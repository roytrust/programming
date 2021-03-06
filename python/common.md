### Tips
* sys.version, sys.executable
* module location: `m.__file__`
* os.name == 'nt'  # Windows
* `t=tempfile.TemporaryDirectory(); t.name; t.cleanup()`

### Environment variable
```
pprint(dict(os.environ))
os.environ.get('')
os.environ[''] = ''

shutil.which()
```

### Modules
* module path: PYTHONPATH; sys.path.append()
* sys.modules[]
* from importlib import reload; reload()

### logging
* Reset log level: logging.getLogger().setLevel(logging.DEBUG)
* `logging.basicConfig(format='%(asctime)s %(message)s', level=os.environ.get('LOGLEVEL', 'INFO'))`
* [logging tips](https://realpython.com/python-logging/): `logging.error(msg, exc_info=True); logging.exception()`
* [tutorial](https://docs.python.org/3/howto/logging.html#logging-basic-tutorial)

### exception
* sys.exc_info(), logging.exception(e), repr(e)
* traceback.print_exc()
* pdb ! run code. alias in ~/.pdbrc

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
