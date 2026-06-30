"""Interaction: SelectCheckbox — activa un checkbox si no está marcado."""


class SelectCheckbox:
    """Activa el checkbox identificado por el locator si no está seleccionado."""

    def __init__(self, locator: tuple):
        self._locator = locator

    @staticmethod
    def identified_by(locator: tuple) -> "SelectCheckbox":
        return SelectCheckbox(locator)

    def perform_as(self, actor):
        checkbox = actor.ability.find(self._locator)
        if not checkbox.is_selected():
            checkbox.click()
