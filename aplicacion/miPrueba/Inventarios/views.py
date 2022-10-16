from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from AWS.Cliente import AWS_Servicio
from .models import Pendientes,Inventario
from threading import Thread
import os

# Create your views here.
def index(request):
    return HttpResponse('Estas en la ruta raiz del backend de la prueba')

@csrf_exempt
def upload(request):
    # funcion para gestionar la carga de ficheros solo se admiten .csv
    if request.method == 'POST':
        consecutivo = request.POST.get('consecutivo')
        cliente = request.POST.get('cliente')
        data = None
        # si se definio un consecutivo para actualizar los datos subidos anteriormente de inventario
        if consecutivo and cliente:
            try:
                consecutivo = int(consecutivo)
                # se borran los datos actuales del inventario que tengan el mismo consecutivo
                Inventario.objects.filter(consecutivo=consecutivo).delete()
                # procesando adjuntos enviados
                res,lser = procesar_adjuntos(request.FILES,cliente,True,consecutivo)
                if len(res)>0:
                    msg = f'se han subido exitosamente {len(res)} ficheros del inventario'
                    code = 200
                    data = {'consecutivos':lser}
                else:
                    msg = 'no se ha subido ningun fichero al sistema!'
                    code = 201
            except IndexError:
                return JsonResponse({'msg':'Error con el parametro "consecutivo"','code':500,'data':None})
        # no hay consecutivo se generaran registros nuevos de consecutivos e inventario
        elif cliente:
            # procesando adjuntos enviados
            res,lser = procesar_adjuntos(request.FILES,cliente)
            if len(res)>0:
                msg = f'se han subido exitosamente {len(res)} ficheros del inventario'
                code = 200
                data = {'consecutivos':lser}
            else:
                msg = 'no se ha subido ningun fichero al sistema!'
                code = 201
        else:
            return JsonResponse({'msg':'Error con el parametro "cliente"','code':500,'data':None})
        # activar subrutina de guardar en la base
        proceso()
        return JsonResponse({'msg':msg,'code':code,'data':data})


def proceso():
    # funcion que invoca la funcion en un hilo separado
    hilo = Thread(target=subrutina)
    hilo.start()

def procesar_adjuntos(objetos,cliente,update=False,Id=None):
    # obteniendo todas las llaves de adjuntos
    l_objetos = list(objetos.keys())
    l_pendientes = [] # lista de las url de los archivos subidos a S3
    l_seriales = []  # lista de los consecutivos de los archivos
    aws = AWS_Servicio()
    for key in l_objetos:
        # solo se suben si son archivos csv
        if objetos[key].name.lower().endswith('.csv'):
            key_s3 = f'subidoPrueba/{cliente}/pendientes/{objetos[key].name}'
            aws.subir_s3(key_s3,data=objetos[key].read())
            l_pendientes.append(key_s3)
    if len(l_pendientes) > 0 and not update:
        for it in l_pendientes:
            reg = Pendientes(key_s3=it)
            reg.save()
            l_seriales.append(reg.id)
    elif len(l_pendientes) > 0 and update:
        for it in l_pendientes:
            reg = Pendientes.objects.get(id=Id)
            reg.key_s3 = it # actualizando ruta
            reg.procesado = False  # actualizando bandera
            reg.save()
            l_seriales.append(reg.id)
    return l_pendientes,l_seriales


def subrutina():
    # funcion para invocar la ejecucion del script de guardar en la base
    os.system('python procesarCSV.py')