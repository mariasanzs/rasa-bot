import mysql.connector

def DataUpdate(Nombre, Apellidos):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="rasa_database"
    )

    mycursor = mydb.cursor()

    sql = "CREATE TABLE pacientes (nombre VARCHAR(255), apellidos VARCHAR(255));"
    sql = 'INSERT INTO pacientes(nombre,apellidos) VALUES ("{0}","{1}");'.format(Nombre,Apellidos) 

    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

if __name__=="__main__":
    DataUpdate("Maria","Sanz")