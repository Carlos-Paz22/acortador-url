from flask import render_template, request, redirect, url_for
from src import app
from src.consultas.enlaces import EnlaceModel
import random ,string


enlaceModel = EnlaceModel()

@app.route("/", methods =['GET'])
def index():
    return render_template("enlace.html")

@app.route("/", methods =['GET', 'POST'])
def enlaceCrear():
    cadena = ""
    enlaceModel = EnlaceModel()
    for i in range(4):
        cadena += random.choice(string.ascii_letters)
       # print("letraaa",cadena)
    
    if request.method =='GET':    
        return render_template('enlace.html')
    else:
        enlacecorto="127.0.0.1:5000/"+ cadena
        url = request.form.get('url')
        enlaceModel.crearUrl(url,enlacecorto)
        return render_template('enlace.html',url=enlacecorto, cadena= cadena)



@app.route("/<link>" , methods =['GET'])
def abrirenlaces(link):
    enlacecorto ="127.0.0.1:5000/"+ link
    enlaceModel = EnlaceModel()
    encontrado = enlaceModel.find_link(enlacecorto)
    print("ecn",encontrado)
    if encontrado == "None":
        return redirect(url_for(enlaces))
    else:
        for islink in encontrado:
            print("enlace",type(islink))
        return redirect(islink)
