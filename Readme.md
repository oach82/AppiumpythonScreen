# Appium Python — Screenplay Pattern + Sauce Labs

Suite de automatización móvil Android con Appium y Python, estructurada bajo el patrón **Screenplay** con ejecución exclusiva en **Sauce Labs**.

---

## Tecnologías

| Herramienta | Uso |
|---|---|
| Python 3.10+ | Lenguaje base |
| Appium 2.x | Automatización móvil |
| UIAutomator2 | Driver Android |
| pytest | Framework de pruebas |
| allure-pytest | Reportes con evidencia visual |
| python-dotenv | Credenciales via `.env` |
| Sauce Labs (us-west-1) | Ejecución en la nube |

---

## Patrón Screenplay — Estructura

```
proyecto/
├── screenplay/                        # Patrón Screenplay
│   ├── abilities/
│   │   └── browse_the_web.py          # Ability: wrapper del driver Appium
│   ├── actors/
│   │   └── actor.py                   # Actor: quien ejecuta las acciones
│   ├── interactions/                   # Acciones atómicas sobre la UI
│   │   ├── click.py                   # Click.on(locator)
│   │   ├── type_text.py              # TypeText.into(locator).the_value(text)
│   │   ├── navigate_back.py          # NavigateBack.times(n)
│   │   └── select_checkbox.py        # SelectCheckbox.identified_by(locator)
│   ├── tasks/                         # Flujos de alto nivel
│   │   ├── navigate_to_invoke_search.py
│   │   ├── navigate_to_nesting_tabs.py
│   │   └── navigate_to_isolated_service.py
│   └── questions/                     # Verificaciones sobre la UI
│       └── is_displayed.py            # IsDisplayed.element(locator)
│
├── test/
│   └── test_appiumdemo.py             # Tests usando el Actor
│
├── config.py                          # Config solo para Sauce Labs
├── conftest.py                        # Fixture: crea el Actor con ability
├── apps/
│   └── ApiDemos-debug.apk            # APK (subir a Sauce Labs Storage)
├── .env                               # Credenciales (NO subir al repo)
├── .env.example                       # Plantilla de credenciales
├── .gitignore
├── pytest.ini                         # Configuración pytest
├── requirements.txt                   # Dependencias Python
├── como_agregar_caso.md               # Guía para agregar nuevos tests
└── Readme.md
```

### Conceptos del patrón Screenplay

| Concepto | Qué hace | Ejemplo |
|---|---|---|
| **Actor** | Quien ejecuta las acciones | `Actor("Tester").who_can(BrowseTheWeb(driver))` |
| **Ability** | Capacidad del actor para interactuar | `BrowseTheWeb` (envuelve el driver) |
| **Task** | Flujo de alto nivel (varias interactions) | `NavigateToInvokeSearch()` |
| **Interaction** | Acción atómica sobre un elemento | `Click.on(locator)` |
| **Question** | Pregunta sobre el estado de la UI | `IsDisplayed.element(locator)` |

### Cómo se ve un test

```python
def test_ejemplo(actor):
    actor.attempts_to(NavigateToInvokeSearch())
    actor.attempts_to(TypeText.into(CAMPO).the_value("texto"))
    assert actor.asks(IsDisplayed.element(ELEMENTO))
```

---

## Prerrequisitos

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd <nombre-del-proyecto>
```

### 2. Crear y activar entorno virtual Python

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar credenciales

```bash
copy .env.example .env
```

Edita `.env` con tus credenciales de Sauce Labs:

```env
SAUCE_USERNAME=tu_usuario
SAUCE_ACCESS_KEY=tu_access_key
```

### 5. Subir el APK a Sauce Labs Storage

El APK debe estar en el storage de Sauce Labs antes de ejecutar los tests:

```bash
python -c "import os; from dotenv import load_dotenv; load_dotenv(); import requests; r = requests.post('https://api.us-west-1.saucelabs.com/v1/storage/upload', auth=(os.environ['SAUCE_USERNAME'], os.environ['SAUCE_ACCESS_KEY']), files={'payload': ('ApiDemos-debug.apk', open('apps/ApiDemos-debug.apk', 'rb'), 'application/octet-stream')}, data={'name': 'ApiDemos-debug.apk'}); print(f'Status: {r.status_code}')"
```

Esto solo se hace una vez (o cuando actualices el APK).

---

## Ejecución

```bash
# Activar entorno virtual
venv\Scripts\activate

# Ejecutar todos los tests
pytest test/test_appiumdemo.py -v --alluredir=allure-results

# Ejecutar un test específico
pytest test/test_appiumdemo.py::test_isolated_service_controller -v --alluredir=allure-results
```

---

## Reporte Allure

```bash
allure serve allure-results
```

---

## Ver resultados en Sauce Labs

1. Entra a https://app.saucelabs.com
2. Ve a **Automated → Test Results**
3. Filtra por build: `appium-screenplay-saucelabs`
