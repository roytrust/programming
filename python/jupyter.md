## Jupyter
### Tips
* complete: tab, shift tab, ?prefix
* show all output: from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
* magics: %env; %lsmagic; %debug; %prun 1+2; !ls; !!ls; %%sh; %timeit
* from IPython.display import display, HTML
display(HTML(df.to_html()))
* startup file: ~/.ipython/profile_default/ipython_config.py
* %load_ext memory_profiler; %memit

* To install: `pip install jupyter`
* Start: `python -m jupyter notebook --notebook-dir=dir`
* Enable remote connection: `--ip 0.0.0.0`
* [nbconvert](https://nbconvert.readthedocs.io/en/latest/): clean output: `jupyter nbconvert --to notebook --ClearOutputPreprocessor.enabled=True note.ipynb --output note2.ipynb`
* Jupyterlab: `pip install jupyterlab; python -m jupyter lab`

* Config: `jupyter --paths; jupyter labextension list`


### Nbextensions
* ExecuteTime: Display when each cell has been executed and how long it took.
* Table of contents.
* memory_profiler
* Hinterland: autocompleting the code
* Snippets
* Qgrid

