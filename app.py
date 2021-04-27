from flask import Flask, request, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields
from marshmallow_sqlalchemy import ModelSchema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://usuario:123456@host.docker.internal:3306/db'
db = SQLAlchemy(app)


# Model
class Empresa(db.Model):
    __tablename__ = "empresa"
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20))
    descripcion = db.Column(db.String(100))

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __repr__(self):
        return f"{self.id}"


db.create_all()


class EmpresaSchema(ModelSchema):
    class Meta(ModelSchema.Meta):
        model = Empresa
        sqla_session = db.session

    id = fields.Number(dump_only=True)
    nombre = fields.String(required=True)
    descripcion = fields.String(required=True)


@app.route('/api/v1/empresa', methods=['GET'])
def index():
    get_empresas = Empresa.query.all()
    empresa_schema = EmpresaSchema(many=True)
    empresas = empresa_schema.dump(get_empresas)
    return make_response(jsonify({"empresas": empresas}))


@app.route('/api/v1/empresa/<id>', methods=['GET'])
def get_empresa_by_id(id):
    get_empresa = Empresa.query.get(id)
    empresa_schema = EmpresaSchema()
    empresa = empresa_schema.dump(get_empresa)
    return make_response(jsonify({"empresa": empresa}))


@app.route('/api/v1/empresa/<id>', methods=['PUT'])
def update_empresa_by_id(id):
    data = request.get_json()
    get_empresa = Empresa.query.get(id)
    if data.get('nombre'):
        get_empresa.nombre = data['nombre']
    if data.get('descripcion'):
        get_empresa.descripcion = data['descripcion']
    db.session.add(get_empresa)
    db.session.commit()
    empresa_schema = EmpresaSchema(only=['id', 'nombre', 'descripcion'])
    empresa = empresa_schema.dump(get_empresa)
    return make_response(jsonify({"empresa": empresa}))


@app.route('/api/v1/empresa/<id>', methods=['DELETE'])
def delete_empresa_by_id(id):
    get_empresa = Empresa.query.get(id)
    db.session.delete(get_empresa)
    db.session.commit()
    return make_response("", 204)


@app.route('/api/v1/empresa', methods=['POST'])
def create_empresa():
    data = request.get_json()
    empresa_schema = EmpresaSchema()
    empresa = empresa_schema.load(data)
    result = empresa_schema.dump(empresa.create())
    return make_response(jsonify({"empresa": result}), 200)


if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0')