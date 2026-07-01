Feature: Isolated Service Controller
  Como usuario de la app ApiDemos
  Quiero iniciar y vincular un servicio aislado
  Para verificar que los controles de servicios funcionan

  Scenario: Start Service 2 y Bind Service 2
    Given el actor está en la pantalla Home
    When navega a App > Service > Isolated Service Controller
    Then la pantalla Isolated Service Controller está visible
    When hace click en Start Service 2
    And activa el checkbox Bind Service 2
