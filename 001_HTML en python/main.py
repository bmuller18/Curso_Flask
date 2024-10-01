from flask import Flask

app = Flask(__name__)

@app.route('/')
def showIndex():
    return '''
        <h1> HOLA MUNDO! </h1>
        <h2> HOLA MUNDO! </h2>
        <h3> HOLA MUNDO! </h3>

        <form >
        <label for="nombre">Nombre:</label><br>

        <label for="email">Email:</label><br>

        <label for="mensaje">Mensaje:</label><br>>

        <input value="Enviar">
    </form>
            '''

app.run()