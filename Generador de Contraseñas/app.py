from flask import Flask, render_template, request, jsonify
from Generador_Contraseñas import generar_contraseña, generar_contraseña_con_tema, generar_contraseña_desde_frase, evaluar_seguridad

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_password', methods=['POST'])
def generate_password():
    tipo = request.form.get('tipo')
    if tipo == 'tradicional':
        longitud = int(request.form.get('longitud', 12))
        incluir_simbolos = 'simbolos' in request.form
        incluir_numeros = 'numeros' in request.form
        password = generar_contraseña(longitud, incluir_simbolos, incluir_numeros)
        print(f"Contraseña generada: {password}")
    elif tipo == 'tematica':
        tema = request.form.get('tema', 'espacio')
        password = generar_contraseña_con_tema(tema)
        print(f"Contraseña generada: {password}")
    elif tipo == 'frase':
        frase = request.form.get('frase')
        password = generar_contraseña_desde_frase(frase)
        print(f"Contraseña generada: {password}")
    
    seguridad = evaluar_seguridad(password)
    print(f"Contraseña generada: {password}")
    return jsonify({'password': password, 'seguridad': seguridad})

if __name__ == '__main__':
    app.run(debug=True)
