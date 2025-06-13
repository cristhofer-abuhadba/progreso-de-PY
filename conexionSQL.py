import pymysql

miConexion= pymysql.connect(host='localhost'
                            ,user='root'
                            ,passwd=''
                            ,db='chat26')
cur=miConexion.cursor()

try:
    #Consulta = cur.execute("INSERT INTO usuarios (id,nickname,password) VALUES (%s,%s,%s)",(3,'cris2','344'))
    Consulta = cur.execute("UPDATE usuarios SET nickname=%s, password=%s WHERE id=%s",
        ('Abuhadba', '123', 0)
    )
    miConexion.commit()
    print('REGISTRO ACEPTADO')
except Exception as e:
    print('erro al ingresar', e)
    miConexion.rollback()

cur.execute('select * from usuarios')
for fila in cur.fetchall():
 print(fila)

miConexion.close()
