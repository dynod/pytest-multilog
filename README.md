# pytest-multilog
A pytest plugin to persist logs from parallel test processes (and other helpers)

<!-- NMK-BADGES-BEGIN -->
[![License: MPL](https://img.shields.io/github/license/dynod/pytest-multilog)](https://github.com/dynod/pytest-multilog/blob/main/LICENSE)
[![Checks](https://img.shields.io/github/actions/workflow/status/dynod/pytest-multilog/build.yml?branch=main&label=build%20%26%20u.t.)](https://github.com/dynod/pytest-multilog/actions?query=branch%3Amain)
[![Issues](https://img.shields.io/github/issues-search/dynod/pytest-multilog?label=issues&query=is%3Aopen+is%3Aissue)](https://github.com/dynod/pytest-multilog/issues?q=is%3Aopen+is%3Aissue)
[![Supported python versions](https://img.shields.io/badge/python-3.8%20--%203.11-blue)](https://www.python.org/)
[![PyPI](https://img.shields.io/pypi/v/pytest-multilog)](https://pypi.org/project/pytest-multilog/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Flake8 analysis result](https://img.shields.io/badge/flake8-0-green)](https://flake8.pycqa.org/)
[![Code coverage](https://img.shields.io/codecov/c/github/dynod/pytest-multilog)](https://app.codecov.io/gh/dynod/pytest-multilog)
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

The **`TestHelper`** class declares a **`logs`** fixture which will be automatically used by its children classes.

## Behavior and attributes

### Root folder
The **`TestHelper`** class provides a **`root_folder`** property, matching with the **pytest** root folder.

### Output folder
The **`TestHelper`** class provides a **`output_folder`** property, where all files will be written. It's set to **`output_folder / "out" / "tests"`**

### Test name
Each test is associated to a name (provided in **`TestHelper.test_name`**), computed from the file name, the class name and the method name.

E.g. for the snippet above, if stored in a **`test_custom.py`** file, the test name will be: **test_custom_TestCustom_test_custom**.

### Current worker
In multi-process environment (**pytest** was invoked with **-n X** argument), the current worker name is provided in **`TestHelper.worker`** attribute.
It's set to **"master"** in single-process environment.

The class also provides a **`TestHelper.worker_index`** attribute, giving the working index as an integer value (will be set to 0 for **"master"**).

### Test folder
Test logs will be written in a **pytest.log** file (path provided in **`TestHelper.test_logs`**), stored in each test folder (provided in **`TestHelper.test_folder`** attribute):
* While the test is running, it's set to **`TestHelper.output_root / "__running__" / TestHelper.worker / TestHelper.test_name`**
* Once the test is terminated, the folder is moved directly under the output root one.

It means that during the test execution, it's possible to check which test is running on which worker 
(easing troubleshooting situations where a given worker is blocked)

### Checking logs
It is possible to verify if some strings are present in the current test log, by using the **`TestHelper.check_logs`** method.
It takes as input argument:
* either a simple string/Pattern or a list of strings/Patterns:
  * strings will be simply checked to be contained in the whole log
  * Patterns will be searched line by line (more flexible, but slower)
* an optional timeout
* a **`check_order`** parameter to verify patterns order (default if False)

The method will assert if all inputs are found in the log (within the expected timeout, if any).

By default, expected patterns order doesn't matter.
If **`check_order`** parameter is set to True, patterns will be expected in the input order, and check will fail if the order doesn't match.
