"""Task: NavigateToIsolatedService — Home > App > Service > Isolated Service Controller."""
from appium.webdriver.common.appiumby import AppiumBy
from screenplay.interactions import Click


_APP                     = (AppiumBy.ACCESSIBILITY_ID, "App")
_SERVICE                 = (AppiumBy.ACCESSIBILITY_ID, "Service")
_ISOLATED_SERVICE_CTRL   = (AppiumBy.ACCESSIBILITY_ID, "Isolated Service Controller")


class NavigateToIsolatedService:
    """Navega desde Home hasta la pantalla Isolated Service Controller."""

    def perform_as(self, actor):
        actor.attempts_to(
            Click.on(_APP),
            Click.on(_SERVICE),
            Click.on(_ISOLATED_SERVICE_CTRL),
        )
