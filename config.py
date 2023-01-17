from pydantic import BaseSettings


class Config(BaseSettings):
    CHROME_URL = False
    SITE_URL = ""
    EMAIL_SELLER = ""
    PASSWORD_SELLER = ""
    EMAIL_BUYER = ""
    PASSWORD_BUYER = ""