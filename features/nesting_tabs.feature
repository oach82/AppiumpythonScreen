Feature: Selección de checkboxes en Nesting Tabs
  Como usuario de la app ApiDemos
  Quiero navegar a Nesting Tabs y activar los checkboxes
  Para verificar que los controles de selección funcionan

  Scenario: Seleccionar ambos checkboxes y volver a Fragment
    Given el actor está en la pantalla Home
    When navega a App > Fragment > Nesting Tabs
    And selecciona el checkbox 1 si no está marcado
    And selecciona el checkbox 2 si no está marcado
    And vuelve 1 nivel atrás
    Then la pantalla Fragment está visible
