# Sphinx Termynal

![Test Status](https://github.com/prajeeshag/sphinx-termynal/actions/workflows/test.yml/badge.svg)
![Doc Build Status](https://github.com/prajeeshag/sphinx-termynal/actions/workflows/build-docs.yml/badge.svg)

![Animation1](./animation1.gif)

A lightweight and modern animated terminal window.
Built for [sphinx](https://www.sphinx-doc.org).

## Installation

```console
pip install sphinx-termynal
```

## Usage

1. **Add the extension to `conf.py`:**

   ```python
   extensions = [
       ...
       'sphynx_termynal',
       ...
   ]
   
2. **Use the extension in your documentation:**
You can now use it in your .rst files. For example:

```rst
.. termynal:: 
   $ pip install sphinx-termynal
   -->
   sphinx-termynal installed
```
This will produce the following terminal animation:

![Animation1](./animation1.gif)
