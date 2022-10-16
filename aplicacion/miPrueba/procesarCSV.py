import psycopg2
import pandas as pd
from io import StringIO
from AWS.Cliente import AWS_Servicio

def transferir_datos(cliente,key,Id,cursor):
    dic_campos = {'FechaInventario':'FechaInventario','GLN_Cliente':'GLN_Cliente_id','GLN_Sucrusal':'GLN_Sucrusal_id',
    'Gtin_Producto':'Gtin_Producto_id','Inventario_Final':'Inventario_Final','PrecioUnidad':'PrecioUnidad'}
    obj_fichero = cliente.obtener_objeto(key)
    data_bin = obj_fichero.read()
    df = pd.read_csv(StringIO(data_bin.decode()))
    dic = df.to_dict('list')
    #print(dic)
    keys = list(dic.keys())
    nreg = len(dic[keys[0]]) # obteniendo longitud de los datos
    nkeys = len(keys) # obtiendo cantidad de campos
    # construyendo vector de campos de sql
    cad_campos = "("
    for campo in keys:
        cad_campos += f'"{dic_campos[campo]}",'
    cad_campos +=  'consecutivo_id)'
    # para cada dato o registro se genera el insert correspondiente
    for it in range(nreg):
        sql = f'insert into "Inventarios_inventario" {cad_campos} values '
        # se contruye vector de valores de sql
        cad_valores = '('
        for itk in range(nkeys):
            cad_valores += f"'{dic[keys[itk]][it]}',"
        cad_valores += f"'{Id}');"
        sql += cad_valores
        # se ejecuta el sql
        cursor.execute(sql)
    # borrar el objeto del directorio pendientes
    cliente.borrar_objeto(key)
    # guardar objeto en directorio procesado
    key_nueva = key.replace('/pendientes/','/procesados/')
    cliente.subir_s3(key_nueva,data=data_bin)


# revisar si hay nuevos datos sin procesar
conn = psycopg2.connect(host='172.18.0.1',database='prueba',user='root',password='kevin1234')
cur = conn.cursor()

sql = 'select id,key_s3 from "Inventarios_pendientes"  where procesado = false;'
cur.execute(sql)
l_data = cur.fetchall()
# si hay nuevos documentos
if len(l_data) > 0:
    aws = AWS_Servicio()
    for Id,key in l_data:
        transferir_datos(aws,key,Id,cur) # se realizan los insert a la base
        conn.commit()  # se guardan cambios
        # actualizar el registro como procesado
        sql = f'update "Inventarios_pendientes" set prcesado=true where id={Id}'
        cur.execute(sql)
        conn.commit()  # se guardan cambios
# cerrando conexion con base de datos
conn.close()

