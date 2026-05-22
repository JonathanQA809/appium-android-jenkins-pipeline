from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait


SETTINGS_PACKAGE = "com.android.settings"
SETTINGS_ACTIVITY = "com.android.settings.Settings"


def test_android_settings_app():

    capabilities = UiAutomator2Options()

    capabilities.platform_name = "Android"
    capabilities.device_name = "emulator-5554"
    capabilities.automation_name = "UiAutomator2"

    capabilities.app_package = SETTINGS_PACKAGE
    capabilities.app_activity = SETTINGS_ACTIVITY
    capabilities.app_wait_activity = "*"

    capabilities.no_reset = True
    capabilities.new_command_timeout = 300

    driver = None

    try:
        driver = webdriver.Remote(
            "http://127.0.0.1:4723",
            options=capabilities
        )

        driver.activate_app(SETTINGS_PACKAGE)

        WebDriverWait(driver, 10).until(
            lambda mobile_driver: mobile_driver.current_package == SETTINGS_PACKAGE
        )

        assert driver.current_package == SETTINGS_PACKAGE

    finally:
        if driver:
            driver.quit()
