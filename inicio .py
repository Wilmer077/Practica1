from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/quienes_somos')
def about():
    return render_template('quienessomos.html')

@app.route('/servicios')
def services():
    return render_template('servicios.html')

@app.route('/noticias')
def news():
    return render_template('noticias.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        mensaje = request.form['mensaje']
    return render_template('contacto.html')

if __name__ == '__main__':
    app.run(debug=True)

