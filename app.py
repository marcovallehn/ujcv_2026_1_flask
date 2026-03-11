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


@app.route("/")
def index():
    cur = conn.cursor()
    cur.execute("SELECT * FROM clientes")
    datos = cur.fetchall()
    cur.close()
    return render_template('index.html', lista_clientes=datos)


@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == 'POST':
        cursor = conn.cursor()
        nombre= request.form['CliNombre']
        apellido = request.form['CliApellido']
        correo = request.form['CliCorreo']
        telefono = request.form['CliTelefono']
        direccion=request.form['CliDireccion']
        cursor.execute("insert into clientes(CliNombre,CliApellido, CliCorreo, CliTelefono, CliDireccion) values(%s, %s, %s, %s, %s)", (nombre, apellido, correo, telefono, direccion))
        conn.commit()
        return redirect(url_for('index'))
    elif request.method=='GET':
         return render_template('agregar.html')




@app.route("/editar/<string:codigo>",  methods=["GET","POST"])
def editar(codigo):
    if request.method == 'GET':
        cur = conn.cursor()
        cur.execute("SELECT * FROM clientes where CliCodigo=%s", (codigo,))
        cliente = cur.fetchone()
        return render_template('editar.html', cliente=cliente)
    elif request.method=='POST': 
        cursor = conn.cursor()
        nombre= request.form['CliNombre']
        apellido = request.form['CliApellido']
        correo = request.form['CliCorreo']
        telefono = request.form['CliTelefono']
        direccion=request.form['CliDireccion']
        cursor.execute("update clientes set CliNombre=%s , CliApellido=%s, CliCorreo=%s, CliTelefono=%s, CliDireccion=%s where CliCodigo=%s", (nombre, apellido, correo, telefono, direccion,codigo))
        conn.commit()
        return redirect(url_for('index'))


@app.route("/eliminar")
def eliminar():
    pass

if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)