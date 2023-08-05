from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.yaml'],
    environments=True,
    merge_enabled=True,
)

mongo_host = settings.mongodb.host
selenium_chrome_host = settings.selenium_chrome.host
selenium_firefox_host = settings.selenium_firefox.host
