# Cómo agregar un nuevo caso de prueba (BDD + Screenplay)

---

## Paso 1 — Escribe el escenario en Gherkin

Crea o edita un archivo `.feature` en `features/`. El nombre del Scenario se usará automáticamente como nombre de la sesión en Sauce Labs.

```gherkin
# features/mi_nuevo_caso.feature
Feature: Mi nueva funcionalidad
  Como usuario de la app ApiDemos
  Quiero realizar una acción
  Para verificar un comportamiento

  Scenario: Descripción del escenario
    Given el actor está en la pantalla Home
    When navega a App > Mi Opción
    And hace click en el botón X
    Then la pantalla Y está visible
```

---

## Paso 2 — Identifica los elementos

Usa **Appium Inspector** para obtener los `resource-id` y `content-desc` de cada elemento.

---

## Paso 3 — ¿Necesitas nuevas Interactions?

Las existentes:

| Interaction | Uso |
|---|---|
| `Click.on(locator)` | Click en un elemento |
| `TypeText.into(locator).the_value(text)` | Escribir texto |
| `NavigateBack.times(n)` | Presionar Back N veces |
| `SelectCheckbox.identified_by(locator)` | Activar checkbox |

Si necesitas algo nuevo, crea en `screenplay/interactions/`:

```python
# screenplay/interactions/mi_interaccion.py
class MiInteraccion:
    def __init__(self, locator):
        self._locator = locator

    @staticmethod
    def on(locator):
        return MiInteraccion(locator)

    def perform_as(self, actor):
        element = actor.ability.find(self._locator)
        # tu lógica aquí...
```

---

## Paso 4 — ¿Necesitas una nueva Task?

Si hay una navegación nueva, crea en `screenplay/tasks/`:

```python
# screenplay/tasks/navigate_to_mi_pantalla.py
from appium.webdriver.common.appiumby import AppiumBy
from screenplay.interactions import Click

_MI_OPCION = (AppiumBy.ACCESSIBILITY_ID, "Mi Opción")

class NavigateToMiPantalla:
    def perform_as(self, actor):
        actor.attempts_to(Click.on(_MI_OPCION))
```

---

## Paso 5 — Agrega los step definitions

En `test/test_bdd.py`, agrega los nuevos steps:

```python
# Cargar el nuevo feature
scenarios("../features/mi_nuevo_caso.feature")

# Nuevos localizadores
MI_ELEMENTO = (AppiumBy.ID, "io.appium.android.apis:id/mi_elemento")

# Nuevo step WHEN
@when("navega a App > Mi Opción")
def navega_mi_opcion(actor):
    actor.attempts_to(NavigateToMiPantalla())

@when("hace click en el botón X")
def click_boton_x(actor):
    actor.attempts_to(Click.on(MI_ELEMENTO))

# Nuevo step THEN
@then("la pantalla Y está visible")
def verificar_pantalla_y(actor):
    assert actor.asks(IsDisplayed.element(MI_ELEMENTO))
```

---

## Paso 6 — Ejecutar

```bash
pytest test/test_bdd.py -v --alluredir=allure-results
```

El nombre del test aparecerá automáticamente en Sauce Labs como nombre de la sesión (derivado del nombre del Scenario en el `.feature`).

---

## Resumen del flujo

```
1. Escribir escenario en features/*.feature (Gherkin)
       ↓
2. Inspeccionar elementos (Appium Inspector)
       ↓
3. ¿Nueva interaction? → screenplay/interactions/
       ↓
4. ¿Nueva navegación? → screenplay/tasks/
       ↓
5. Agregar steps en test/test_bdd.py
       ↓
6. Ejecutar con pytest
```
