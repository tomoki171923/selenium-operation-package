# selenium-operation-package

Python package. It helps operate [Selenium](https://www.selenium.dev/). Support browser is Google Chrome.

## Install

```bash
pip install git+https://github.com/tomoki171923/selenium-operation-package#egg=selenpack
```

## Usage

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

## Set Up Environment

needs Selenium Server (Grid / Standalone) or Local web driver to execute selenpack.

reference the following.

<https://github.com/tomoki171923/docker-selenium-python>
