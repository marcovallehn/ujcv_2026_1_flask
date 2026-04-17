
from flask import Blueprint, render_template, request, redirect, url_for
from db import get_connection

bpclientes = Blueprint('clientes', __name__, url_prefix='/clientes')


@bpclientes.route("/")
def clientes_index():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes")
    datos = cur.fetchall()
    cur.close()
    return render_template('clientes/index.html', lista_clientes=datos)


@bpclientes.route("/agregar", methods=["GET", "POST"])
def agregar_datos():
    if request.method == 'POST':
        conn = get_connection()
        cursor = conn.cursor()
        nombre= request.form['CliNombre']
        apellido = request.form['CliApellido']
        correo = request.form['CliCorreo']
        telefono = request.form['CliTelefono']
        direccion=request.form['CliDireccion']
        cursor.execute("insert into clientes(CliNombre,CliApellido, CliCorreo, CliTelefono, CliDireccion) values(%s, %s, %s, %s, %s)", (nombre, apellido, correo, telefono, direccion))
        conn.commit()
        return redirect(url_for('clientes_index'))
    elif request.method=='GET':
         return render_template('/clientes/agregar.html')


@bpclientes.route("/editar/<string:codigo>",  methods=["GET","POST"])
def editar(codigo):
    if request.method == 'GET':
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("SELECT * FROM clientes where CliCodigo=%s", (codigo,))
        cliente = cur.fetchone()
        return render_template('/clientes/editar.html', cliente=cliente)
    elif request.method=='POST': 
        cursor = conn.cursor()
        nombre= request.form['CliNombre']
        apellido = request.form['CliApellido']
        correo = request.form['CliCorreo']
        telefono = request.form['CliTelefono']
        direccion=request.form['CliDireccion']
        cursor.execute("update clientes set CliNombre=%s , CliApellido=%s, CliCorreo=%s, CliTelefono=%s, CliDireccion=%s where CliCodigo=%s", (nombre, apellido, correo, telefono, direccion,codigo))
        conn.commit()
        return redirect(url_for('clientes_index'))


@bpclientes.route("/eliminar/<string:codigo>",  methods=["GET","POST"])
def eliminar(codigo):
    if request.method == 'GET':
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes where CliCodigo=%s", (codigo,))
        cliente = cursor.fetchone()
        return render_template('/clientes/eliminar.html', cliente=cliente)
    elif request.method=='POST': 
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(" delete from clientes where CliCodigo=%s", (codigo,))
        conn.commit()
        return redirect(url_for('clientes_index'))
