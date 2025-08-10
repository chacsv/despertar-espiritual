from bottle import Bottle, run, template

app = Bottle()

# Ruta principal
@app.route('/')
def home():
    return template("""
        <h1>Bienvenido a mi página de oración</h1>
        <p>Dios te bendiga. Este es un espacio para interceder y compartir sobre un despertar espiritual.</p>
        <a href="/historia">Ver historia de movimientos de oración</a>
    """)

# Página de historia
@app.route('/historia')
def historia():
    return template("""
        <h1>Historia de los movimientos de oración</h1>
        <p>Desde tiempos bíblicos hasta la actualidad, Dios ha levantado movimientos de oración que han impactado
        ciudades, naciones y generaciones.</p>
        <a href="/">Volver al inicio</a>
    """)

if __name__ == "__main__":
    # En Render se usa el puerto que da la variable de entorno PORT
    import os
    port = int(os.environ.get("PORT", 8080))
    run(app, host='0.0.0.0', port=port, debug=True, reloader=True)