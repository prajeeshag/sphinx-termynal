
# Sphinx Termynal
Create animated terminal window in your [Sphinx](https://www.sphinx-doc.org) documentation.

## Installation
``` {code-block} console
   $ pip install sphinx-termynal
```

## Usage
1. **Add the extension to `conf.py`:**

```{code-block} python
   extensions = [
       ...
       'sphynx_termynal',
       ...
   ]
```

2. **Use the extension in your documentation:**

You can now use it in your documentation files. For example:

::::{tab-set}

:::{tab-item} reST
```{code-block} rst
   .. termynal:: 
      $ pip install sphinx-termynal
      -->
      sphinx-termynal installed
```
:::

:::{tab-item} MyST
````{code-block} md
   ```{termynal}
      $ pip install sphinx-termynal
      -->
      sphinx-termynal installed
   ```
````
:::
::::

This will produce the following terminal animation:

```{termynal}
   $ pip install sphinx-termynal
   -->
   sphinx-termynal installed
```

- A line starting with `$` will be rendered as input command.
- A line starting with `-->` is rendered as a progress bar.
- Everything else is rendered as it is.
