"""Task: NavigateToInvokeSearch — Home > App > Search > Invoke Search."""
from appium.webdriver.common.appiumby import AppiumBy
from screenplay.interactions import Click


# Localizadores
_APP            = (AppiumBy.ACCESSIBILITY_ID, "App")
_SEARCH         = (AppiumBy.ACCESSIBILITY_ID, "Search")
_INVOKE_SEARCH  = (AppiumBy.ACCESSIBILITY_ID, "Invoke Search")


class NavigateToInvokeSearch:
    """Navega desde Home hasta la pantalla Invoke Search."""

    def perform_as(self, actor):
        actor.attempts_to(
            Click.on(_APP),
            Click.on(_SEARCH),
            Click.on(_INVOKE_SEARCH),
        )
