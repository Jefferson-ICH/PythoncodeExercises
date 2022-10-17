import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="")
cursor1=conexion1.cursor()
cursor1.execute("show databases")
for base in cursor1:
    print(base)
conexion1.close()


#Insersion
""" conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="db_picoyplaca")
cursor1=conexion1.cursor()
sql="INSERT INTO usuarios(nombre,password) VALUES (%s,%s)"
datos=("Miadmin","admin90")
cursor1.execute(sql,datos)
conexion1.commit()
conexion1.close()
 """
#recuperar todas las filas
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="db_picoyplaca")
cursor1=conexion1.cursor()
cursor1.execute("SELECT * from usuarios")
for fila in cursor1:
    print(fila)
conexion1.close()

#Borrar y modificar filas
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",database="db_picoyplaca")
cursor1=conexion1.cursor()
cursor1.execute("DELETE FROM usuarios where id=12")
cursor1.execute("UPDATE usuarios set nombre='python' WHERE id=8")
conexion1.commit()
cursor1.execute("SELECT * from usuarios")
for fila in cursor1:
    print(fila)
conexion1.close()




