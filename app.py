from flask import Flask, render_template

from bpClientes import bpclientes
from bpProductos import bpproductos
from bpProveedores import bpproveedores
import bpProductos


app = Flask(__name__)

app.register_blueprint(bpclientes)
app.register_blueprint(bpproductos)
app.register_blueprint(bpproveedores)


@app.route("/")
def index():
    return render_template('index.html')



if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)