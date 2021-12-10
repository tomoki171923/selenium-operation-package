from src.selenium_operation import SeleniumOperation


if __name__ == "__main__":
    selenium = SeleniumOperation()
    selenium.toPage("https://www.google.com/")
    selenium.setScreenshot(base_file_name="example")
    selenium.takeScreenshot()
    el = selenium.setTextboxByName(name="q", value="weather japan")
    print(el)
    el.submit()
    selenium.takeScreenshot()
    del selenium
