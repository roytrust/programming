1. Platform: `os.name=='nt'; sys.version; sys.executable`
1. Sublist: list(zip(*a))[0]
1. Append dict: {**d1, **d2}
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
1. Reflection: `dir(dir); a=getattr(dir, '__str__'); callable(a)`
1. temp files: `t=tempfile.TemporaryDirectory(); t.name; t.cleanup()`
1. Size: `len(pickle.dumps(o)); sys.getsizeof(list(range(200)))`
1. Disassembler: `dis.dis(myfunc)`
1. File operation: `pathlib.read_text, write_text; read/write bytes` 
1. Dict: `{**dict1, **dict2}; dict1.update(dict2); dict1 | dict2; dict1 |= dict2; dict1.setdefault()`
1. [defaultdict](https://realpython.com/python-defaultdict/): `from collections import defaultdict`
