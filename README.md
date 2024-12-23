**Sistema de Control de Gastos por Departamento**

Sistema web desarrollado con Flask que permite gestionar y visualizar gastos departamentales, implementando el patrón MVC.

**Características**

Filtrado de gastos por rango de fechas
Visualización de gastos por departamento y empleado
Cálculo automático de totales por departamento
Interfaz responsiva con Bootstrap
Base de datos SQLite

**Tecnologías**

Python 3.8+
Flask
SQLAlchemy

**Estructura MVC**

Models: /app/models/expense_model.py

Clases: Empleado, Departamento, Gasto
Lógica de base de datos


Views: /app/templates/expenses/

Interfaz de usuario
Formularios y visualización


Controllers: /app/controllers/expense_controller.py

Manejo de rutas
Lógica de negocio

Deployado en Render
