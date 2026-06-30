"""Interaction: Click — hace click en un elemento."""


class Click:
    """Hace click en el elemento identificado por el locator."""

    def __init__(self, locator: tuple):
        self._locator = locator

    @staticmethod
    def on(locator: tuple) -> "Click":
        """Factory method para mejor legibilidad."""
        return Click(locator)

    def perform_as(self, actor):
        actor.ability.find_clickable(self._locator).click()
