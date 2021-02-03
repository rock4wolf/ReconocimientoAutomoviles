import tkinter as tk
from tkinter import *
from tkinter import messagebox
import pymysql
import mysql.connector
from testModel import TModel
from Log import BDlog
from tkinter import font as tkfont
from tkinter import filedialog
from trainDeepLizard import TrainModel
from tkinter import ttk,font
from datetime import date
from PIL import ImageTk,Image 
from tkcalendar import Calendar, DateEntry
from tkinter import simpledialog

class StartWindow():
    def __init__(self, master):
        self.master = master
        #self.SwitchWindow
        Label(master,text="Acceso al sistema", bg="gold", fg="white", width="300", height="3", font=("Arial", 15)).pack()
        Label(master,text="").pack()
        Button(master,text="Iniciar sesión", height="3", width="30", command=lambda: self.SwitchWindow(1), font=("Arial", 10)).pack()
        Label(master,text="").pack()
        Button(master,text="Registrar", height="3", width="30", command=lambda: self.SwitchWindow(2), font=("Arial", 10)).pack()
        Button(master,text="Salir", height="3", width="30", command=self.master.destroy, font=("Arial", 10)).pack()

    def SwitchWindow(self,flag):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        if flag == 1:
            app = loginWindow(toplevel)
        else:
            if flag == 2:
                #registro
                app = RegistWindow(toplevel)

