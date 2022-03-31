# module-cli

Bootstrap extensible single-module CLIs

## Installation

### With `pipx`

This package is intended to generate python modules that function as CLIs and therefore shouldn't be a dependency of any module/package that it generates. **Because of this it's recommended to use this package via `pipx`**:

```bash
pipx run module-cli /path/to/module.py
```

### With `pip`

If you really want this package as one of _your_ package's dependencies, then install via `pip` in the usual way:

```bash
pip install module-cli
```

Which you can then use the CLI:

```bash
$ module-cli -h
usage: module-cli [-h] [-v] [out]

positional arguments:
  out            File to write to. (default: -)

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show program's version number and exit
```

## Installing your CLI

The modules generated by `module-cli` contain a function `cli()`. This function is the one you'll likely want to point to if you intend to turn your module into an installable command-line application.

- **`setup.cfg`**:

  ```ini
  [options.entry_points]
  console_scripts =
      my_cli = my_pkg.my_module:cli
  ```

- **`setup.py`**:

  ```python
  setup(
      entry_points = {
          'console_scripts': ['my_cli=my_pkg.my_module:cli'],
      }
  )
  ```

- **`pyproject.toml`** (poetry):

  ```toml
  [tool.poetry.scripts]
  my_cli = "my_pkg.my_module:cli"
  ```

## Contributing

1. Have or install a recent version of `poetry` (version >= 1.1)
1. Fork the repo
1. Setup a virtual environment (however you prefer)
1. Run `poetry install`
1. Run `pre-commit install`
1. Add your changes (adding/updating tests is always nice too)
1. Commit your changes + push to your fork
1. Open a PR
