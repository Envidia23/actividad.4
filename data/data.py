import pandas as pd #sirve para importar la libreria de pandas

# sirve para importar los datos del archivo csv
data_teorico = pd.read_csv(r"C:\Users\user\Desktop\actividad5\data\Data ingeniero.csv")

#Código general
""" En caso que se exigiera realizar la limpieza de la data se haría aca"""

def dataTeorico(): #sirve para ejecutar el codigo dentro de una funcion
    dataTeoricoEsfuerzo = data_teorico['Esfuerzo[kN]'] #Sirve para acceder a un valor específico y llamarlo de una manera especifica
    dataTeoricoDeformacion = data_teorico['Deformacion[mm]'] #Sirve para acceder a un valor específico y llamarlo de una manera especifica
    return dataTeoricoEsfuerzo, dataTeoricoDeformacion ##sirvevpara devolver un valor desde una función.