class RegistWindow:
    def __init__(self, master):
        self.master = master
        self.Freg = tk.Frame(self.master)
        Label(self.Freg, text="Ingresar los siguientes datos , \n para el registro en el sistema",bg="dark goldenrod", fg="white", width="300", height="3", font=("Arial", 15)).pack()
        Label(self.Freg, text="").pack()
        Label(self.Freg, text="Usuario").pack()
        self.nombreusuario_entry = Entry(self.Freg)
        self.nombreusuario_entry.pack()
        Label(self.Freg).pack()
        Label(self.Freg, text="Contraseña").pack()
        self.contrausuario_entry = Entry(self.Freg)
        self.contrausuario_entry.pack()
        Label(self.Freg).pack()
        Label(self.Freg, text="Correo").pack()
        self.correousuario_entry = Entry(self.Freg)
        self.correousuario_entry.pack()
        Label(self.Freg).pack()
        #command=insertar_datos
        Button(self.Freg, text="Registrar",command=self.nuevoReg).pack()
        Button(self.Freg, text="regresar",command=self.goBack).pack()
        self.Freg.pack()

    def nuevoReg(self):
        flag=BDlog.insertar_datos(self.correousuario_entry,self.contrausuario_entry,self.nombreusuario_entry)
        if flag:
            self.userMail=self.correousuario_entry.get()
            self.SwitchWindow()
        else:
            print("intente de nuevo")

    def goBack(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        app = StartWindow(toplevel)

    def SwitchWindow(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        print("correo: ",self.UserMail)
        if self.UserMail == "upemor@upemor.com":
            app = adminWindow(toplevel,self.UserMail)
        else:
            app = UserWindow(toplevel,self.UserMail)

class loginWindow:
    def __init__(self, master):
        self.UserMail = ""
        self.master = master
        self.Flog = tk.Frame(self.master)
        self.correo_usuario_entry = StringVar()
        self.contra_usuario_entry = StringVar()
        Label(self.Flog, text="Ingresar Usuario y contraseña",bg="navy", fg="white", width="300", height="3", font=("Arial", 15)).pack()
        Label(self.Flog, text="").pack()
        Label(self.Flog, text="Correo ").pack()
        self.correo_usuario_entry = Entry(self.Flog)
        self.correo_usuario_entry.pack()
        Label(self.Flog).pack()
        Label(self.Flog, text="Contraseña").pack()
        self.contra_usuario_entry = Entry(self.Flog,show="*")
        self.contra_usuario_entry.pack()
        Label(self.Flog).pack()
        #command=validacion_datos
        Button(self.Flog, text="Iniciar sesión",command=self.validateUser).pack()
        Button(self.Flog, text="Regresar",command=self.goBack).pack()
        self.Flog.pack()
    
    #destruye y regresa a root
    def goBack(self):
        root.deiconify()
        self.master.withdraw()

    def validateUser(self):
        print("cuenta:",self.correo_usuario_entry.get(),self.contra_usuario_entry.get())
        self.ConBD=BDlog(self.correo_usuario_entry,self.contra_usuario_entry)
        flag=self.ConBD.validacion_datos()
        if flag == 1:
            self.UserMail=self.correo_usuario_entry.get()
            #dirigir a ventana usuario
            self.SwitchWindow(1)
        if flag == 2:
            self.UserMail=self.correo_usuario_entry.get()
            print("correo:",self.UserMail)
            self.SwitchWindow(2)
        if flag == 0:
            print("intente de nuevo")
            self.contra_usuario_entry.set("")
    
    def SwitchWindow(self,flag):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        if flag == 1:
            app = UserWindow(toplevel,self.UserMail)
        else:
            if flag == 2:
                app = adminWindow(toplevel,self.UserMail)
    
    def close_windows(self):
        self.master.destroy()

class adminWindow:
    def __init__(self, master,UserMail):
        self.UserMail=UserMail
        self.master = master
        self.Fadmin = tk.Frame(self.master)
        Label(self.Fadmin, text="Sistema de Administrador",bg="thistle", fg="white", width="300", height="3", font=("Arial", 15)).pack()
        Label(self.Fadmin, text="").pack()
        Button(self.Fadmin,text="Realizar Prueba", height="3", width="30", command=lambda: self.SwitchWindow(1), font=("Arial", 12)).pack()
        Label(self.Fadmin,text="").pack()
        Button(self.Fadmin,text="bitácora", height="3", width="30", font=("Arial", 12),command=lambda: self.SwitchWindow(2)).pack()
        Label(self.Fadmin,text="").pack()
        Button(self.Fadmin,text="entrenar sistema", height="3", width="30", font=("Arial", 12),command=lambda: self.SwitchWindow(5)).pack()
        Label(self.Fadmin,text="").pack()
        Button(self.Fadmin,text="ver usuarios registrados", height="3", width="30", font=("Arial", 12),command=lambda: self.SwitchWindow(3)).pack()
        Label(self.Fadmin,text="").pack()
        Button(self.Fadmin,text="Cerrar Sesion", height="3", width="30", font=("Arial", 12), command=lambda: self.SwitchWindow(4)).pack()
        self.Fadmin.pack()
    
    def SwitchWindow(self,flag):
        if flag == 1:
            toplevel = tk.Toplevel(self.master)
            self.master.withdraw()
            app = pruebaWindow(toplevel,self.UserMail)
        else:
            if flag == 2:
                self.option=0
                self.win = Toplevel()
                self.win.title('selecciona filtro')
                message = "flitro de bitacora"
                Label(self.win, text=message).pack()
                Button(self.win, text='mostrar todos los registros', command=lambda: self.sel(1)).pack()
                Button(self.win, text='mostrar registros de usuario', command=lambda: self.sel(2)).pack()
                #Button(self.win, text='mostrar registros de una fecha', command=lambda: self.sel(3)).pack()
                Button(self.win, text='cancelar', command=self.win.destroy).pack()
            else:
                if flag ==3:
                    toplevel = tk.Toplevel(self.master)
                    self.master.withdraw()
                    app = VerUsuariosW(toplevel,self.UserMail)
                else:
                    if flag==4:
                        self.master.withdraw()
                        toplevel = tk.Toplevel(self.master)
                        app = StartWindow(toplevel)
                    else:
                        if flag ==5:
                            toplevel = tk.Toplevel(self.master)
                            self.master.withdraw()
                            app = trainWindow(toplevel,self.UserMail)


    def sel(self,flag):
        toplevel = tk.Toplevel(self.master)
        self.option=flag
        self.win.destroy()
        self.master.withdraw()
        app = bitacoraWindow(toplevel,self.UserMail,self.option)

class UserWindow:
    def __init__(self, master,UserMail):
        self.UserMail=UserMail
        self.master = master
        self.Fuser = tk.Frame(self.master)
        Label(self.Fuser, text="Sistema de Usuario",bg="thistle", fg="white", width="300", height="3", font=("Arial", 15)).pack()
        Label(self.Fuser, text="").pack()
        Button(self.Fuser,text="Realizar Prueba", height="3", width="30", command=lambda: self.SwitchWindow(1), font=("Arial", 12)).pack()
        Label(self.Fuser,text="").pack()
        Button(self.Fuser,text="bitácora", height="3", width="30", font=("Arial", 12), command=lambda: self.SwitchWindow(2)).pack()
        Label(self.Fuser,text="").pack()
        Button(self.Fuser,text="Cerrar Sesion", height="3", width="30", font=("Arial", 12), command=lambda: self.SwitchWindow(3)).pack()
        self.Fuser.pack()

    def SwitchWindow(self,flag):
        if flag == 1:
            toplevel = tk.Toplevel(self.master)
            self.master.withdraw()
            app = pruebaWindow(toplevel,self.UserMail)
        else:
            if flag == 2:
                self.option=0
                self.win = Toplevel()
                self.win.title('selecciona filtro')
                message = "flitro de bitacora"
                Label(self.win, text=message).pack()
                Button(self.win, text='mostrar todos los registros', command=lambda: self.sel(1)).pack()
                Button(self.win, text='mostrar registros de usuario', command=lambda: self.sel(2)).pack()
                Button(self.win, text='mostrar registros de una fecha', command=lambda: self.sel(3)).pack()
                Button(self.win, text='cancelar', command=self.win.destroy).pack()
            else:
                if flag == 3:
                    self.master.withdraw()
                    toplevel = tk.Toplevel(self.master)
                    app = StartWindow(toplevel)

    def sel(self,flag):
        toplevel = tk.Toplevel(self.master)
        self.option=flag
        self.win.destroy()
        self.master.withdraw()
        app = bitacoraWindow(toplevel,self.UserMail,self.option)

class bitacoraWindow:
    def __init__(self, master,UserMail,flag):
        self.flag=flag
        print("seleccion: ",self.flag)
        self.UserMail=UserMail
        self.master = master
        dbConnect = {
            'host':'localhost',
            'user':'root',
            'password':'12345',
            'database':'Estanciados'
        }
        self.conexion = mysql.connector.connect(**dbConnect)
        self.cursor = self.conexion.cursor()
        if flag == 1:
            #todos los registros
            sql= "select * from bitacora"
            self.cursor.execute(sql)
            self.resultados = self.cursor.fetchall()
        else:
            if flag==2:
                #por usuario
                print(self.UserMail)
                if self.UserMail !="":
                    sql= "select Id_Usuario from Usuario where correo ='"+self.UserMail+"'"
                self.cursor.execute(sql)
                self.resultados = self.cursor.fetchall()
                print("resultado: ",self.resultados,"pimer elemento: ",self.resultados[0][0])
                self.idUser= self.resultados[0][0]
                sql= "select * from bitacora where Id_Usuario= %s" %self.idUser
                self.cursor.execute(sql)
                self.resultados = self.cursor.fetchall()
            else:
                if flag ==3:
                    #por fecha
                    self.top = tk.Toplevel()
                    ttk.Label(self.top, text='escoge fecha').pack(padx=10, pady=10)
                    self.cal = DateEntry(self.top, width=12, background='darkblue',foreground='white', borderwidth=2)
                    self.cal.pack(padx=10, pady=10)
                    Button(self.top, text='aceptar',command=self.getDate).pack()    
        if flag!=3:
            self.createTable()

        

    def createTable(self):
        self.cursor.close()
        self.conexion.close()
        self.Fbit=tk.Frame(self.master)
        self.lblidTrain = Label(self.master, text="Id Entrenamiento", width=10)
        self.lblidTrain.grid(row=0, column=1,sticky = W)
        self.lblidBit = Label(self.master, text="Id Bitacora", width=10)
        self.lblidBit.grid(row=0, column=2,sticky = W)
        self.LblUser = Label(self.master, text="Usuario", width=10)
        self.LblUser.grid(row=0, column=3,sticky = W)
        self.lblDate = Label(self.master, text="Fecha", width=10)
        self.lblDate.grid(row=0, column=4,sticky = W)
        self.lblPrec = Label(self.master, text="precision", width=10)
        self.lblPrec.grid(row=0, column=5,sticky = W)
        self.lblRes = Label(self.master, text="resultado", width=10)
        self.lblRes.grid(row=0, column=6,sticky = W)
        self.lblRep = Label(self.master, text="reporte", width=10)
        self.lblRep.grid(row=0, column=7,sticky = W)
        
        for index, data in enumerate(self.resultados):
            Label(self.master, text=data[0]).grid(row=index+1, column=1)
            Label(self.master, text=data[1]).grid(row=index+1, column=2)
            Label(self.master, text=data[2]).grid(row=index+1, column=3)
            Label(self.master, text=data[3]).grid(row=index+1, column=4)
            Label(self.master, text=data[4]).grid(row=index+1, column=5)
            Label(self.master, text=data[5]).grid(row=index+1, column=6)
            Label(self.master, text=data[6]).grid(row=index+1, column=7)
        self.btnBack=Button(self.master,text="regresar",command=self.goBack).grid()

    def getDate(self):
        self.fecha=date.today()
        self.fecha=self.cal.get()
        self.fecha.strftime('%Y-%m-%d')
        sql= "select * from Bitacora where Agre_Fecha = %s"%self.fecha
        self.cursor.execute(sql)
        self.resultados = self.cursor.fetchall()
        self.top.destroy()
        self.createTable()
        
        
    
    def goBack(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        print("correo: ",self.UserMail)
        if self.UserMail == "upemor.com":
            app = adminWindow(toplevel,self.UserMail)
        else:
            app = UserWindow(toplevel,self.UserMail)
    
class pickDate():
    def __init__(self):
        self.top = tk.Toplevel()
        ttk.Label(self.top, text='Choose date').pack(padx=10, pady=10)
        self.cal = DateEntry(self.top, width=12, background='darkblue',foreground='white', borderwidth=2)
        self.cal.pack(padx=10, pady=10)
        Button(self.top, text='aceptar',command=self.getDate).pack()
        
    def getDate(self):
        self.top.destroy()
        return self.cal
    
class pruebaWindow:
    def __init__(self, master,UserMail):
        self.UserMail=UserMail
        self.master = master
        self.Fprueba = tk.Frame(self.master)
        fontb = font.Font(weight='bold')
        self.lblimg = Label(self.Fprueba, text="imagen",font=fontb)
        self.boximg = Entry(self.Fprueba,width=30)
        #self.separ = ttk.Separator(self.Fprueba, orient=VERTICAL)
        self.btnSearch = Button(self.Fprueba, text="Buscar imagen",command=self.FileOpen)
        self.btnAceptar = Button(self.Fprueba, text="Aceptar",state='disabled',command=self.accept)
        self.lblimg.pack(side=LEFT, expand=1,padx=5,pady=5)
        self.boximg.pack(side=LEFT, expand=1,padx=5,pady=5)
        self.btnAceptar.pack(side=LEFT, expand=1,padx=5,pady=5)
        #self.separ.pack(side=LEFT, fill=BOTH, expand=1,padx=5,pady=5)
        self.btnSearch.pack(side=LEFT, expand=1,padx=5,pady=5)
        Button(self.Fprueba,text="regresar",command=lambda: self.SwitchWindow()).pack()
        self.Fprueba.pack()
        
    def FileOpen(self):
        #aqui me quede
        self.img_Path=filedialog.askopenfilename(initialdir = "/",title = "selecciona la imagen",filetype = (("jpeg,jpg","*.jpg"),("All Files","*.*")))
        print("imagen :",self.img_Path)
        self.boximg.insert(0,self.img_Path)
        self.img = Image.open(self.img_Path)
        self.img = self.img.resize((224,224),Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.panel = Label(self.Fprueba,image = self.img)
        self.panel.image = self.img
        self.btnAceptar.config(state="normal")
        self.panel.pack()
        
    def accept(self):
        self.new_model=TModel('D:/desarrollo/Reconocimiento/CarsModel.model')
        self.new_model.PredictImg(self.img_Path)
        self.prec = self.new_model.getPrecision()
        self.result = self.new_model.getResultado()
        self.report=messagebox.askyesno(title="verificar prueba",message="¿la prediccion fue correcta?")
        self.insertBD()
 
    def SwitchWindow(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        print("correo: ",self.UserMail)
        if self.UserMail == "upemor.com":
            app = adminWindow(toplevel,self.UserMail)
        else:
            app =UserWindow(toplevel,self.UserMail)

    def insertBD(self):
        today = date.today()
        dbConnect = {
        'host':'localhost',
        'user':'root',
        'password':'12345',
        'database':'Estanciados'
        }
        conexion = mysql.connector.connect(**dbConnect)
        cursor = conexion.cursor()
        print(self.UserMail)
        if self.UserMail !="":
            sql= "select Id_Usuario from Usuario where correo ='"+self.UserMail+"'"
        cursor.execute(sql)
        self.resultados = cursor.fetchall()
        print("resultado: ",self.resultados,"pimer elemento: ",self.resultados[0][0])
        self.idUser= self.resultados[0][0]
        if(self.report):
            reporte=1
        else:
            reporte=0
        sqlInsertar = "insert into Bitacora(Id_Entre,Id_Usuario,Agre_Fecha,Pre,Resultado,Reporte)values({},{},'{}',{},'{}','{}')".format(1,self.idUser, today,self.prec,self.result,reporte)
        try:
            if (self.idUser== ''):
                raise Exception("Esta vacio algun parametro")
                messagebox.showinfo(message="Parametro Vacio", title="Aviso")
                return False
            else:
                cursor.execute(sqlInsertar)
                conexion.commit()
                messagebox.showinfo(message="prueba agregada a la bitacora exitoso", title="Aviso")
                cursor.close()
                conexion.close()
                return True
        except Exception as e:
            messagebox.showinfo(message="prueba agregada a la bitacora Fallido", title="Aviso")
            print("Ocurrio un error",e)

class VerUsuariosW:
    def __init__(self, master,UserMail):
        self.UserMail=UserMail
        self.master = master
        dbConnect = {
            'host':'localhost',
            'user':'root',
            'password':'12345',
            'database':'Estanciados'
        }
        self.conexion = mysql.connector.connect(**dbConnect)
        self.cursor = self.conexion.cursor()
        sql= "select * from Usuario"
        self.cursor.execute(sql)
        self.resultados = self.cursor.fetchall()
        self.cursor.close()
        self.conexion.close()
        self.lblidTrain = Label(self.master, text="Id usuario", width=10)
        self.lblidTrain.grid(row=0, column=1,sticky = W)
        self.lblidBit = Label(self.master, text="Nombre", width=10)
        self.lblidBit.grid(row=0, column=2,sticky = W)
        self.LblUser = Label(self.master, text="correo", width=10)
        self.LblUser.grid(row=0, column=3,sticky = W)
        
        for index, data in enumerate(self.resultados):
            Label(self.master, text=data[0]).grid(row=index+1, column=1)
            Label(self.master, text=data[1]).grid(row=index+1, column=2)
            Label(self.master, text=data[2]).grid(row=index+1, column=3)
        self.btnBack=Button(self.master,text="regresar",command=self.goBack).grid()
        Button(self.master,text="editar",command=self.editar).grid()
        Button(self.master,text="eliminar",command=self.eliminar).grid()

    def editar(self):
        self.idUser = simpledialog.askstring("Input", "Id usuario a editar:",parent=self.master)
        self.userCorreo = simpledialog.askstring("Input", "nuevo correo:",parent=self.master)
        dbConnect = {
        'host':'localhost',
        'user':'root',
        'password':'12345',
        'database':'Estanciados'
        }

        conexion = mysql.connector.connect(**dbConnect)
        cursor = conexion.cursor()
        sqlModificar = "Update Usuario set Correo =%s where Id_Usuario = %s"
        sql = "UPDATE customers SET address = %s WHERE address = %s"
        val = (self.userCorreo, self.idUser)
        cursor.execute(sqlModificar,val)
        conexion.commit()
        cursor.close()
        conexion.close()
        self.refresh()

    def eliminar(self):
        self.idUser = simpledialog.askstring("Input", "Id usuario a eliminar:",parent=self.master)
        dbConnect = {
        'host':'localhost',
        'user':'root',
        'password':'12345',
        'database':'Estanciados'
        }

        conexion = mysql.connector.connect(**dbConnect)
        cursor = conexion.cursor()
        
        sqlEliminar = "delete from Usuario where Id_Usuario = %s"%self.idUser
        cursor.execute(sqlEliminar)
        conexion.commit()
        cursor.close()
        conexion.close()
        self.refresh()

    def goBack(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        app = adminWindow(toplevel,self.UserMail)

    def refresh(self):
        toplevel = tk.Toplevel(self.master)
        self.master.withdraw()
        app = VerUsuariosW(toplevel,self.UserMail)
        
class trainWindow:
    def __init__(self, master):
        self.master = master
        self.Ftrain = tk.Frame(self.master)
        self.CTrainPath=StringVar()
        self.CValPath=StringVar()
        self.CTestPath=StringVar()
        self.NCTrainPath=StringVar()
        self.NCValPath=StringVar()
        self.NCTestPath=StringVar()
        Label(self.Ftrain, text="Entrenamiento de sistema",bg="thistle", fg="white", width="300", height="3", font=("Arial", 15)).pack()
        Label(self.Ftrain, text="").pack()
        Label(self.Ftrain, text="ruta de imagenes de autos para entrenamiento:").pack()
        Label(self.Ftrain,textvariable=self.CTrainPath).pack()
        Button(self.Ftrain, text="Buscar ruta",command=lambda: self.fileDialog(self.CTrainPath)).pack()
        Label(self.Ftrain, text="ruta de imagenes para validacion:").pack()
        Label(self.Ftrain,textvariable=self.CValPath).pack()
        Button(self.Ftrain, text="Buscar ruta",command=lambda: self.fileDialog(self.CValPath)).pack()
        Label(self.Ftrain, text="ruta de imagenes para pruebas:").pack()
        Label(self.Ftrain,textvariable=self.CTestPath).pack()
        Button(self.Ftrain, text="Buscar ruta",command=lambda: self.fileDialog(self.CTestPath)).pack()
        Label(self.Ftrain, text="ruta de imagenes sin autos para entrenamiento:").pack()
        Label(self.Ftrain,textvariable=self.NCTrainPath).pack()
        Button(self.Ftrain, text="Buscar ruta",command=lambda: self.fileDialog(self.NCTrainPath)).pack()
        Label(self.Ftrain, text="ruta de imagenes para validacion:").pack()
        Label(self.Ftrain,textvariable=self.NCValPath).pack()
        Button(self.Ftrain, text="Buscar ruta",command=lambda: self.fileDialog(self.NCValPath)).pack()
        Label(self.Ftrain, text="ruta de imagenes para pruebas:").pack()
        Label(self.Ftrain,textvariable=self.NCTestPath).pack()
        Button(self.Ftrain, text="Buscar ruta",command=lambda: self.fileDialog(self.NCTestPath)).pack()
        self.btnAceptar = Button(self.Ftrain, text="Aceptar",state='disabled',command=self.accept)
        self.btnAceptar.pack()
        Button(self.Ftrain, text="regresar",command=self.goBack).pack()

    def fileDialog(self,labelPath):
        self.filePath=filedialog.askdirectory()
        labelPath.set(self.filePath)
        if self.NCTrainPath.get()!="" and self.NCTestPath.get()!="" and self.CTrainPath.get()!="" and self.CValPath.get()!="" and self.CTestPath.get()!="" and self.NCValPath.get()!="":
            self.btnAceptar.state(["!disabled"])

    def accept(self):
        new_train = TrainModel(self.CTrainPath,
            self.CValPath,
            self.CTestPath,
            self.NCTrainPath,
            self.NCValPath,
            self.NCTestPath)

    def goBack(self):
        self.master.withdraw()
        toplevel = tk.Toplevel(self.master)
        app = adminWindow(toplevel,self.UserMail)   

if __name__ == "__main__":
    root = tk.Tk()
    #ventana principal
    cls = StartWindow(root)
    root.mainloop()