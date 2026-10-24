# pytest-multilog

A pytest plugin to persist logs from parallel test processes (and other helpers)

<!-- NMK-BADGES-BEGIN -->
[![License: MIT License](https://img.shields.io/github/license/dynod/pytest-multilog)](https://github.com/dynod/pytest-multilog/blob/main/LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/dynod/pytest-multilog/build.yml?branch=main&label=build%20%26%20u.t.)](https://github.com/dynod/pytest-multilog/actions?query=branch%3Amain)
[![Issues](https://img.shields.io/github/issues-search/dynod/pytest-multilog?label=issues&query=is%3Aopen+is%3Aissue)](https://github.com/dynod/pytest-multilog/issues?q=is%3Aopen+is%3Aissue)
[![Supported python versions](https://img.shields.io/badge/python-3.10%20--%203.14-blue)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/pytest-multilog)](https://pypi.org/project/pytest-multilog/)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg)](https://astral.sh/ruff)
[![Code coverage](https://img.shields.io/codecov/c/github/dynod/pytest-multilog)](https://app.codecov.io/gh/dynod/pytest-multilog)
[![Documentation Status](https://readthedocs.org/projects/pytest-multilog/badge/?version=stable)](https://pytest-multilog.readthedocs.io/)
<!-- NMK-BADGES-END -->

## Usage

To use the multilog feature, a test class just needs to inherit from the **`TestHelper`** class:

```python
from pytest_multilog import TestHelper

class TestCustom(TestHelper):
    def test_custom(self):
        # Custom test implementation
        ...
```

## Documentation

For more information about how to use the test logs related features and properties, please see the full documentation [here](https://pytest-multilog.readthedocs.io/).

## Issues

Issues for this project shall be reported on the [**`pytest-multilog`** GitHub project](https://github.com/dynod/pytest-multilog/issues).
