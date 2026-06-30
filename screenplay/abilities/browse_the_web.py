"""
Ability: BrowseTheWeb
Encapsula la capacidad de un Actor para interactuar con una aplicación móvil
a través del driver de Appium.
"""
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BrowseTheWeb:
    """
    Ability que otorga al Actor la capacidad de interactuar con la app móvil.
    Envuelve el Appium WebDriver y provee métodos de espera y búsqueda.
    """

    def __init__(self, driver: WebDriver):
        self._driver = driver

    @property
    def driver(self) -> WebDriver:
        return self._driver

    def find(self, locator: tuple, timeout: int = 10):
        """Espera y retorna el elemento."""
        return WebDriverWait(self._driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def find_clickable(self, locator: tuple, timeout: int = 10):
        """Espera a que el elemento sea clickeable y lo retorna."""
        return WebDriverWait(self._driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def is_present(self, locator: tuple, timeout: int = 5) -> bool:
        """Retorna True si el elemento aparece antes del timeout."""
        try:
            WebDriverWait(self._driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except Exception:
            return False

    def go_back(self):
        """Presiona el botón Back del dispositivo."""
        self._driver.back()
