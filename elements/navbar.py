from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from elements.base import BasePageElement
from locators.base import BasePageLocators


class NavBar(BasePageElement):

    def click_on_components_tab(self: object) -> object:
        """
        Click on components tab.
        """
        components_tab = self.driver.find_element(*BasePageLocators.COMPONENTS_TAB)
        components_tab.click()
        return self

    def click_on_monitors(self: object) -> object:
        """
        Click on monitors in components tab dropdown list.
        """
        monitors = self.driver.find_element(*BasePageLocators.MONITORS)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.element_to_be_clickable(BasePageLocators.MONITORS))
        monitors.click()
        return self

    def click_on_phones_tab(self: object) -> object:
        """
        Click on phones tab.
        """
        phones = self.driver.find_element(*BasePageLocators.PHONES)
        phones.click()
        return self