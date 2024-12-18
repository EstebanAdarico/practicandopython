from flask import Flask , request,render_template

#creando objeto de la clase flask
app = Flask(__name__)

#creamos la primera ruta
@app.route('/')
def index ():
   #return '<center><h1>BIENVENIDO  AL MUNDO DE FLASK inmundo animal </h1></center>'

   #RETORNANDO UN REDER TEMPLATE DESDE UN ARCHIVO HTML
   nombre = request.args.get('nombre','no hay nombre')


   #HACEMOS UNA BUENA PRACTICA CREANDO DICCIONARIOS
   context = {
      'nombre':nombre,
   }
   # **context va a enviarle el listado del diccionario con sus valores a la plantilla de index.html'
   #este comentario es para actualizar el render template de index a home.html 
   return render_template('home.html',**context)

@app.route('/peliculas')
def peliculas():
   listaPeliculas= ['CODA','ENCANTO','RENACIDO','YO ROBOT']
   nombre = request.args.get('nombre','no hay nombre')
   #HACEMOS UNA BUENA PRACTICA CREANDO DICCIONARIOS
   #probando el ciclo for para la plantilla con esta lista 
   context={
      'peliculas':listaPeliculas,
      'nombre':nombre
   }
   return render_template('peliculas.html',**context)


#PARA DESPLEGAR NUESTRA APP WEB Y SE PUEDA ACTULIZAR
app.run(debug = True)

