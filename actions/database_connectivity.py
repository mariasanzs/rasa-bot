import mysql.connector
import numpy as np
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

def DataAddPregunta(Pregunta,Opcion1,Puntuacion1, Opcion2,Puntuacion2,Opcion3,Puntuacion3):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="rasa_database"
    )

    mycursor = mydb.cursor()

    
    sql = 'INSERT INTO preguntas(pregunta,opcion1,puntuacion1, opcion2,puntuacion2,opcion3,puntuacion3) VALUES ("{0}","{1}","{2}","{3}","{4}","{5}","{6}");'.format(Pregunta,Opcion1,Puntuacion1, Opcion2,Puntuacion2,Opcion3,Puntuacion3)
    mycursor.execute(sql)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")

def DataSelectPregunta(Id):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="root",
        database="rasa_database"
    )

    mycursor = mydb.cursor()

    
    sql = 'SELECT * FROM preguntas WHERE id = "{0}"; '.format(Id)
    mycursor.execute(sql)

    myresult = mycursor.fetchall()
    #print(myresult)
    result = np.array(myresult)
    print (result[0])
    return [result[0]]

if __name__=="__main__":
    #DataUpdate("Maria")
    #DataValoracion("6","8","7","Mejorar Respuestas")
    #DataAddPregunta("Un conocido te pide el móvil para una llamada, tu le dices: 'Ni de broma, llama tu con el tuyo'","comportamiento inhibido","0","comportamiento asertivo", "0", "comportamiento agresivo", "10")
    #DataSelectPregunta("1")
    DataAddPregunta("Si pienso: 'todo esto es por mi culpa', estoy ","autoexigiendome (deberías)","6","Despersonalizando la culpa", "0", "personalizando la culpa", "10")
    DataAddPregunta("Pensar: 'La vida es demasiado dura' es ...","una creencia racional","0","una creencia irracional", "10", "un pensamiento irracional", "5")
    DataAddPregunta("Si pienso: 'Seguro que no le he caído bien', estoy ...","Sacando conclusiones precipitadas","10","etiquetando a una persona", "3", "generalizando de forma excesiva", "0")
    DataAddPregunta("Pensar que: 'Las cosas deberían de ser fáciles' es ","una trampa del pensamiento","2","una creencia irracional", "10", "un pensamiento lógico", "0")
    DataAddPregunta("Pensar: 'Debería de hacer lo que me diga, aunque no quiera, porque es mi amigo', es ...","una creencia irracional","3","una falta para decir no", "6", "ambas", "10")
    DataAddPregunta("Recriminarle a alguien: 'Siempre hacemos lo que tu dices' es ","una mala de pedir un cambio de conducta","7","una generalización", "4", "ambas, y además es agresivo", "10")
    DataAddPregunta("Es erróneo pensar que la felicidad...","no depende de nosotros","10","las cosas externas no importan", "1", "la buscamos nosotros", "0")
    DataAddPregunta("Has tenido un mal día, pero por no molestar no se lo cuentas a tu pareja, que también estará cansada","es un comportamiento inhibido","10","es una generalización de una situación", "0", "es un comportamiento asertivo", "0")
    DataAddPregunta("Pensar que tienes derecho a cometer errores es ...","una creencia irracional ","0","un derecho asertivo", "10", "una autoinstrucción", "3")
