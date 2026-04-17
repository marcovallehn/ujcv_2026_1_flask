from base import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    CliCodigo = db.Column(db.Integer, primary_key=True)
    CliNombre = db.Column(db.String(100))
    CliApellido = db.Column(db.String(100))
    CliCorreo = db.Column(db.String(100))
    CliTelefono = db.Column(db.String(20))
    CliDireccion = db.Column(db.String(255))

    def __repr__(self):
        return f'<Cliente {self.CliNombre}>'