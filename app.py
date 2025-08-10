from bottle import Bottle, run
import os

app = Bottle()

@app.route('/')
def inicio():
    return "<h1>Bienvenido a mi página de oración</h1><p>Dios te bendiga</p>"

@app.route('/historia')
def historia():
    return "<h1>Historia de los movimientos de oración</h1><p>Aquí hablaremos de grandes avivamientos y despertares espirituales.</p>"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # Usa el puerto que Render asigna
    run(app, host="0.0.0.0", port=port, debug=True)