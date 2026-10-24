# Changelog

Here are listed all the meaningfull changes done on **`pytest-multilog`**

```{note}
Only interface and important behavior changes are listed here.

The fully detailed changelog is also available on [Github](https://github.com/dynod/pytest-multilog/releases)
```

## Release 1.7

- Provide a real documentation

## Release 1.6

- Fix type hinting in API
- Replace logs configuration override by a simple file handler

## Release 1.5

- Advanced and configurable handling for **[`test_name`](pytest_multilog.helper.TestHelper.test_name)** and **[`test_final_folder`](pytest_multilog.helper.TestHelper.test_final_folder)**

## Release 1.4

- Added optional **check_order** argument to **[`check_logs`](pytest_multilog.helper.TestHelper.check_logs)** method

## Release 1.3

- Fix logs encoding to "utf-8" for all platforms
- Add pattern support in **[`check_logs`](pytest_multilog.helper.TestHelper.check_logs)** method

## Release 1.2

- Added optional **timeout** argument to **[`check_logs`](pytest_multilog.helper.TestHelper.check_logs)** method

## Release 1.1

- Added **[`check_logs`](pytest_multilog.helper.TestHelper.check_logs)** method

## Release 1.0

Initial release
