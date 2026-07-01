Feature: Búsqueda en ApiDemos
  Como usuario de la app ApiDemos
  Quiero navegar a Invoke Search y escribir texto
  Para verificar que la navegación y entrada de texto funcionan

  Scenario: Navegar a Invoke Search, escribir texto y volver al Home
    Given el actor está en la pantalla Home
    When navega a App > Search > Invoke Search
    And escribe "hola" en el campo de búsqueda
    And vuelve 3 niveles atrás
    Then la pantalla Home está visible
