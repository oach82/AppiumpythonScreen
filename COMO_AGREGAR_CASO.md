# Cómo agregar un nuevo caso de prueba (Screenplay)

---

## Paso 1 — Identifica los elementos

Usa **Appium Inspector** o **Layout Inspector** de Android Studio para anotar los `resource-id` y `content-desc` de cada elemento involucrado.

---

## Paso 2 — ¿Necesitas una nueva Interaction?

Las interactions existentes son:

| Interaction | Uso |
|---|---|
| `Click.on(locator)` | Click en un elemento |
| `TypeText.into(locator).the_value(text)` | Escribir texto en un campo |
| `NavigateBack.times(n)` | Presionar Back N veces |
| `SelectCheckbox.identified_by(locator)` | Activar checkbox si no está marcado |

Si necesitas algo nuevo (ej: long press, swipe), crea un archivo en `screenplay/interactions/`:

```python
# screenplay/interactions/long_press.py
class LongPress:
    def __init__(self, locator):
        self._locator = locator

    @staticmethod
    def on(locator):
        return LongPress(locator)

    def perform_as(self, actor):
        element = actor.ability.find(self._locator)
        # lógica del long press...
```

---

## Paso 3 — Crea la Task (flujo de navegación)

Si el nuevo caso necesita navegar a una pantalla nueva, crea un archivo en `screenplay/tasks/`:

```python
# screenplay/tasks/navigate_to_mi_pantalla.py
from appium.webdriver.common.appiumby import AppiumBy
from screenplay.interactions import Click

_OPCION_A = (AppiumBy.ACCESSIBILITY_ID, "Opción A")
_OPCION_B = (AppiumBy.ACCESSIBILITY_ID, "Opción B")

class NavigateToMiPantalla:
    def perform_as(self, actor):
        actor.attempts_to(
            Click.on(_OPCION_A),
            Click.on(_OPCION_B),
        )
```

Agrega el import en `screenplay/tasks/__init__.py`:
```python
from screenplay.tasks.navigate_to_mi_pantalla import NavigateToMiPantalla
```

---

## Paso 4 — ¿Necesitas una nueva Question?

Si necesitas verificar algo diferente a "está visible", crea en `screenplay/questions/`:

```python
# screenplay/questions/has_text.py
class HasText:
    def __init__(self, locator, expected):
        self._locator = locator
        self._expected = expected

    @staticmethod
    def on(locator, expected):
        return HasText(locator, expected)

    def answered_by(self, actor):
        element = actor.ability.find(self._locator)
        return element.text == self._expected
```

---

## Paso 5 — Escribe el test

En `test/test_appiumdemo.py`:

```python
@allure.feature("AppiumDemo - Mi Feature")
@allure.story("Descripción del escenario")
def test_mi_nuevo_caso(actor):
    with allure.step("Navegar a la pantalla"):
        actor.attempts_to(NavigateToMiPantalla())

    with allure.step("Realizar la acción"):
        actor.attempts_to(Click.on(MI_BOTON))

    with allure.step("Verificar resultado"):
        assert actor.asks(IsDisplayed.element(MI_ELEMENTO))
```

---

## Paso 6 — Ejecutar

```bash
pytest test/test_appiumdemo.py::test_mi_nuevo_caso -v --alluredir=allure-results
```

---

## Resumen del flujo

```
1. Inspeccionar elementos (Appium Inspector)
       ↓
2. ¿Nueva interaction? → screenplay/interactions/
       ↓
3. ¿Nueva navegación? → screenplay/tasks/
       ↓
4. ¿Nueva verificación? → screenplay/questions/
       ↓
5. Escribir test en test/test_appiumdemo.py
       ↓
6. Ejecutar con pytest
```
