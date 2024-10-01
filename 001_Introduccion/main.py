from flask import Flask

app = Flask(__name__)

@app.route('/')
def showIndex():
    return "Hola Mundo!"

app.run()