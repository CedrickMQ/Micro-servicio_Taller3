from flask import Flask, render_template, request
from faker import Faker

app = Flask(__name__)
faker = Faker()

@app.route('/crear registro')
def Create_profiles():
    try:
        return {"message":"Creando Registro"}
    except:
        return {"Error en crear registro"}
if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)