from flask import Flask,render_template
from flask_bootstrap import Bootstrap
import pandas
import psycopg2

app = Flask(__name__)
Bootstrap(app)


def mostarUsuarios():
    conexion = psycopg2.connect(host = "localhost", database= "practica", user="postgres", password="1234") #String de conexion hacia la base de datos
    df = pandas.read_sql_query("select * from usuarios",conexion))#sentencia sql que realiza la peticion a la base
    
    print(df)#muestra en pantalla todos los datos de la tabla 
    conexion.close()



def mostrarEquipos():
    conexion = psycopg2.connect(host = "localhost", database= "practica", user="postgres", password="1234") #String de conexion hacia la base de datos
    df = pandas.read_sql_query("select * from equipos",conexion)
    
    print(df)#muestra en pantalla todos los datos de la tabla 
    conexion.close()

#agregar un nuevo usuario a la base de datos 
def agregarUsiarios (id,nombre,apellidos,contraseÃ±a,rol_usuarios,intentos):
    conexion = psycopg2.connect(host = "localhost", database= "practica", user="postgres", password="1234") #String de conexion hacia la base de datos
     
    cur = conexion.cursor()#puntero que me permite realizar acciones hacia la base de datos 
   
    cur.execute("INSERT INTO public.usuarios  VALUES (%s,%s,%s,%s,%s)",(id,nombre,apellidos,contraseÃ±a,rol_usuarios)))#sentencia sql que realiza la peticion a la base
    cur.close()
    conexion.commit()#funciona para realizar el guadado y actualizado dentro de la base de datos
#agregar un nuevo equipo a la base de datos 
def agregarEquipo(id_equipo, nombre_equipo, id_usuario):
    conexion = psycopg2.connect(host = "localhost", database= "practica", user="postgres", password="1234") #String de conexion hacia la base de datos
     
    cur = conexion.cursor()#puntero que me permite realizar acciones hacia la base de datos 
    cur.execute("INSERT INTO public.equipos(id_equipo, nombre_equipo, id_usuario) VALUES (%s, %s, %s)", (id_equipo,nombre_equipo,id_usuario)))#sentencia sql que realiza la peticion a la base
    conexion.commit()#funciona para realizar el guadado y actualizado dentro de la base de datos
#modificar datos de un equipo 
def modificarUsuarios(id,nombre,apellidos,contraseÃ±a):
    conexion = psycopg2.connect(host = "localhost", database= "practica", user="postgres", password="1234")  #String de conexion hacia la base de datos 
    cur = conexion.cursor()#puntero que me permite realizar acciones hacia la base de datos 
    cur.execute("UPDATE public.usuarios SET nombre=%s,apellidos=%s,contraseÃ±a=%s  where id_usuario= %s ",(nombre,apellidos,contraseÃ±a,id)))#sentencia sql que realiza la peticion a la base
    conexion.commit()#funciona para realizar el guadado y actualizado dentro de la base de datos
    print("Los datos han sido actualizados")
    mostarUsuarios()
#modificar datos de un equipo 
def ModificarEquipo(id_equipo,nombre_equipo):
    conexion = psycopg2.connect(host = "localhost", database= "practica", user="postgres", password="1234") #String de conexion hacia la base de datos  
    cur = conexion.cursor()#puntero que me permite realizar acciones hacia la base de datos 
    cur.execute("UPDATE public.equipos SET nombre_equipo=%s  where id_equipo= %s ",(nombre_equipo,id_equipo)))#sentencia sql que realiza la peticion a la base
    conexion.commit()#funciona para realizar el guadado y actualizado dentro de la base de datos
    print("Los datos han sido actualizados")
    mostrarEquipos()
#eliminar un usuario, de la tabla en la base de datos
def eliminarUsuarios(id):
    conexion = psycopg2.connect(host = "localhost", database= "practica", user="postgres", password="1234") #String de conexion hacia la base de datos  
    cur = conexion.cursor()#puntero que me permite realizar acciones hacia la base de datos 
    cur.execute("DELETE FROM  public.usuarios   where id_usuario = %s ",[id]))#sentencia sql que realiza la peticion a la base
    conexion.commit()
    print("Los datos han sido actualizados")
    mostarUsuarios()
#eliminar un equipo, de la tabla en la base de datos
def eliminarEquipos(id_equipo):
    conexion = psycopg2.connect(host = "localhost", database= "practica", user="postgres", password="1234")  #String de conexion hacia la base de datos
    cur = conexion.cursor()#puntero que me permite realizar acciones hacia la base de datos 
    cur.execute("""DELETE FROM equipos  WHERE  id_equipo=%s""",[id_equipo])#sentencia sql que realiza la peticion a la base
    conexion.commit()#funciona para realizar el guadado y actualizado dentro de la base de datos 
    print("Los datos han sido actualizados\n")
    mostrarEquipos()
