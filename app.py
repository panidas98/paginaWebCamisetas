from flask import Flask, render_template

app = Flask(__name__)

productos_hombre = [
    {
        'nombre': 'Camiseta Básica Blanca',
        'precio': 19.99,
        'imagen': 'img/hombre1.jpeg'
    },
    {
        'nombre': 'Camiseta Estampada Azul',
        'precio': 24.99,
        'imagen': 'img/hombre2.jpg'
    }
]

productos_mujer = [
    {
        'nombre': 'Camiseta Rosa Casual',
        'precio': 21.99,
        'imagen': 'img/mujer1.jpg'
    },
    {
        'nombre': 'Camiseta Verde Sport',
        'precio': 23.99,
        'imagen': 'img/mujer2.jpg'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hombre')
def hombre():
    return render_template('hombre.html', productos=productos_hombre)

@app.route('/mujer')
def mujer():
    return render_template('mujer.html', productos=productos_mujer)

if __name__ == '__main__':
    app.run(debug=True)