
from flask import Flask, flash, redirect, render_template, request, session, abort,Response,send_file
import test
import beta1

app = Flask(__name__)
app.debug = True
app.secret_key="hola mundo"
datos_plantilla=[]


@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return logout()


@app.route('/login',methods=["POST"])
def do_admin_login():
    if request.form['password'] == 'a' and request.form['username'] == 'a':
        session['logged_in'] = True
        return menu()
    else:
        flash('wrong password!')
        return logout()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route('/menu')
def menu():
    if session.get('logged_in')==False:
        return render_template('login.html')
    else:
        return render_template("menu.html")

@app.route('/Crear Informe')
def informe():
    if session.get('logged_in')==False:
        return render_template('login.html')
    else:
        return render_template("informe.html")

@app.route('/informe',methods= ['GET'])
def URL():
    if session.get('logged_in')==False:
        return render_template('login.html')
    else:
        URL = request.args.get('URL')
        URL= test.datos(URL)
        datos_plantilla = CrearVista(URL)
        document=beta1.crearDocx(datos_plantilla[1])
        document.save('demo.docx')
        return datos_plantilla[0]

@app.route('/CrearVista',methods= ['GET'])
def CrearVista(lista):
    datos=lista[0]
    info=lista[1]
    trabajadores=lista[2]
    render_template('vista.html', datos=datos, info=info, trabajadores=trabajadores)
    return [render_template('vista.html',datos=datos,info=info,trabajadores=trabajadores),lista]

@app.route("/descargar")
def descargar():
    filename='demo.docx'
    return send_file(
        filename,
        mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document")


if __name__ == '__main__':
    app.run(debug=True)