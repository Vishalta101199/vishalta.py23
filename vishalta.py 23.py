import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace with your desired browser driver path if not using webdriver_manager
# from selenium.webdriver.chrome import webdriver

class TestIMDBSearch:

    @pytest.fixture(scope="class")
    def driver(self):
        # Use webdriver_manager for automatic driver setup (optional)
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(ChromeDriverManager().install())

        # Alternatively, provide your own driver path
        # driver = webdriver.Chrome("/path/to/chromedriver")

        driver.implicitly_wait(10)  # Set implicit wait for convenience (optional)
        yield driver
        driver.quit()

    def test_imdb_search_pom(self, driver):
        # Page Object Model (POM) elements
        name_field = (By.ID, "name")
        birth_date_from = (By.ID, "birth_date-from")
        birth_date_to = (By.ID, "birth_date-to")
        gender_select = (By.ID, "gender")
        keyword_field = (By.ID, "keywords")
        search_button = (By.ID, "find")

        # Navigate to IMDb search page
        driver.get("https://www.imdb.com/search/name/")

        # Enter data using POM elements
        name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(name_field)
        )
        name_input.send_keys("Tom Hanks")

        birth_date_from_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(birth_date_from)
        )
        birth_date_from_input.send_keys("1956-07-09")

        birth_date_to_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(birth_date_to)
        )
        birth_date_to_input.send_keys("2024-03-27")

        gender_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(gender_select)
        )
        gender_dropdown.select_by_value("male")

        keyword_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(keyword_field)
        )
        keyword_input.send_keys("actor")

        # Click search button using explicit wait for clickability
        search_button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(search_button)
        )
        search_button_element.click()

        # Assertions (add as needed to verify search results)
        # ...

if __name__ == "__main__":
    pytest.main()
