import mysql.connector

def DataUpdate(Nombre):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="rasa_database"
    )

    mycursor = mydb.cursor()

    hola = mycursor.execute("SELECT * FROM pacientes WHERE nombre='%s' % (Nombre)")
    myresult = mycursor.fetchall()
    if (hola):
         print("este nombre ya estaba")
    else:
         sql = 'INSERT INTO pacientes(nombre) VALUES ("{0}");'.format(Nombre)
         mycursor.execute(sql)

    #sql = 'INSERT IGNORE INTO pacientes(nombre) VALUES ("{0}");'.format(Nombre)
    #mycursor.execute(sql)

    

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def DataValoracion(Puntos1,Puntos2,Puntos3,Cambios):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="rasa_database"
    )

    mycursor = mydb.cursor()

    sql = 'INSERT INTO valoracion(fecha,pregunta1,pregunta2,pregunta3,cambios) VALUES (now(),"{0}","{1}","{2}","{3}");'.format(Puntos1,Puntos2,Puntos3,Cambios)
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

if __name__=="__main__":
    DataUpdate("Maria")
    DataValoracion("6","8","7","Mejorar Respuestas")