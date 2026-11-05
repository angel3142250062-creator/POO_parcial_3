import mysql.connector

try:
    conexion= mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database='bd_coches'
        
    )
    cursor=conexion.cursor(buffered=True)
except:
    print("......!Por el momento no es posible conectarse a la base de datos")
    
