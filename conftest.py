"""
Conftest — crea el Actor con la ability BrowseTheWeb conectado a Sauce Labs.
"""
import allure
import pytest
from appium import webdriver
from config import Config
from screenplay.abilities import BrowseTheWeb
from screenplay.actors import Actor


@pytest.fixture
def actor(request):
    """
    Fixture que crea un Actor con la ability de navegar la app en Sauce Labs.
    El nombre del test se envía a Sauce Labs como nombre de la sesión.
    """
    test_name = request.node.name.replace("test_", "").replace("_", " ").title()
    config = Config(test_name=test_name)
    drv = webdriver.Remote(
        command_executor=config.server_url,
        options=config.options
    )
    the_actor = Actor("Tester").who_can(BrowseTheWeb(drv))
    yield the_actor
    drv.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Captura screenshot para Allure al finalizar cada test."""
    outcome = yield
    report = outcome.get_result()
    if report.when == "call":
        the_actor = item.funcargs.get("actor")
        if the_actor is not None:
            try:
                screenshot = the_actor.ability.driver.get_screenshot_as_png()
                nombre = "screenshot_fallo" if report.failed else "screenshot_final"
                allure.attach(screenshot, name=nombre, attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass
