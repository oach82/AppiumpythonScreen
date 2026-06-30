"""Task: NavigateToNestingTabs — Home > App > Fragment > Nesting Tabs."""
from appium.webdriver.common.appiumby import AppiumBy
from screenplay.interactions import Click


_APP          = (AppiumBy.ACCESSIBILITY_ID, "App")
_FRAGMENT     = (AppiumBy.ACCESSIBILITY_ID, "Fragment")
_NESTING_TABS = (AppiumBy.ACCESSIBILITY_ID, "Nesting Tabs")


class NavigateToNestingTabs:
    """Navega desde Home hasta la pantalla Nesting Tabs."""

    def perform_as(self, actor):
        actor.attempts_to(
            Click.on(_APP),
            Click.on(_FRAGMENT),
            Click.on(_NESTING_TABS),
        )
