### Tips
* sys.version
* module location: `m.__file__`


### Environment variable
```
pprint(dict(os.environ))
os.environ.get('')
os.environ[''] = ''

shutil.which()
```

### module path
* PYTHONPATH
* sys.path.append()

### Datetime
```python
# current date time
from datetime import datetime
datetime.now(); datetime.now().time(); datetime.now().date()
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

