"""Interaction: TypeText — escribe texto en un campo."""


class TypeText:
    """Limpia un campo y escribe el texto indicado."""

    def __init__(self, text: str, locator: tuple):
        self._text = text
        self._locator = locator

    @staticmethod
    def into(locator: tuple) -> "_TypeTextBuilder":
        """Inicia la construcción: TypeText.into(locator).the_value('texto')"""
        return _TypeTextBuilder(locator)

    def perform_as(self, actor):
        field = actor.ability.find(self._locator)
        field.clear()
        field.send_keys(self._text)


class _TypeTextBuilder:
    def __init__(self, locator: tuple):
        self._locator = locator

    def the_value(self, text: str) -> TypeText:
        return TypeText(text, self._locator)
