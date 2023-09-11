from data.data import *  #sirve para importar todas las librerias del archivo data
from BD.baseDatos import * #sirve para importar todas las librerias del archivo BD (base de datos)
from sklearn.linear_model import LinearRegression #sirve para importar las librerias de sklearn
from grafica.grafica import * #sirve para importar todas las librerias del archivo grafica
import pandas as pd #sirve para importar las librerias de pandas

#Datos del excel
dataTeoricoEsfuerzo, dataTeoricoDeformacion = dataTeorico() #Sirve para asignar los valores devueltos por una función en múltiples variables.

#Datos de la base de datos y realizamos el modelo
data_list = lecturaDatos() #Sirve para llamar a una función llamada lecturaDatos() y asignar el valor de retorno de esa función a la variable data_list
data_real = pd.DataFrame(data_list) #Sirve para convertir una lista de datos en un DataFrame de pandas en Python
data_real_fit = data_real #sirve para nombrar como data_real al data_real_fit
X = data_real_fit['Esfuerzo[kN]'].values.reshape(-1, 1) #sirve para nombrar la variable X y el .reshape(-1, 1) cambia la forma del arreglo de numpy.
y = data_real_fit['Deformacion[mm]'].values.reshape(-1, 1)#sirve para nombrar la variable Y y el .reshape(-1, 1) cambia la forma del arreglo de numpy.
x_lim = data_real['Esfuerzo[kN]'].iloc[-1] #Sirve para asignar el valor del último elemento de una columna específica de un DataFrame de pandas a la variable x_lim
y_lim = data_real['Deformacion[mm]'].iloc[-1] #Sirve para asignar el valor del último elemento de una columna específica de un DataFrame de pandas a la variable y_lim
model = LinearRegression() #sirve para crear una regresión lineal en Python
model.fit(X, y) #Sirve para entrenar un modelo de aprendizaje automático en Python
prediction = round(model.predict(np.array([3000]).reshape(-1, 1))[0][0],1) #Sirve para una predicción de regresión lineal
print('la predicción a 1000 kN es de: ', prediction ,'mm') #sirve para mostrar información de la regresion lineal


dataRealEsfuerzo = data_real['Esfuerzo[kN]'] #Sirve para crear una nueva variable llamada dataRealEsfuerzo que almacena una columna específica de un DataFrame en Python
dataRealDeformacion = data_real['Deformacion[mm]'] #Sirve para crear una nueva variable llamada dataRealEsfuerzo que almacena una columna específica de un DataFrame en Python

#realizamos la lectura de las gráficas
gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) #sirve para ver la gráfica de esfuerzo y deformación
gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion) #sirve para ver la prediccion de la gráfica de esfuerzo y deformación
gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model)#sirve para ver la prediccion de la gráfica de esfuerzo y deformación para un valor de entrada de 3000

