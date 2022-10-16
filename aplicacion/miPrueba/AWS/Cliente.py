import boto3

BUCKET = 'archivosred'

class AWS_Servicio:
    key_id = 'AKIAZFLNJNGOXVY7TRBD'
    key_secret = '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'

    def obtener_servicio(self, servicio):
        """Metodo utilizado para obtener un cliente del servicio requerido
           params: servicio => str
           return: cliente(Obj)
        """
        cliente = boto3.client(servicio,
                               region_name="us-east-2",
                               aws_access_key_id=self.key_id,
                               aws_secret_access_key=self.key_secret
                               )
        return cliente

    def subir_s3(self, key, archivo=None, data=None):
        """Metodo utilizado para subir archivos a S3
           # params: key => str
           # params: archivo => str
           # params: data => IOBuffer
           # return: => dict
        """
        s3 = self.obtener_servicio('s3')
        if archivo or data:
            if archivo:
                f = open(archivo, 'rb')
                data = f.read()
                f.close()
            s3.put_object(
                ACL='public-read',
                Body=data,
                Bucket=BUCKET,
                Key=key
            )
            return {'error': False, 'mensaje': '', 'data': None}
        else:
            return {'error': True, 'mensaje': 'Inconsistencia con los parametros suministrados', 'data': None}


    def obtener_objeto(self,key:str):
        """ Metodo para obtener la informacion de un objeto almacenado en S3
        """
        s3 = self.obtener_servicio('s3')
        obj = s3.get_object(Bucket=BUCKET,Key=key)
        return obj['Body']

    def borrar_objeto(self,key:str):
        """ Metodo para borrar la informacion de un objeto almacenado en S3
        """
        s3 = self.obtener_servicio('s3')
        s3.delete_object(Bucket=BUCKET,Key=key)