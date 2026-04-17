from flask import Blueprint, render_template, request, redirect, url_for
from models import Cliente
from base import db

bpclientes = Blueprint('clientes', __name__, url_prefix='/clientes')


@bpclientes.route("/")
def clientes_index():
    datos = Cliente.query.all()
    return render_template('clientes/index.html', lista_clientes=datos)


@bpclientes.route("/agregar", methods=["GET", "POST"])
def agregar_datos():
    if request.method == 'POST':
        nuevo = Cliente(
            CliNombre=request.form['CliNombre'],
            CliApellido=request.form['CliApellido'],
            CliCorreo=request.form['CliCorreo'],
            CliTelefono=request.form['CliTelefono'],
            CliDireccion=request.form['CliDireccion']
        )
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('clientes.clientes_index'))

    return render_template('clientes/agregar.html')


@bpclientes.route("/editar/<int:codigo>", methods=["GET", "POST"])
def editar(codigo):
    cliente = Cliente.query.get_or_404(codigo)

    if request.method == 'POST':
        cliente.CliNombre = request.form['CliNombre']
        cliente.CliApellido = request.form['CliApellido']
        cliente.CliCorreo = request.form['CliCorreo']
        cliente.CliTelefono = request.form['CliTelefono']
        cliente.CliDireccion = request.form['CliDireccion']

        db.session.commit()
        return redirect(url_for('clientes.clientes_index'))

    return render_template('clientes/editar.html', cliente=cliente)


@bpclientes.route("/eliminar/<int:codigo>", methods=["GET", "POST"])
def eliminar(codigo):
    cliente = Cliente.query.get_or_404(codigo)

    if request.method == 'POST':
        db.session.delete(cliente)
        db.session.commit()
        return redirect(url_for('clientes.clientes_index'))

    return render_template('clientes/eliminar.html', cliente=cliente)