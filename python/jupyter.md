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


### Nbextensions
* ExecuteTime: Display when each cell has been executed and how long it took.
* Table of contents.
* memory_profiler
