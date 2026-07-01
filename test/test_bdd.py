"""
Step definitions BDD (pytest-bdd) conectados al patrón Screenplay.
Cada step usa el Actor para ejecutar Tasks, Interactions y Questions.
"""
import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from appium.webdriver.common.appiumby import AppiumBy

from screenplay.tasks import NavigateToInvokeSearch, NavigateToNestingTabs, NavigateToIsolatedService
from screenplay.interactions import Click, TypeText, NavigateBack
from screenplay.interactions.select_checkbox import SelectCheckbox
from screenplay.questions import IsDisplayed


# ── Cargar todos los .feature ──────────────────────────────────────────────────
scenarios("../features/invoke_search.feature")
scenarios("../features/nesting_tabs.feature")
scenarios("../features/isolated_service.feature")


# ── Localizadores ──────────────────────────────────────────────────────────────
ACCESSIBILITY_ITEM = (AppiumBy.ACCESSIBILITY_ID, "Accessibility")
QUERY_INPUT        = (AppiumBy.ID, "io.appium.android.apis:id/txt_query_prefill")
NESTING_TABS_ITEM  = (AppiumBy.ACCESSIBILITY_ID, "Nesting Tabs")
CHECK1             = (AppiumBy.ID, "io.appium.android.apis:id/menu1")
CHECK2             = (AppiumBy.ID, "io.appium.android.apis:id/menu2")
START_SERVICE_2    = (AppiumBy.ID, "io.appium.android.apis:id/start2")
BIND_SERVICE_2     = (AppiumBy.ID, "io.appium.android.apis:id/bind2")


# ── GIVEN ──────────────────────────────────────────────────────────────────────
@given("el actor está en la pantalla Home")
def actor_en_home(actor):
    """El fixture 'actor' de conftest.py ya abre la app en Home."""
    pass


# ── WHEN ───────────────────────────────────────────────────────────────────────
@when("navega a App > Search > Invoke Search")
def navega_invoke_search(actor):
    actor.attempts_to(NavigateToInvokeSearch())


@when("navega a App > Fragment > Nesting Tabs")
def navega_nesting_tabs(actor):
    actor.attempts_to(NavigateToNestingTabs())


@when("navega a App > Service > Isolated Service Controller")
def navega_isolated_service(actor):
    actor.attempts_to(NavigateToIsolatedService())


@when(parsers.parse('escribe "{texto}" en el campo de búsqueda'))
def escribe_texto(actor, texto):
    actor.attempts_to(TypeText.into(QUERY_INPUT).the_value(texto))


@when(parsers.parse("vuelve {n:d} niveles atrás"))
def vuelve_n_niveles(actor, n):
    actor.attempts_to(NavigateBack.times(n))


@when(parsers.parse("vuelve {n:d} nivel atrás"))
def vuelve_un_nivel(actor, n):
    actor.attempts_to(NavigateBack.times(n))


@when("selecciona el checkbox 1 si no está marcado")
def selecciona_check1(actor):
    actor.attempts_to(SelectCheckbox.identified_by(CHECK1))


@when("selecciona el checkbox 2 si no está marcado")
def selecciona_check2(actor):
    actor.attempts_to(SelectCheckbox.identified_by(CHECK2))


@when("hace click en Start Service 2")
def click_start_service(actor):
    actor.attempts_to(Click.on(START_SERVICE_2))


@when("activa el checkbox Bind Service 2")
def activa_bind_service(actor):
    actor.attempts_to(SelectCheckbox.identified_by(BIND_SERVICE_2))


# ── THEN ───────────────────────────────────────────────────────────────────────
@then("la pantalla Home está visible")
def verificar_home(actor):
    assert actor.asks(IsDisplayed.element(ACCESSIBILITY_ITEM)), \
        "La pantalla Home no está visible"


@then("la pantalla Fragment está visible")
def verificar_fragment(actor):
    assert actor.asks(IsDisplayed.element(NESTING_TABS_ITEM)), \
        "La pantalla Fragment no está visible"


@then("la pantalla Isolated Service Controller está visible")
def verificar_isolated_service(actor):
    assert actor.asks(IsDisplayed.element(START_SERVICE_2)), \
        "La pantalla Isolated Service Controller no está visible"
