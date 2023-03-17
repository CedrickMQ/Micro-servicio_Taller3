from flask import Flask, jsonify
from faker import Faker
import itertools

app = Flask(__name__)
faker = Faker()

def random_data():
    profiles = [dict(itertools.islice(faker.profile().items(),6)) for data in range (13)]
    return profiles

@app.route('/crear registro')
def Create_profiles():
    try:
        data = random_data()
        return jsonify(data)
        print(data)
        return {"message":"Creando Registro"}
    except:
        return {"Error en crear registro"}
if __name__=='__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)