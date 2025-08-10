from bottle import Bottle, run, template
import os

app = Bottle()

@app.route('/')
def home():
    return template('<h1>Bienvenido a la página de oración</h1><p>Dios te bendiga</p>')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))  # Render envía el puerto aquí
    run(app, host='0.0.0.0', port=port)