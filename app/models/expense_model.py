from app import db
from datetime import datetime

class Empleado(db.Model):
    __tablename__ = 'empleados'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    gastos = db.relationship('Gasto', backref='empleado', lazy=True)
    
    @staticmethod
    def get_all():
        return Empleado.query.all()

class Departamento(db.Model):
    __tablename__ = 'departamentos'
    
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    gastos = db.relationship('Gasto', backref='departamento', lazy=True)
    
    @staticmethod
    def get_all():
        return Departamento.query.all()

class Gasto(db.Model):
    __tablename__ = 'gastos'
    
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.String(200), nullable=False)
    monto = db.Column(db.Float, nullable=False)
    id_empleado = db.Column(db.Integer, db.ForeignKey('empleados.id'), nullable=False)
    id_dept = db.Column(db.Integer, db.ForeignKey('departamentos.id'), nullable=False)
    
    @staticmethod
    def get_gastos_by_date_range(fecha_ini, fecha_fin):
        return db.session.query(
            Departamento.nombre.label('departamento'),
            Empleado.nombre.label('empleado'),
            Gasto.descripcion,
            Gasto.fecha,
            Gasto.monto
        ).join(
            Departamento,
            Gasto.id_dept == Departamento.id
        ).join(
            Empleado,
            Gasto.id_empleado == Empleado.id
        ).filter(
            Gasto.fecha.between(fecha_ini, fecha_fin)
        ).order_by(
            Departamento.nombre,
            Gasto.fecha
        ).all()
    
    @staticmethod
    def get_totales_by_date_range(fecha_ini, fecha_fin):
        return db.session.query(
            Departamento.nombre,
            db.func.sum(Gasto.monto).label('total')
        ).join(Gasto).filter(
            Gasto.fecha.between(fecha_ini, fecha_fin)
        ).group_by(Departamento.nombre).all()