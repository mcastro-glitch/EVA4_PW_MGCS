from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cantidad = int(request.form['cantidad'])
        precio_por_tarro = 9000
        total_sin_descuento = cantidad * precio_por_tarro

        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0.0

        total_con_descuento = total_sin_descuento * (1 - descuento)
        valor_descuento = total_sin_descuento - total_con_descuento

        return render_template('ejercicio1.html', nombre=nombre, total_sin_descuento=total_sin_descuento, total_con_descuento=total_con_descuento, valor_descuento=valor_descuento)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    message = ''
    if request.method == 'POST':
        nombre = request.form['nombre']
        contraseña = request.form['contraseña']

        if nombre == 'juan' and contraseña == 'admin':
            message = f'Bienvenido administrador {nombre}'
        elif nombre == 'pepe' and contraseña == 'user':
            message = f'Bienvenido usuario {nombre}'
        else:
            message = 'Usuario o contraseña incorrectos'

    return render_template('ejercicio2.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
