from elements.base import BasePageElement


class Button(BasePageElement):

    def __init__(self, driver, locator):
        super().__init__(driver)
        self.btn = self.driver.find_element(*locator)

    def click(self):
        self.btn.click()
