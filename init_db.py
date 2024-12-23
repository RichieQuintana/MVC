from app import create_app, db
from app.models.expense_model import Empleado, Departamento, Gasto
from datetime import datetime

def init_database():
    app = create_app()
    
    with app.app_context():
        # Recrear todas las tablas
        db.drop_all()
        db.create_all()
        
        # Crear departamentos
        departamentos = [
            Departamento(id=1, nombre='IT'),
            Departamento(id=2, nombre='Desarrollo'),
            Departamento(id=3, nombre='Diseño'),
            Departamento(id=4, nombre='Marketing')
        ]
        db.session.add_all(departamentos)
        
        # Crear empleados
        empleados = [
            Empleado(id=1, nombre='Zoila Baca'),
            Empleado(id=2, nombre='Aquiles C'),
            Empleado(id=3, nombre='Johnhy Metas')
        ]
        db.session.add_all(empleados)
        
        # Crear gastos
        gastos = [
            Gasto(
                id=1,
                fecha=datetime.strptime('16/11/2024', '%d/%m/%Y').date(),
                descripcion='UPS',
                monto=60,
                id_empleado=1,
                id_dept=1
            ),
            Gasto(
                id=2,
                fecha=datetime.strptime('22/11/2024', '%d/%m/%Y').date(),
                descripcion='Monitor secundario',
                monto=250,
                id_empleado=3,
                id_dept=2
            ),
            Gasto(
                id=3,
                fecha=datetime.strptime('23/11/2024', '%d/%m/%Y').date(),
                descripcion='Rollup',
                monto=60,
                id_empleado=3,
                id_dept=3
            ),
            Gasto(
                id=4,
                fecha=datetime.strptime('25/11/2024', '%d/%m/%Y').date(),
                descripcion='UPS',
                monto=60,
                id_empleado=1,
                id_dept=1
            )
        ]
        db.session.add_all(gastos)
        
        # Guardar todos los cambios
        db.session.commit()
        
        print("Base de datos inicializada exitosamente!")

if __name__ == '__main__':
    init_database()