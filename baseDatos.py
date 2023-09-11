from pymongo.mongo_client import MongoClient #sirve para importar la libreria de pymongo

#establece una conexion a la base de datos MongoDB
def conexion():
    uri = "mongodb+srv://cagomezj:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    return MongoClient(uri) #sirvevpara devolver un valor desde una función.

#CREATE
""" Código necesario para crear un create en MongoDB"""


#READ
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos(): #sirve para ejecutar el codigo dentro de una funcion
    client = conexion() #sirve para establecer una conexión a una base de datos MongoDB utilizando una URI específica
    db = client.actividad4.data_real #sirve para establecer una referencia a una colección dentro de una base de datos MongoDB
    data_list = [] #se crea una nueva lista vacía y la asigna a la variable data_list
    for data_real_bd in db.find():#sirve para iterar a través de los documentos de una colección MongoDB
        data_list.append(data_real_bd) #sirve para agregar un elemento, en este caso, el valor de la variable data_real_bd, a una lista llamada data_list
    return data_list #sirvevpara devolver un valor desde una función.

#UPDATE
""" Código necesario para actualizar un dato en la BD"""

#DELETE
""" Código necesario para eliminar un dato en la BD"""