import multiprocessing 
import math

def calcular_funcion(numero):
  resultado=math.factorial(numero)
  print(f"EL factorial de {numero} es {resultado}")
  return resultado 

if __name__=="__main__":
 numeros=[1000 + x for x in range(5)]
 with multiprocessing.Pool(processes=5) as pool:
  resultados=pool.map(calcular_funcion,numeros)
  print("Resultados",resultados)
