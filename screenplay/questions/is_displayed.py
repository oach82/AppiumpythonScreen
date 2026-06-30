"""Question: IsDisplayed — verifica si un elemento está visible en pantalla."""


class IsDisplayed:
    """Retorna True si el elemento identificado por el locator está visible."""

    def __init__(self, locator: tuple):
        self._locator = locator

    @staticmethod
    def element(locator: tuple) -> "IsDisplayed":
        return IsDisplayed(locator)

    def answered_by(self, actor) -> bool:
        return actor.ability.is_present(self._locator)
