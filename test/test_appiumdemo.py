"""
Tests de UI para ApiDemos — Patrón Screenplay + Sauce Labs.

Ejecutar:
    pytest test/test_appiumdemo.py -v --alluredir=allure-results
"""
import allure
from appium.webdriver.common.appiumby import AppiumBy

from screenplay.tasks import NavigateToInvokeSearch, NavigateToNestingTabs, NavigateToIsolatedService
from screenplay.interactions import Click, TypeText, NavigateBack
from screenplay.interactions.select_checkbox import SelectCheckbox
from screenplay.questions import IsDisplayed


# ── Localizadores ──────────────────────────────────────────────────────────────
ACCESSIBILITY_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Accessibility")
QUERY_INPUT        = (AppiumBy.ID, "io.appium.android.apis:id/txt_query_prefill")
NESTING_TABS_ITEM  = (AppiumBy.ACCESSIBILITY_ID, "Nesting Tabs")
CHECK1             = (AppiumBy.ID, "io.appium.android.apis:id/menu1")
CHECK2             = (AppiumBy.ID, "io.appium.android.apis:id/menu2")
START_SERVICE_2    = (AppiumBy.ID, "io.appium.android.apis:id/start2")
BIND_SERVICE_2     = (AppiumBy.ID, "io.appium.android.apis:id/bind2")


# ── Test 1: Invoke Search ─────────────────────────────────────────────────────
@allure.feature("AppiumDemo - Búsqueda")
@allure.story("Invoke Search y volver al Home")
def test_invoke_search_and_back_home(actor):
    with allure.step("Navegar a App > Search > Invoke Search"):
        actor.attempts_to(NavigateToInvokeSearch())

    with allure.step("Escribir texto en el campo de búsqueda"):
        actor.attempts_to(TypeText.into(QUERY_INPUT).the_value("hola"))

    with allure.step("Volver 3 niveles hasta Home"):
        actor.attempts_to(NavigateBack.times(3))

    with allure.step("Verificar que la pantalla Home está visible"):
        assert actor.asks(IsDisplayed.element(ACCESSIBILITY_ITEM)), \
            "La pantalla Home no está visible tras volver"


# ── Test 2: Nesting Tabs ──────────────────────────────────────────────────────
@allure.feature("AppiumDemo - Fragment")
@allure.story("Seleccionar checkboxes en Nesting Tabs y volver")
def test_select_checks_and_back(actor):
    with allure.step("Navegar a App > Fragment > Nesting Tabs"):
        actor.attempts_to(NavigateToNestingTabs())

    with allure.step("Seleccionar ambos checkboxes"):
        actor.attempts_to(
            SelectCheckbox.identified_by(CHECK1),
            SelectCheckbox.identified_by(CHECK2),
        )

    with allure.step("Volver a Fragment"):
        actor.attempts_to(NavigateBack.once())

    with allure.step("Verificar que la pantalla Fragment está visible"):
        assert actor.asks(IsDisplayed.element(NESTING_TABS_ITEM)), \
            "La pantalla Fragment no está visible tras volver"


# ── Test 3: Isolated Service Controller ───────────────────────────────────────
@allure.feature("AppiumDemo - Service")
@allure.story("Start Service 2 y Bind Service 2")
def test_isolated_service_controller(actor):
    with allure.step("Navegar a App > Service > Isolated Service Controller"):
        actor.attempts_to(NavigateToIsolatedService())

    with allure.step("Verificar que la pantalla está visible"):
        assert actor.asks(IsDisplayed.element(START_SERVICE_2)), \
            "La pantalla Isolated Service Controller no está visible"

    with allure.step("Click en Start Service 2"):
        actor.attempts_to(Click.on(START_SERVICE_2))

    with allure.step("Activar Bind Service 2"):
        actor.attempts_to(SelectCheckbox.identified_by(BIND_SERVICE_2))
