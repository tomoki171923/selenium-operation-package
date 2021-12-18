# selenium-operation-package

Python package, which helps automate websites operation using [Selenium](https://www.selenium.dev/). The supported browser is Google Chrome.

## For User

### Install

```bash
pip install git+https://github.com/tomoki171923/selenium-operation-package#egg=selenpack
```

OR

Pipfile

```python
[packages]
selenpack = {git = "https://github.com/tomoki171923/selenium-operation-package.git", editable = true, ref = "main"}
```

OR

requirements.txt

```python
selenpack @ git+https://github.com/tomoki171923/selenium-operation-package@main
```

### Usage

```python
from selenpack.selenium_operation import SeleniumOperation

if __name__ == "__main__":
    selenium = SeleniumOperation()
    # visit Google.com
    selenium.goPage("https://www.google.com/")
    # take a screenshot
    selenium.setScreenshot(folder="./", base_file_name="example")
    selenium.takeScreenshot()
    # Google search
    el = selenium.setTextboxByName(name="q", value="weather japan")
    el.submit()
    # take a screenshot
    selenium.takeScreenshot()
    del selenium
```

### Environment

needs Selenium Server (Grid / Standalone) or Local web driver to execute selenpack.

reference the following.

<https://github.com/tomoki171923/docker-selenium-python>

## For Contributor

### Pre-Commit

```bash
brew install pre-commit
pre-commit install
```

### Build

```bash
docker-compose build
```

### Add Package

```bash
docker-compose run --rm app pipenv install PACKAGE_NAME
```
