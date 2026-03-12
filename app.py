from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ujcv_2026_1_progra2',
            ssl_disabled=True  # Desactiva SSL
        )


@app.route("/clientes/")
def clientes_index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes")
    datos = cur.fetchall()
    cur.close()
    return render_template('clientes/index.html', lista_clientes=datos)


@app.route("/clientes/agregar", methods=["GET", "POST"])
def agregar_datos():
    if request.method == 'POST':
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


@app.route("/clientes/editar/<string:codigo>",  methods=["GET","POST"])
def editar(codigo):
    if request.method == 'GET':
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


@app.route("/clientes/eliminar/<string:codigo>",  methods=["GET","POST"])
def eliminar(codigo):
    if request.method == 'GET':
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM clientes where CliCodigo=%s", (codigo,))
        cliente = cursor.fetchone()
        return render_template('/clientes/eliminar.html', cliente=cliente)
    elif request.method=='POST': 
        cursor = conn.cursor()
        cursor.execute(" delete from clientes where CliCodigo=%s", (codigo,))
        conn.commit()
        return redirect(url_for('clientes_index'))


@app.route("/productos/")
def productos_index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos")
    datos = cur.fetchall()
    cur.close()
    return render_template('productos/index.html', lista_productos=datos)





if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)