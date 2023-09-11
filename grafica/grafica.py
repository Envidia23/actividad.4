import matplotlib.pyplot as plt #sirve para instalar la libreria matplotlib
import numpy as np #sirve para instalar la libreria numpy



def gr_con_prediccion(x_lim,y_lim,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #es una fncion que sirve para generar graficos esfuerzo vs deformacion
    
    
    plt.figure(figsize=(15, 6))#Sirve para configurar el tamaño de la figura de un gráfico
    plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #Sirve para crear un gráfico en Python. 
    plt.scatter(	dataRealEsfuerzo, dataRealDeformacion, color='red') #Sirve para crear un gráfico de dispersión de color rojo
    plt.xlabel('Esfuerzo [kN]') #Sirve para nombrar al eje X de un grafico
    plt.ylabel('Deformación [mm]') #Sirve para nombrar al eje Y de un gráfico
    plt.title('Gráfica 2: teórico versus real [ZOOM]') #Sirve para agregar un título al gráfico
    plt.xlim(0, x_lim) #Sirve para establecer los límites del eje X
    plt.ylim(0, y_lim) #Sirve para establecer los límites del eje Y
    plt.grid() #Sirve para agregar una grilla al grafico
    plt.gca().invert_yaxis() #Sirve para invertir el eje Y 
    plt.show() #Sirve para mostrar el gráfico

def gr_con_prediccion_3000(prediction,dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion,model): #es una fncion que sirve para generar graficos
  plt.figure(figsize=(15, 6)) #Sirve para configurar el tamaño de la figura de un gráfico
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #Sirve para crear un gráfico en Python
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #Sirve para crear un gráfico de dispersión de color rojo
  plt.plot(np.linspace(0,1000).reshape(-1,1),model.predict(np.linspace(0,1000).reshape(-1,1)),'m') #Sirve para crear un gráfico en Python
  plt.scatter(	3000 , prediction, color='green') #Sirve para crear un gráfico de dispersión de color verde
  plt.xlabel('Esfuerzo [kN]') #Sirve para nombrar al eje X de un grafico
  plt.ylabel('Deformación [mm]') #Sirve para nombrar al eje Y de un grafico
  plt.title('Gráfica 3: Predicción a una carga de 3000 kN') #Sirve para agregar un título al gráfico
  plt.xlim(0, 3000) #Sirve para establecer los límites del eje X
  plt.ylim(0, 45) #Sirve para establecer los límites del eje Y
  plt.grid() #Sirve para agregar una grilla al grafico
  plt.gca().invert_yaxis() #Sirve para invertir el eje Y
  plt.show() #Sirve para mostrar el gráfico

def gr_sin_prediccion(dataTeoricoEsfuerzo,dataTeoricoDeformacion,dataRealEsfuerzo,dataRealDeformacion): #es una fncion que sirve para generar graficos esfuerzo vs deformacion
  plt.figure(figsize=(15, 6)) #Sirve para configurar el tamaño de la figura de un gráfico
  plt.plot(	dataTeoricoEsfuerzo , dataTeoricoDeformacion) #Sirve para crear un gráfico en Python
  plt.scatter(	dataRealEsfuerzo , dataRealDeformacion, color='red') #Sirve para crear un gráfico de dispersión de color rojo
  plt.xlabel('Esfuerzo [kN]') #Sirve para nombrar al eje X de un grafico
  plt.ylabel('Deformación [mm]') #Sirve para nombrar al eje Y de un grafico
  plt.title('Gráfica 1: teórico versus real') #Sirve para agregar un título al gráfico
  plt.grid() #Sirve para agregar una grilla al grafico
  plt.gca().invert_yaxis() #Sirve para invertir el eje Y
  plt.show() #Sirve para mostrar el gráfico