"""
Configuración para ejecución en Sauce Labs.
Lee credenciales desde el archivo .env en la raíz del proyecto.
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options

load_dotenv()

SAUCELABS_SERVER_URL = "https://ondemand.us-west-1.saucelabs.com/wd/hub"


class Config:
    """
    Configuración de Appium para Sauce Labs (us-west-1).
    Lee SAUCE_USERNAME y SAUCE_ACCESS_KEY desde .env.
    """

    def __init__(self):
        self.username = os.environ.get("SAUCE_USERNAME")
        self.access_key = os.environ.get("SAUCE_ACCESS_KEY")

        if not self.username:
            raise ValueError(
                "SAUCE_USERNAME no está definida. Configura la variable en el archivo .env."
            )
        if not self.access_key:
            raise ValueError(
                "SAUCE_ACCESS_KEY no está definida. Configura la variable en el archivo .env."
            )

        self.server_url = SAUCELABS_SERVER_URL
        self.options = self._build_options()

    def _build_options(self) -> UiAutomator2Options:
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.app = "storage:filename=ApiDemos-debug.apk"
        options.app_package = "io.appium.android.apis"
        options.app_activity = ".ApiDemos"
        options.no_reset = False
        options.load_capabilities({
            "sauce:options": {
                "username": self.username,
                "accessKey": self.access_key,
                "name": "AppiumDemo - Screenplay",
                "build": "appium-screenplay-saucelabs",
            }
        })
        return options
