from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os


db_user = os.environ.get('POSTGRES_USER')
db_password = os.environ.get('POSTGRES_PASSWORD')
db_name = os.environ.get('POSTGRES_DB')
db_host = os.environ.get('POSTGRES_HOST')

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{db_user}:{db_password}@{db_host}/{db_name}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Paquete(db.Model):
    id = db.Column(db.String, primary_key=True)
    estado = db.Column(db.String, nullable=False)


""" paquetes = {}  # TODO: Cambiar a una base de datos


@app.route('/paquetes', methods=['GET'])
def get_paquetes():
    return jsonify(paquetes)


@app.route('/paquete', methods=['POST'])
def registrar_paquete():
    datos = request.json
    id_paquete = datos['id']
    paquetes[id_paquete] = {'estado': 'registrado'}
    return jsonify({'mensaje': 'Paquete registrado con éxito'}), 201


@app.route('/paquete/<id>', methods=['GET'])
def obtener_estado_paquete(id):
    paquete = paquetes.get(id)
    if paquete:
        return jsonify({'id': id, 'estado': paquete['estado']})
    else:
        return jsonify({'mensaje': 'Paquete no encontrado'}), 404


@app.route('/paquete/<id>', methods=['PUT'])
def actualizar_estado_paquete(id):
    datos = request.json
    estado = datos.get('estado')
    if id in paquetes:
        paquetes[id]['estado'] = estado
        return jsonify({'mensaje': 'Estado actualizado'})
    else:
        return jsonify({'mensaje': 'Paquete no encontrado'}), 404 """


@app.route('/paquetes', methods=['GET'])
def get_paquetes():
    # Consulta todos los paquetes en la base de datos
    paquetes = Paquete.query.all()
    # Convierte los paquetes a formato JSON
    return jsonify({paquete.id: {"estado": paquete.estado} for paquete in paquetes})


@app.route('/paquete', methods=['POST'])
def registrar_paquete():
    datos = request.get_json()
    id_paquete = datos['id']
    nuevo_paquete = Paquete(id=id_paquete, estado='registrado')
    db.session.add(nuevo_paquete)
    db.session.commit()
    return jsonify({'mensaje': 'Paquete registrado con éxito'}), 201


@app.route('/paquete/<id>', methods=['GET'])
def obtener_estado_paquete(id):
    paquete = Paquete.query.get(id)
    if paquete:
        return jsonify({'id': id, 'estado': paquete.estado})
    else:
        return jsonify({'mensaje': 'Paquete no encontrado'}), 404


@app.route('/paquete/<id>', methods=['PUT'])
def actualizar_estado_paquete(id):
    datos = request.get_json()
    paquete = Paquete.query.get(id)
    if paquete:
        paquete.estado = datos.get('estado', paquete.estado)
        db.session.commit()
        return jsonify({'mensaje': 'Estado actualizado'})
    else:
        return jsonify({'mensaje': 'Paquete no encontrado'}), 404
    
@app.route('/contar', methods=['GET'])
def contar():
    count = Paquete.query.count()
    return jsonify(paquetes=count)

@app.route('/distintos', methods=['GET'])
def distintos_estados():
    distintos_estados = db.session.query(Paquete.estado).distinct().all()
    return jsonify([status[0] for status in distintos_estados])

@app.route('/resumen', methods=['GET'])
def get_status_summary():
    summary = db.session.query(Paquete.estado, db.func.count(Paquete.estado).label('count')).group_by(Paquete.estado).all()
    return jsonify({status: count for status, count in summary})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
