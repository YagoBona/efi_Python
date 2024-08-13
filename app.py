from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Crear la aplicación Flask
app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///celulares.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Importar los modelos
from modelos import Equipo, Modelo, Categoria

# Definir rutas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/modelos')
def list_modelos():
    modelos = Modelo.query.all()
    return render_template('equipos/list.html', modelos=modelos)

@app.route('/categorias')
def list_categorias():
    categorias = Categoria.query.all()
    return render_template('categorias/list.html', categorias=categorias)


@app.route('/equipos/create', methods=['GET', 'POST'])
def create_equipo():
    if request.method == 'POST':
        nuevo_equipo = Equipo(
            nombre=request.form['nombre'],
            modelo_id=request.form['modelo_id'],
            categoria_id=request.form['categoria_id'],
            costo=request.form['costo']
        )
        db.session.add(nuevo_equipo)
        db.session.commit()
        return redirect(url_for('list_equipos'))
    else:
        modelos = Modelo.query.all()
        categorias = Categoria.query.all()
        return render_template('equipos/create.html', modelos=modelos, categorias=categorias)
