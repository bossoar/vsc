from logging import debug
from flask import Flask
from flask import render_template,request
import pyodbc


app = Flask(__name__)


# Conectar base de datos
conn_str = (
    r'Driver={SQL Server};'
    r'Server=SRV13-VMSQL\NORPATAGONICA;'
    r'Database=Prueba;'
    r'Trusted_Connection=yes;'
    )

# cursor.execute("INSERT INTO mytable(name,address) VALUES (?,?)",('thavasi','mumbai'))

# sql = " INSERT INTO Terminal(Numero,Observaciones) VALUES (?,?)",(10,'Prueba')
# conexion = pyodbc.connect(conn_str)
# cursor = conexion.cursor()
# cursor.execute("INSERT INTO Terminal(Numero,Observaciones) VALUES (?,?)",(11,'Prueba'))
# conexion.commit()
# cursor.close()


# s = "<table style='border:1px solid red'>"    
# for row in cursor:    
#         s = s + "<tr>"    
#         for x in row:    
#                 s = s + "<td>" + str(x) + "</td>"    
#                 s = s + "</tr>"    
# conexion.close()    
       

        # try:
               


        
    # OK! conexión exitosa
        # except Exception as e:
     # Atrapar error
                # print("Ocurrió un error al conectar a SQL Server: ", e)

# @app.route('/')
# def index():                

#               return  "<html><body>" + s + "</body></html>"  
# cursor = connection.cursor()    
# cursor.execute("SELECT * FROM EmployeeMaster")   
# 
# 
# 
# 
@app.route('/create')
def create():
    return render_template('terminal/create.html')
    
     
@app.route('/store', methods=['GET', 'POST'])
def storage():
                datos = ''        
                _numero = request.form['txtNumero']
                _observaciones = request.form['txtobservaciones']
                
                conexion = pyodbc.connect(conn_str)
                cursor = conexion.cursor()
                sql= "INSERT INTO Terminal(Numero,Observaciones) VALUES (%s,%s);"
                datos(_numero,_observaciones)
                cursor.execute(sql,datos)
                conexion.commit()
                cursor.close()




   
  
    








if __name__ == '__main__':
    app.run(debug=True)






