import pytest
from config.driver_setup import initialize_driver

@pytest.fixture
def setup():
    driver = initialize_driver()
    yield driver
    driver.quit()