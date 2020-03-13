### Tips
* sys.version
* module location: `m.__file__`


### Environment variable
```
pprint(dict(os.environ))
os.environ.get('')
os.environ[''] = ''
```

### module path
* PYTHONPATH
* sys.path.append()

### Asterisk `*,**` prefix operator
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

