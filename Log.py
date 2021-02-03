import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
import mysql.connector


class BDlog():
    def __init__(self,correo_usuario_entry,contra_usuario_entry):
        self.correo_usuario_entry=correo_usuario_entry
        self.contra_usuario_entry=contra_usuario_entry

    def insertar_datos(correo,userpass,nombreusuario_entry,idusuario_entry):
        dbConnect = {
        'host':'localhost',
        'user':'root',
        'password':'12345',
        'database':'Estanciados'
        }
        conexion = mysql.connector.connect(**dbConnect)
        cursor = conexion.cursor()
        sql= "select * from Usuario"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        for datos in resultados:
            print(datos)

        sqlInsertar = "insert into Usuario(Nombre,Correo,Contraseña)values('{}','{}','{}')".format(nombreusuario_entry.get(), userpass.get(), correo.get())
        try:
            if (nombreusuario_entry.get() == ''):
                raise Exception("Esta vacia algun parametro")
                messagebox.showinfo(message="Parametro Vacio", title="Aviso")
                return False
            else:
                messagebox.showinfo(message="Registro exitoso", title="Aviso")
                cursor.execute(sqlInsertar)
                conexion.commit()
                cursor.close()
                conexion.close()
                return True
        except Exception as e:
            messagebox.showinfo(message="Registro Fallido", title="Aviso")
            print("Ocurrio un error",e)

    #delete
    def eliminar_datos(self,correousuario_entry):
        dbConnect = {
        'host':'localhost',
        'user':'root',
        'password':'12345678',
        'database':'Estanciados'
        }

        conexion = mysql.connector.connect(**dbConnect)
        cursor = conexion.cursor()
        sql= "select * from Usuario"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        #print(resultados)
        #for datos in resultados:
        #   print(datos)
        #print(str(datos[0])+"  "+str(datos[1]))
        #insertar
        sqlEliminar = "delete from Usuario where Correo ={}".format(correousuario_entry)
    # delete from Usuario where Id_Usuario =%s
        try:
            messagebox.showinfo(message="Eliminado", title="Aviso")
            # raise Exception("Esta vacia algun parametro")
            cursor.execute(sqlEliminar)
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            messagebox.showinfo(message="Ocurrio un error", title="Aviso")
            print("Ocurrio un error",e)



    #actualizar
    def update_datos(self,correousuario_entry):
        dbConnect = {
        'host':'localhost',
        'user':'root',
        'password':'12345',
        'database':'Estanciados'
        }

        conexion = mysql.connector.connect(**dbConnect)
        cursor = conexion.cursor()
        sql= "select * from Usuario"
        cursor.execute(sql)
        resultados = cursor.fetchall()
        sqlModificar = "Update Usuario set Nombre ='{}' whereCorreo = {}".format(correousuario_entry.get())

    # delete from Usuario where Id_Usuario =%s
        try:
            messagebox.showinfo(message="Se actualizo el usuario", title="Aviso")
            cursor.execute(sqlModificar)
            conexion.commit()
            cursor.close()
            conexion.close()
        except Exception as e:
            print("No se pudo modificar",e)

            
    def validacion_datos(self):
        adminMail = "upemor.com"
        adminPass = "iti2020"
        if(self.correo_usuario_entry.get()==adminMail and self.contra_usuario_entry.get() == adminPass):
            return 2
        else:
            dbConnect = {
            'host':'localhost',
            'user':'root',
            'password':'12345',
            'database':'Estanciados'
            }
            try:
                conexion = mysql.connector.connect(**dbConnect)
                cursor = conexion.cursor()
                sqlValidar =("select * FROM Usuario WHERE Correo ='"+self.correo_usuario_entry.get()+"'  and Contraseña = '"+self.contra_usuario_entry.get()+"'")
                cursor.execute(sqlValidar)
                resultados = cursor.fetchall()
                print(resultados)
                if (resultados):
                    conexion.commit()
                    messagebox.showinfo(title="Inicio de sesión ", message="Usuario correcto")
                    cursor.close()
                    conexion.close()
                    return 1
                else:
                    return 0
            except Exception as e:
                messagebox.showinfo(title="Inicio de sesión ", message="Usuario invalido")
                print("Ocurrio un error",e)
                return 0