"""Interaction: NavigateBack — presiona el botón Back del dispositivo."""


class NavigateBack:
    """Presiona el botón Back una cantidad determinada de veces."""

    def __init__(self, times: int = 1):
        self._times = times

    @staticmethod
    def once() -> "NavigateBack":
        return NavigateBack(1)

    @staticmethod
    def times(n: int) -> "NavigateBack":
        return NavigateBack(n)

    def perform_as(self, actor):
        for _ in range(self._times):
            actor.ability.go_back()
