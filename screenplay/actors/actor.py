"""
Actor — representa al usuario que interactúa con la aplicación.
Puede tener habilidades (abilities) y ejecutar tareas (tasks).
"""
from screenplay.abilities.browse_the_web import BrowseTheWeb


class Actor:
    """
    El Actor es quien ejecuta las acciones sobre la aplicación.
    Se le asignan abilities y ejecuta tasks/interactions/questions.
    """

    def __init__(self, name: str):
        self.name = name
        self._ability: BrowseTheWeb | None = None

    def who_can(self, ability: BrowseTheWeb) -> "Actor":
        """Asigna una ability al Actor. Retorna self para encadenamiento."""
        self._ability = ability
        return self

    @property
    def ability(self) -> BrowseTheWeb:
        """Retorna la ability BrowseTheWeb del Actor."""
        if self._ability is None:
            raise RuntimeError(f"El actor '{self.name}' no tiene ability asignada.")
        return self._ability

    def attempts_to(self, *tasks):
        """Ejecuta una o más tasks/interactions en secuencia."""
        for task in tasks:
            task.perform_as(self)

    def asks(self, question) -> any:
        """Realiza una question y retorna la respuesta."""
        return question.answered_by(self)
