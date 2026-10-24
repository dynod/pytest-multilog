# Usage

To use the multilog feature, a test class just needs to inherit from the **[`TestHelper`](pytest_multilog.helper.TestHelper)** class:

```python
from pytest_multilog import TestHelper

class TestCustom(TestHelper):
    def test_custom(self):
        # Custom test implementation
        ...
```

The **[`TestHelper`](pytest_multilog.helper.TestHelper)** class declares a **[`logs`](pytest_multilog.helper.TestHelper.logs)** fixture which will be automatically used by its children classes.

## Logging behavior and related properties

### Root folder

The **[`TestHelper`](pytest_multilog.helper.TestHelper)** class provides a **[`root_folder`](pytest_multilog.helper.TestHelper.root_folder)** property, matching with the [**pytest** root folder](https://docs.pytest.org/en/stable/reference/customize.html#initialization-determining-rootdir-and-configfile).

```{note}
This property is initialized by the **[`logs`](pytest_multilog.helper.TestHelper.logs)** fixture, so make sure this fixture is called (in particular from other fixtures) before using **[`root_folder`](pytest_multilog.helper.TestHelper.root_folder)** or any derived property.
```

### Output folder

The **[`TestHelper`](pytest_multilog.helper.TestHelper)** class provides a **[`output_folder`](pytest_multilog.helper.TestHelper.output_folder)** property, where all files will be written. It's set to **[`root_folder`](pytest_multilog.helper.TestHelper.root_folder)/out/tests**

### Test name

Each test is associated to a name (provided in **[`test_name`](pytest_multilog.helper.TestHelper.test_name)** property), computed from the file name, the class name and the method name.

E.g. for the snippet above, if stored in a **`test_custom.py`** file, the test name will be: **custom/Custom/custom**.

Test name compute behavior can be configured with following options:

- test file part is computed relatively to the root test module. Test module name is configured through the **[`test_module`](pytest_multilog.helper.TestHelper.test_module)** property (default value is **`"tests"`**). Overriding the property value allow to change the computing behavior:
  - if tests are relative to another test module, just change the name returned by this **[`test_module`](pytest_multilog.helper.TestHelper.test_module)** property
  - if the **[`test_module`](pytest_multilog.helper.TestHelper.test_module)** property is set to None or an empty string, file part will be simply removed from the test name. In the above example, test name would become: **Custom/custom**
  - if the name provided by **[`test_module`](pytest_multilog.helper.TestHelper.test_module)** property is not found in the current test file path, if the test file is located in a submodule, it will be simply ignored in the file part of the test name (i.e. only the test file name will be used, not its relative path)
- By default, **"test\_"** and **"Test"** prefixes are removed from the different parts of the test name, in order to shorten it while keeping it unique (since all pytest detected tests files, class and methods must use these prefixes). In order to disable this replacement (i.e. restore behavior of versions < 1.5.0), just set the **[`filter_test_prefixes`](pytest_multilog.helper.TestHelper.filter_test_prefixes)** property to **`False`**.

### Current worker

In multi-process environment (**pytest** was invoked with **-n X** argument), the current worker name is provided in **[`worker`](pytest_multilog.helper.TestHelper.worker)** property.
It's set to **"master"** in single-process environment.

The class also provides a **[`worker_index`](pytest_multilog.helper.TestHelper.worker_index)** property, giving the working index as an integer value (will be set to 0 for **"master"**).

### Test folder

Test logs will be written to a **pytest.log** file (path provided in **[`test_logs`](pytest_multilog.helper.TestHelper.test_logs)** property), stored in each test folder (provided in **[`test_folder`](pytest_multilog.helper.TestHelper.test_folder)** property):

- While the test is running, it's set to **[`output_folder`](pytest_multilog.helper.TestHelper.output_folder)/\_\_running\_\_/[`worker`](pytest_multilog.helper.TestHelper.worker)/[`test_name`](pytest_multilog.helper.TestHelper.test_name).replace("/","\\")**
- Once the test is terminated, the folder is moved out of the **\_\_running\_\_** folder to the final folder (see **[`test_final_folder`](pytest_multilog.helper.TestHelper.test_final_folder)** property).

It means that during the test execution, it's possible to check which test is running on which worker
(easing troubleshooting situations where a given worker is blocked)

## Checking logs

It is possible to verify if some strings are present in the current test log, by using the **[`check_logs`](pytest_multilog.helper.TestHelper.check_logs)** method.
It takes as input argument:

- either a simple string/Pattern or a list of strings/Patterns:
  - strings will be simply checked to be contained in the whole log
  - Patterns will be searched line by line (more flexible, but slower)
- an optional timeout
- a **`check_order`** parameter to verify patterns order (default if False)

The method will assert if all inputs are found in the log (within the expected timeout, if any).

By default, expected patterns order doesn't matter.
If **`check_order`** parameter is set to True, patterns will be expected in the input order, and check will fail if the order doesn't match.
