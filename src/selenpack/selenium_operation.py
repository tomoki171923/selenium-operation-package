# -*- coding: utf-8 -*-
# the following is not necessary if Python version is 3.9 or over.
from __future__ import annotations

# reference : https://www.selenium.dev/selenium/docs/api/py/index.html
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ExpectedConditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from PIL import ImageGrab
import os
from datetime import date
import time
import platform


class SeleniumOperation:
    def __init__(
        self,
        window_size: str = "1920,1080",
        headless: bool = True,
        remote_driver: bool = True,
    ) -> None:
        self.wait_time: int = 10
        self.screenshot_folder: str = None
        self.screenshot_base_name: str = None
        self.setWebdriver(window_size, headless, remote_driver)

    def __del__(self):
        self.driver.quit()

    # set webdriver
    def setWebdriver(
        self, window_size: str, headless: bool, remote_driver: bool
    ) -> None:
        # setting chrome driver
        chrome_options = Options()
        chrome_options.add_argument(f"--window-size={window_size}")
        if headless is True:
            chrome_options.add_argument("--headless")
        if remote_driver is True:
            self.driver = webdriver.Remote(
                command_executor=os.environ["SELENIUM_URL"],
                options=webdriver.ChromeOptions(),
            )
        else:
            path: str
            if "macOS" in platform.platform():
                path = "/usr/local/bin/chromedriver"
            elif "Windows" in platform.platform():
                path = "C:\\programs\\chromedriver"
            self.driver = webdriver.Chrome(options=chrome_options, executable_path=path)
        # for wait loading
        self.driver.implicitly_wait(self.wait_time)
        # for wait javascript function
        self.driver.set_script_timeout(self.wait_time)

    # set screenshot
    def setScreenshot(
        self, folder: str = "./screenshot/chrome/", base_file_name: str = None
    ) -> None:
        self.screenshot_folder = folder
        if not os.path.exists(self.screenshot_folder):
            os.mkdir(self.screenshot_folder)
        if base_file_name is None:
            self.screenshot_base_name = date.today().strftime("%Y-%m-%d")
        else:
            self.screenshot_base_name = base_file_name

    # go to the specified url.
    def goPage(self, url: str) -> None:
        self.driver.get(url)
        WebDriverWait(self.driver, self.wait_time).until(
            ExpectedConditions.presence_of_all_elements_located
        )

    # trimming blank character in first and last
    def trimStr(self, string: str) -> str:
        return string.lstrip().rstrip()

    # waiting until display specific element
    def waitDisplayElementByClass(self, class_name: str) -> None:
        wait = WebDriverWait(self.driver, self.wait_time)
        wait.until(
            ExpectedConditions.presence_of_element_located((By.CLASS_NAME, class_name))
        )
        time.sleep(1)

    # waiting until complete ajax action
    def waitCompleteAjax(self) -> None:
        wait = WebDriverWait(self.driver, self.wait_time)
        wait.until(
            lambda driver: self.driver.execute_script("return jQuery.active == 0")
        )
        time.sleep(1)

    # waiting until display alert
    def waitDisplayAlert(self) -> None:
        wait = WebDriverWait(self.driver, self.wait_time)
        wait.until(ExpectedConditions.alert_is_present())
        time.sleep(1)

    # ******************************************
    # screenshot functions
    # ******************************************
    # save a screenshot
    def takeScreenshot(self, zoom_ratio: int = 100) -> None:
        if self.screenshot_folder is None or self.screenshot_base_name is None:
            self.setScreenshot()
        script: str = "document.body.style.zoom='{}%'"
        self.driver.execute_script(script.format(zoom_ratio))
        filepath: str = self.__getScreenshotFilePath()
        self.driver.save_screenshot(filepath)

    # save a screenshot (alert only, and target is main screen only)
    # main screen -> If you use a laptop, laptop's screen is main screen.
    def takeAlertScreenshot(self) -> None:
        if self.screenshot_folder is None or self.screenshot_base_name is None:
            self.setScreenshot()
        img = ImageGrab.grab()
        filepath: str = self.__getScreenshotFilePath("-alert")
        img.save(filepath)

    # get screenshot file path
    def __getScreenshotFilePath(self, addition: str = None) -> str:
        base_filepath: str = self.screenshot_folder + self.screenshot_base_name
        if addition is not None:
            base_filepath += addition
        index: int = 1
        filepath: str = base_filepath + f"-{str(index).zfill(3)}.png"
        while os.path.isfile(filepath):
            index += 1
            filepath = base_filepath + f"-{str(index).zfill(3)}.png"
        return filepath

    # ******************************************
    # click functions
    # ******************************************
    # click the element.
    def click(self, element: WebElement) -> None:
        element.click()

    # find & click the element by id.
    def clickById(self, id: str) -> None:
        self.findElementById(id).click()

    # find & click the element by name. (It is the first element found.)
    def clickByName(self, name: str) -> None:
        self.findElementByName(name).click()

    # find & click the element by link text. (It is the first element found.)
    def clickByText(self, text: str) -> None:
        self.findElementByText(text).click()

    # find & click the element by class. (It is the first element found.)
    def clickByClass(self, classname: str) -> None:
        self.findElementByClass(classname).click()

    # ******************************************
    # scroll functions
    # ******************************************
    # scroll to the element.
    def scroll(self, element: WebElement) -> None:
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    # scroll to the element by id.
    def scrollById(self, id: str) -> WebElement:
        element: WebElement = self.findElementById(id)
        self.scroll(element)
        return element

    # scroll to the element by name. (It is the first element found.)
    def scrollByName(self, name: str) -> WebElement:
        element: WebElement = self.findElementByName(name)
        self.scroll(element)
        return element

    # scroll to the element by link text. (It is the first element found.)
    def scrollByText(self, text: str) -> WebElement:
        element: WebElement = self.findElementByText(text)
        self.scroll(element)
        return element

    # scroll to the element by class. (It is the first element found.)
    def scrollByClass(self, classname: str) -> WebElement:
        element: WebElement = self.findElementByClass(classname)
        self.scroll(element)
        return element

    # ******************************************
    # set value functions
    # ******************************************
    # set the value on the textbox by id.
    def setTextboxById(self, id: str, value: str) -> WebElement:
        element: WebElement = self.findElementById(id)
        element.send_keys(value)
        return element

    # set the value on the textbox by name. (It is the first element found.)
    def setTextboxByName(self, name: str, value: str) -> WebElement:
        element: WebElement = self.findElementByName(name)
        element.send_keys(value)
        return element

    # set the value on the textbox by class. (It is the first element found.)
    def setTextboxByClass(self, classname: str, value: str) -> WebElement:
        element: WebElement = self.findElementByClass(classname)
        element.send_keys(value)
        return element

    # set the value on the selectbox by id.
    def setSelectboxById(self, id: str, value: str) -> Select:
        select: Select = Select(self.findElementById(id))
        select.select_by_visible_text(value)
        return select

    # set the value on the selectbox by name. (It is the first element found.)
    def setSelectboxByName(self, name: str, value: str) -> Select:
        select: Select = Select(self.findElementByName(name))
        select.select_by_visible_text(value)
        return select

    # set the value on the selectbox by class. (It is the first element found.)
    def setSelectboxByClass(self, classname: str, value: str) -> Select:
        select: Select = Select(self.findElementByClass(classname))
        select.select_by_visible_text(value)
        return select

    # ******************************************
    # get functions
    # ******************************************
    # get options on the selectbox by id.
    def getSelectboxOptionsById(self, id: str) -> tuple[Select, list]:
        select: Select = Select(self.findElementById(id))
        option_texts: list = list()
        for option in select.options:
            text: str = self.trimStr(option.text)
            option_texts.append(text)
        return select, option_texts

    # get options on the selectbox by name. (It is the first element found.)
    def getSelectboxOptionsByName(self, name: str) -> tuple[Select, list]:
        select: Select = Select(self.findElementByName(name))
        option_texts: list = list()
        for option in select.options:
            text: str = self.trimStr(option.text)
            option_texts.append(text)
        return select, option_texts

    # ******************************************
    # find element functions
    # ******************************************
    # find an element by id.
    def findElementById(self, id: str) -> WebElement:
        return self.driver.find_element(By.ID, id)

    # find an element by name. (It is the first element found.)
    def findElementByName(self, name: str) -> WebElement:
        return self.driver.find_element(By.NAME, name)

    # find an element by link text. (It is the first element found.)
    def findElementByText(self, text: str) -> WebElement:
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, text)

    # find an element by class. (It is the first element found.)
    def findElementByClass(self, classname: str) -> WebElement:
        return self.driver.find_element(By.CLASS_NAME, classname)