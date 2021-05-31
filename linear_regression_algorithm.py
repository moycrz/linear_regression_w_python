import numpy as np
import matplotlib.pyplot as plt

#Ecuacion de minimos cuadrados
def estimate_b0_b1(x, y):
  '''
  En esta funcion vamos a calular todo los datos necesarios para
  graficar nuestro modelo de regresion lineal, las operaciones
  hechas en la misma son sacadas del metodo de minimos cuadrados
  '''
  n = np.size(x)
  #Obtenemos promedios de X y de Y
  #m hace referencia a media
  m_x, m_y = np.mean(x), np.mean(y) 

  #Calcular sumatoria de XY y mi sumatoria de XX
  sumatoria_xy = np.sum((x-m_x)*(y-m_y))
  sumatoria_xx = np.sum(x*(x-m_x))

  #Coeficiente de regresion
  b_1 = sumatoria_xy / sumatoria_xx
  b_0 = m_y - b_1*m_x 

  return(b_0, b_1)


#Funcion de graficado
def plot_regression(x, y, b):
  '''
  En esta funcion vamos a graficar los parametros dados
  '''
  #market se refiere al tipo de señalizacion que se mostrara, en este caso un punto
  #color se refiere al color que se mostrara en los puntos, s al tamaño
  plt.scatter(x, y, color = 'g', marker = 'o', s = 30)
  y_pred = b[0] + b[1]*x #formula de regresion
  plt.plot(x, y_pred, color = 'b')

  #etiquetas
  plt.xlabel('x-Independiente')
  plt.xlabel('y-Dependiente')
  
  plt.show()


#Codigo MAIN
def main():
  #Este sera nuestro dataset
  x = np.array([1,2,3,4,5])
  y = np.array([2,3,5,6,5])

  #Obtenemos b1 y b2 con base en nuestro dataset
  b = estimate_b0_b1(x, y)
  print('Los valores b0 = {}, b1= {}'.format(b[0], b[1]))

  #Graficamos nuestra linea de regresion
  plot_regression(x, y, b)


if __name__ == '__main__':
  main()