#filtro de usuarios, busca un usuario por id y lo mmuestra en pantalla    
def buscarUsuarios(id):
    conexion = psycopg2.connect(host = "localhost", database= "practica", user="postgres", password="1234") #String de conexion hacia la base de datos

    cur = conexion.cursor()#puntero que me permite realizar acciones hacia la base de datos 

    cur.execute("SELECT * FROM usuarios")#sentencia sql que realiza la peticion a la base
#ciclo que recorre la lista y muestra su encuentra el equipo que se busca
    rows = cur.fetchall ()
    for r in rows :
        if id == r[0]:
            print(f"id = {r[0]} nombre = {r[1]} Apellidos = {r[2]} ContraseÃ±a = {r[3]} rol = {r[4]} intentos = {r[5]}")
            
            
    else:
        print("El usuario no existe.")   

    cur.close()
    conexion.close()
#filtro de equipos, busca un equipo por id y lo mmuestra en pantalla
def buscarEquipos(id_equipo):
    conexion = psycopg2.connect(host = "localhost", database= "practica", user="postgres", password="1234") #String de conexion hacia la base de datos

    cur = conexion.cursor()#puntero que me permite realizar acciones hacia la base de datos 

    cur.execute("SELECT * FROM equipos")#sentencia sql que realiza la peticion a la base
#ciclo que recorre la lista y muestra su encuentra el equipo que se busca
    rows = cur.fetchall ()
    for r in rows :
        if id_equipo == r[0]:
            print(f"id del Equipo = {r[0]} nombre = {r[1]} id lider = {r[2]} ")
            
            
    else:
        print("El usuario no existe.")   

    cur.close()
    conexion.close()

if __name__ == "__main__":
    print("******************************************************************")
    opcion =int(input("Menu del programa\nOpcion 1: Mostrar los Usuarios "
    "\nOpcion 2: Mostrar Equipos Creados \nOpcion 3: Insertar Usuarios al Sistema "
    "\nOpcion 4: Insertar Equipos al Sistema\nOpcion 5:Modificar Usuarios del Sistema "
    "\nOpcion 6:Modificar Equipos del Sistema \nOpcion 7: Eliminar Usuario del Sistema "
    "\nOpcion 8: Eliminar Equipos del Sistema "
    "\nOpcion 9: Buscar un usuario en el Sistema \nOpcion 10: Buscar un Equipo en el Sistema\n  "))
    print("******************************************************************")
    #menu del sistema para realizar los procesos de mantenimento.
    if opcion == 1:
        mostarUsuarios()
                                
    if opcion == 2:
        mostrarEquipos()

    if opcion == 3:
        id = int(input("intruduzca el ID:\n"))
        nombre = input("Ingrese el Nombre:\n")
        apellidos = input("Ingrese el Apelidos:\n")
        contraseÃ±a = input("Ingrese la ContraseÃ±a:\n ")
        rol_usuarios = input("Ingrese el Rol del Usuario en el Sistema:\n")
        intentos = int(input("Intruduzca la Cantidad de Intentos:\n"))
        agregarUsiarios (id,nombre,apellidos,contraseÃ±a,rol_usuarios,intentos)
                

    if opcion == 4:
        id_equipo  = int(input("intruduzca el ID del Equipo:\n")) 
        nombre_equipo = input("Ingrese el Nombre del Equipo:\n") 
        id_usuario =  int(input("intruduzca el ID del usuario anclado a este Equipo:\n")) 
        agregarEquipo(id_equipo,nombre_equipo,id_usuario)

    if opcion == 5:
        id = int(input("intruduzca el ID:\n"))
        nombre = input("Ingrese el Nombre:\n")
        apellidos = input("Ingrese el Apelidos:\n")
        contraseÃ±a = input("Ingrese la ContraseÃ±a:\n ")
        modificarUsuarios(id,nombre,apellidos,contraseÃ±a)

    if opcion == 6:
        id_equipo  = int(input("intruduzca el ID del Equipo:\n")) 
        nombre_equipo = input("Ingrese el Nombre del Equipo:\n") 
        id_usuario =  int(input("intruduzca el ID del usuario anclado a este Equipo:\n")) 
        ModificarEquipo(id_equipo,nombre_equipo,id_usuario)

    if opcion == 7:
       id = int(input("intruduzca el ID:\n"))
       eliminarUsuarios(id)


    if opcion == 8:
       id_equipo  = int(input("intruduzca el ID del Equipo:\n")) 
       eliminarEquipos(id_equipo)

    if opcion == 9:
       id  = int(input("intruduzca el ID del Usuario:\n")) 
       buscarUsuarios(id)
    
    if opcion == 10:
       id_equipo  = int(input("intruduzca el ID del Equipo:\n")) 
       buscarEquipos(id_equipo)
            