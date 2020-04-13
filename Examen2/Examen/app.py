from flask import (
    Flask,
    g,
    redirect,
    render_template,
    request,
    session,
    url_for
)
import pyodbc

# Se instancian los datos que se capturaran del template del HTML
class User:
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __repr__(self):
        return f'<User: {self.username}>'

# Se establece el string de conexión con la base de datos
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=QS44\MILTONQS44;DATABASE=examen2;UID=examen;PWD=12345678')
cursor = conn.cursor()
cursor.execute("SELECT IdUsuario, Nombre, contrasena FROM Usuarios") #se carga el cursor con el select de los datos de la tabla de logins
rows= cursor.fetchall()
users = [] #Se crea una lista
for row in rows: # se recorre el cursor
    
    Id = row.IdUsuario
    Nombre = row.Nombre
    contrasena = row.contrasena
    users.append(User(id = Id, username = Nombre, password = contrasena)) #Se agregan los datos del cursos a una lista
    

app = Flask(__name__)
app.secret_key = 'somesecretkeythatonlyishouldknow'

#Este before requeste valida que si el Id es incorrecto muestre de nuevo el login
@app.before_request
def before_request():
    g.user = None

    if 'user_id' in session:
        user = [x for x in users if x.id == session['user_id']][0]
        g.user = user
        

@app.route('/login', methods=['GET', 'POST'])#este es el appi que contiene la pagina del login
def login():
    if request.method == 'POST': #Definimos que el metodo es un post
        session.pop('user_id', None)
        #Tomamos los datos que se ingresan en el html del login
        username = request.form['username']
        password = request.form['password']
       
        for user in users: #recorremos la lista que contiene los datos extraidos de la tabla usuarios
            if user.username == username and user.password == password: #validamos si el nombre de usuario y el password son correctos
                session['user_id'] = user.id
                return redirect(url_for('profile'))#redireccionamos a la pagina del profile si el resultado es correcto

    return render_template('login.html')#sino redirigimos de nuevo al login

@app.route('/profile')
def profile():
    if not g.user:
        return redirect(url_for('login'))

    return render_template('profile.html')


if __name__ == '__main__':
   app.run(port=5000)
