
# Sphinx Termynal

![PyPI - Version](https://img.shields.io/pypi/v/sphinx-termynal)
![Test Status](https://github.com/prajeeshag/sphinx-termynal/actions/workflows/test.yml/badge.svg)
[![codecov](https://codecov.io/gh/prajeeshag/sphinx-termynal/graph/badge.svg?token=UNNUW30IQL)](https://codecov.io/gh/prajeeshag/sphinx-termynal)
![Doc Build Status](https://github.com/prajeeshag/sphinx-termynal/actions/workflows/build-docs.yml/badge.svg)

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
       "sphynx_terminal",
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

## Example: Multi-line command

::::{tab-set}

:::{tab-item} reST
```{code-block} rst
   .. termynal:: 
      $ pip install sphinx-termynal \
      sphinx \
      numpy
      -->
      done
```
:::

:::{tab-item} MyST
````{code-block} md
   ```{termynal}
      $ pip install sphinx-termynal \
      sphinx \
      numpy
      -->
      done
   ```
````
:::
::::

```{termynal}
   $ pip install sphinx-termynal \
   sphinx \
   numpy
   -->
   done
```

## Example: Special characters

::::{tab-set}

:::{tab-item} reST
```{code-block} rst
   .. termynal:: 
      $ < > & " '
```
:::

:::{tab-item} MyST
````{code-block} md
   ```{termynal}
      $ < > & " '
   ```
````
:::
::::

```{termynal}
   $ < > & " '
```

## Credits

Thanks [ines](https://github.com/ines/termynal), [termynal.py](https://github.com/termynal/termynal.py)
