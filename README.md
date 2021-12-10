# selenium-operation-package

Python package. It helps operate [Selenium](https://www.selenium.dev/). Support browser is Google Chrome.

## Install

```bash
pip install git+https://github.com/tomoki171923/selenium-operation-package#egg=selenpack
```

## Usage

```python
from selenpack import SeleniumOperation

if __name__ == "__main__":
    selenium = SeleniumOperation()
    selenium.toPage("https://www.google.com/")
    selenium.setScreenshot(base_file_name="example")
    selenium.takeScreenshot()
    el = selenium.setTextboxByName(name="q", value="weather japan")
    el.submit()
    selenium.takeScreenshot()
    del selenium
```

## Environment

need Selenium Server (Grid / Standalone) or Local web driver to execute selenpack.

reference the following.
<https://github.com/tomoki171923/docker-selenium-python>
