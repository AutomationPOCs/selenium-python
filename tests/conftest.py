import pytest
from config import Config
from models.bases.driver_base import DriverBase


@pytest.fixture(scope="class")
def config(request):
    config_pass = Config()
    request.cls.config = config_pass
    return config_pass


@pytest.fixture(autouse=True)
def setup(request, config):
    global driver
    driver = DriverBase(config.CHROME_URL, config.SITE_URL)
    request.cls.driver = driver
    return driver
