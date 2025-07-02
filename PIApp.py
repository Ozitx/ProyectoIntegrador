from flask import Flask, jsonify, render_template, request, url_for, flash, redirect
from flask_mysqldb import MySQL
import MySQLdb

app = Flask(__name__)

app.config['MYSQL_HOST']="localhost"
app.config['MYSQL_USER']="root"
app.config['MYSQL_PASSWORD']="Cynthia13"
app.config['MYSQL_DB']="QRO_VIC"
app.secret_key = 'mysecretkey'

mysql = MySQL(app)

#Ruta para inicio de sesión
app.route('/')
def home():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM QRO_VIC')
        consultaTodo = cursor.fetchall()
        return render_template('LoginPI.html', errores={}, usuarios = consultaTodo)
    
    except Exception as e:
        print('error al consultar todo: '+e)
        return render_template('LoginPI.html', errores={}, usuarios = [])
    
    finally:
        cursor.close()

#Ruta para registrarse
app.route('/RegistroPI.html')
def registro():
    return render_template('RegistroPI.html')

#Ruta del inicio de la appweb
app.route('/Inicio')
def inicio():
    return render_template('Inicio.html')

#Ruta de ventas de plantas
app.route('/VentasPlantas')
def ventas():
    return render_template('/VentasPlantas.html')

#Ruta para mostrar el Blog del sito
app.route('/Blog')
def blog():
    return render_template('BLOG PI.html')

#Ruta para mostrar MÁS
app.route('/Mas')
def mas():
    return render_template('MÁS.html')

#Ruta para interfaz "Contáctanos"
app.route('/Contactanos')
def contactanos():
    return render_template('Contactanos.html')

if __name__ == '__main__':
    app.run(port= 3000, debug= True)